# Environment
* Raspberry Pi 4 model B
	* Raspberry Pi OS <br>
	[ Linux raspberrypi 6.1.21-v8+ #1642 SMP PREEMPT Mon Apr  3 17:24:16 BST 2023 aarch64 GNU/Linux ]
* SSD-1306 (OLED Display)
* Python3.9.2 (Default installed)


---
# Setup
### 1. For OLED with I2C connection [^1]
<b>1.1 Enable Raspberry Pi I2C interface.</b><br>

Open terminal and type below<br>
```$ sudo raspi-config```<br>
[ 3 Interface Options ] -> [ P5 I2C ] -> ["はい" (or "Yes")]<br>
-> [ "了解" ] -> [ Finish ]

<b>1.2 Make Python-venv and Install Modules.</b>

Open terminal and type below<br>
```$ python3 -m venv venv```<br>
```$ source venv/bin/activate```<br>
```(venv) $ pip install adafruit-circuitpython-ssd1306```<br>
```(venv) $ pip install smbus2 pillow```<br>

### 2. For LED controll [^2]
<b>2.1 Install Raspberry Pi Library and Enable it.</b><br>
```(venv) $ sudo apt install pigpio```<br>
```(venv) $ sudo service pigpio start```<br>
```(venv) $ systemctl enable pigpiod.service```

<b>2.2 Install modules</b><br>
```(venv) $ pip install pigpio```<br>
```(venv) $ pip install gpiozero```<br>

# Start Program
```(venv) $ python main.py```

---
[^1]: ラズパイを使って、OLED表示デバイスに文字列や画像を表示するよ
https://zenn.dev/kotaproj/articles/6f08ea43cd4dda8e0d2f#%E7%94%BB%E5%83%8F%E3%82%92%E4%BD%9C%E6%88%90%E3%81%97%E3%81%A6%E6%8F%8F%E7%94%BB

[^2]:Lチカ（LEDをチカチカさせる）
https://zenn.dev/kotaproj/books/raspberrypi-tips/viewer/010_kiso_lchika
