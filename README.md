# cytron maker drive

[Cytron Maker Drive](https://www.cytron.io/p-maker-drive-simplifying-h-bridge-motor-driver-for-beginner), Pi Camera, [Elecom JC-U3912TBK](https://www.elecom.co.jp/products/JC-U3912TBK.html) を利用した装軌車両ラジコンのクライアントプログラムです。

参考: https://tutorial.cytron.io/2019/03/06/getting-started-maker-drive-raspberry-pi/

## 事前準備

### Raspberry Pi OS

#### pigpiod の有効化

```
$ sudo systemctl enable pigpiod
$ sudo systemctl start pigpiod
```

#### ストリーミングサーバ

1. [Pi Camera のセットアップ](https://projects.raspberrypi.org/en/projects/getting-started-with-picamera)
2. [Web streaming](https://picamera.readthedocs.io/en/latest/recipes2.html#web-streaming) のコードを `/home/pi/streaming-server/streaming_server.py` に設置
    - カメラ画像を回転させたいときは `camera.rotation = 90` などとすればよい
3. 下を `/etc/systemd/system/streaming-server.service` に設置する
    ```
    [Unit]
    Description=Streaming server
    After=network.target

    [Service]
    WorkingDirectory=/home/pi/streaming-server
    ExecStart=/usr/bin/python3 streaming-server.py
    Restart=on-failure
    User=pi
    Group=pi

    [Install]
    WantedBy=multi-user.target
    ```
4. `sudo systemctl enable streaming-server`
5. `sudo systemctl start streaming-server`

### Linux

下のコマンドで依存パッケージのインストールができる。

```
make init-venv install-dep
```

使用しているパッケージは以下なので、手動でインストールしてもよい。

- [pygame](https://www.pygame.org/wiki/GettingStarted)
- [pigpio](https://gpiozero.readthedocs.io/en/stable/remote_gpio.html#preparing-the-control-computer)
- [OpenCV on Wheels](https://github.com/skvark/opencv-python#installation-and-usage)


## 実行

Makefile の `PIGPIO_ADDR` を Raspberry Pi のIPやホスト名に変更し、下のコマンドを実行。

```
make run
```

## 各ファイルの説明

|ファイル名|説明|
|--|--|
|gamepad\_sample.py|ゲームパッドのジョイスティックから取得できる値を表示する|
|maker\_drive\_gamepad.py|Elecom JC-U3912TBKの左右のジョイスティックでモータを制御する|
|maker\_drive\_gamepad\_video.py|maker\_drive\_gamepad.pyにビデオ表示を追加したもの|
|maker\_drive.py|一定間隔ごとにモータの回転を変更する|
