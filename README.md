# cytron maker drive

https://www.cytron.io/p-maker-drive-simplifying-h-bridge-motor-driver-for-beginner

参考: https://tutorial.cytron.io/2019/03/06/getting-started-maker-drive-raspberry-pi/

## 事前準備

### Raspberry Pi OS

```
$ sudo systemctl enable pigpiod
$ sudo systemctl start pigpiod
```

### Linux

- [pygame](https://www.pygame.org/wiki/GettingStarted)
- [pigpio](https://gpiozero.readthedocs.io/en/stable/remote_gpio.html#preparing-the-control-computer)
- [OpenCV on Wheels](https://github.com/skvark/opencv-python#installation-and-usage)

## 実行

```
PIGPIO_ADDR="<RASPBERRY_PI_IP_ADDRESS>" python3 maker_drive_gamepad.py
```
