import pigpio
from time import sleep

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

# 前進
motor_speed(200, 200)
sleep(1)
motor_speed(0, 0)
sleep(0.5)
# 後退
motor_speed(-100, -100)
sleep(1)
motor_speed(0, 0)
sleep(0.5)
# 左旋回
motor_speed(0, 100)
sleep(1)
motor_speed(0, 0)
sleep(0.5)
# 右旋回
motor_speed(100, 0)
sleep(1)
motor_speed(0, 0)
sleep(0.5)
# 超信地旋回
motor_speed(100, -100)
sleep(1)
motor_speed(0, 0)
sleep(0.5)
# 超信地旋回
motor_speed(-100, 100)
sleep(1)
motor_speed(0, 0)
sleep(0.5)
