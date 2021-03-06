import pygame


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
screen = pygame.display.set_mode((500, 700))
pygame.display.set_caption("gamepad")
screen.fill(WHITE)
pygame.display.flip()

done = False

tp = TextPrint()
clock = pygame.time.Clock()
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    tp.reset()
    screen.fill(WHITE)
    for i in range(pygame.joystick.get_count()):
        js = pygame.joystick.Joystick(i)
        for j in range(js.get_numaxes()):
            axis = js.get_axis(j)
            tp.tprint(screen, f"Joystick {i} Axis {j} value: {axis}")
        for j in range(js.get_numbuttons()):
            button = js.get_button(j)
            tp.tprint(screen, f"Joystick {i} Button {j} value: {button}")
        for j in range(js.get_numhats()):
            hat = js.get_hat(j)
            tp.tprint(screen, f"Joystick {i} hat {j} value: {hat}")
        for j in range(js.get_numballs()):
            ball = js.get_ball(j)
            tp.tprint(screen, f"Joystick {i} ball {j} value: {ball}")

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
