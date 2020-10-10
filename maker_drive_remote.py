from pynput.keyboard import KeyCode, Listener
import pigpio

pi1 = pigpio.pi()
pi2 = pigpio.pi()

M1A = 17
M1B = 18
M2A = 27
M2B = 22

pi1.set_mode(M1A, pigpio.OUTPUT)
pi1.set_mode(M1B, pigpio.OUTPUT)
pi2.set_mode(M2A, pigpio.OUTPUT)
pi2.set_mode(M2B, pigpio.OUTPUT)


def motor_speed(speed_left, speed_right):
    if speed_left > 0:
        pi2.set_PWM_dutycycle(M2A, speed_left)
        pi2.set_PWM_dutycycle(M2B, 0)
    else:
        pi2.set_PWM_dutycycle(M2B, abs(speed_left))
        pi2.set_PWM_dutycycle(M2A, 0)

    if speed_right > 0:
        pi1.set_PWM_dutycycle(M1A, speed_right)
        pi1.set_PWM_dutycycle(M1B, 0)
    else:
        pi1.set_PWM_dutycycle(M1B, abs(speed_right))
        pi1.set_PWM_dutycycle(M1A, 0)


motor_speed(0, 0)

speed = 200


def on_press(key):
    if type(key) is KeyCode:
        k = key.char
        if k == "f":
            pi2.set_PWM_dutycycle(M2B, 0)
            pi2.set_PWM_dutycycle(M2A, speed)
        elif k == "d":
            pi2.set_PWM_dutycycle(M2A, 0)
            pi2.set_PWM_dutycycle(M2B, speed)
        elif k == "j":
            pi1.set_PWM_dutycycle(M1B, 0)
            pi1.set_PWM_dutycycle(M1A, speed)
        elif k == "k":
            pi1.set_PWM_dutycycle(M1A, 0)
            pi1.set_PWM_dutycycle(M1B, speed)


def on_release(key):
    if type(key) is KeyCode:
        k = key.char
        if k == "f":
            pi2.set_PWM_dutycycle(M2A, 0)
            pi2.set_PWM_dutycycle(M2B, 0)
        elif k == "d":
            pi2.set_PWM_dutycycle(M2B, 0)
            pi2.set_PWM_dutycycle(M2A, 0)
        elif k == "j":
            pi1.set_PWM_dutycycle(M1A, 0)
            pi1.set_PWM_dutycycle(M1B, 0)
        elif k == "k":
            pi1.set_PWM_dutycycle(M1B, 0)
            pi1.set_PWM_dutycycle(M1A, 0)
        elif k == "s":
            motor_speed(0, 0)


with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
