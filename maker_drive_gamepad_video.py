import queue

import cv2
from numpy import rot90
from os import getenv
import pigpio
import pygame
import threading

pi = pigpio.pi()

M1A = 17
M1B = 18
M2A = 27
M2B = 22

pi.set_mode(M1A, pigpio.OUTPUT)
pi.set_mode(M1B, pigpio.OUTPUT)
pi.set_mode(M2A, pigpio.OUTPUT)
pi.set_mode(M2B, pigpio.OUTPUT)


def motor_speed(speed_left, speed_right):
    if speed_left > 0:
        pi.set_PWM_dutycycle(M2A, speed_left)
        pi.set_PWM_dutycycle(M2B, 0)
    else:
        pi.set_PWM_dutycycle(M2A, 0)
        pi.set_PWM_dutycycle(M2B, abs(speed_left))

    if speed_right > 0:
        pi.set_PWM_dutycycle(M1A, speed_right)
        pi.set_PWM_dutycycle(M1B, 0)
    else:
        pi.set_PWM_dutycycle(M1A, 0)
        pi.set_PWM_dutycycle(M1B, abs(speed_right))


motor_speed(0, 0)


class TextPrint(object):
    def __init__(self):
        self.reset()
        self.font = pygame.font.Font(None, 20)

    def tprint(self, screen, text):
        bm = self.font.render(text, True, BLACK)
        screen.blit(bm, (self.x, self.y))
        self.y += self.line_height

    def reset(self):
        self.x = 10
        self.y = 10
        self.line_height = 15


WHITE = pygame.Color("white")
BLACK = pygame.Color("black")

pygame.init()
screen = pygame.display.set_mode((640, 600))
pygame.display.set_caption(f"tank: {getenv('PIGPIO_ADDR')}")
screen.fill(WHITE)
pygame.display.flip()

done = False


def play_video():
    while not done:
        cap = cv2.VideoCapture(f"http://{getenv('PIGPIO_ADDR')}:8000/stream.mjpg")
        try:
            while not done:
                ret, frame = cap.read()
                if ret:
                    frame = rot90(frame)
                    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                    sf = pygame.surfarray.make_surface(frame)
                    screen.blit(sf, (0, 100))
                    pygame.display.update((0, 100, 640, 580))
        finally:
            cap.release()


threading.Thread(target=play_video, daemon=True).start()


def create_debug_funcs():
    q = queue.Queue()
    tp = TextPrint()

    def p(text):
        q.put(text)

    def r():
        while True:
            val = q.get()
            if val is None:
                break
            tp.reset()
            tp.tprint(screen, val)
            pygame.display.update((0, 0, 640, 100))

    def c():
        q.put(None)

    return p, r, c


debug, render, stop_debug = create_debug_funcs()
threading.Thread(target=render, daemon=True).start()

joysticks = [pygame.joystick.Joystick(i) for i in range(pygame.joystick.get_count())]
clock = pygame.time.Clock()
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
            stop_debug()

    screen.fill(WHITE, (0, 0, 640, 100))
    for js in joysticks:
        # ジョイスティックの値は -1 から 1 まで。 0 がセンター。 -1 が上。
        # 軸番号はおそらく 1 が左ジョイスティックの Y、 2 が右ジョイスティックのY
        v = (js.get_axis(1), js.get_axis(2))
        debug(f"{v}")
        motor_speed(int(-255 * v[0]), int(-255 * v[1]))

    clock.tick(60)

pygame.quit()
