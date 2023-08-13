from gpiozero import LED
from gpiozero import Button
from gpiozero.pins.pigpio import PiGPIOFactory

from board import I2C
from PIL import Image, ImageDraw, ImageFont
import adafruit_ssd1306

DEVICE_ADDR = 0x3C
DISP_WIDTH = 128
DISP_HEIGHT = 64

PIN_LED_1 = 16
PIN_LED_2 = 17
PIN_LED_3 = 18
PIN_LED_4 = 19

PIN_BTN1 = 20
PIN_BTN2 = 21
PIN_BTN3 = 22
PIN_BTN4 = 23

# OLEDの設定
oled = adafruit_ssd1306.SSD1306_I2C(DISP_WIDTH, DISP_HEIGHT, I2C(), addr=DEVICE_ADDR)
# init display
oled.fill(0)
oled.show()

# GPIO操作用クラス
factory = PiGPIOFactory()

btn1 = Button(PIN_BTN1, pull_up=False, pin_factory=factory)
btn2 = Button(PIN_BTN2, pull_up=False, pin_factory=factory)
btn3 = Button(PIN_BTN3, pull_up=False, pin_factory=factory)
btn4 = Button(PIN_BTN4, pull_up=False, pin_factory=factory)
buttons = [btn1, btn2, btn3, btn4]

ledBlue = LED(PIN_LED_1, pin_factory=factory)
ledYellow = LED(PIN_LED_2, pin_factory=factory)
ledRed = LED(PIN_LED_3, pin_factory=factory)
ledGreen = LED(PIN_LED_4, pin_factory=factory)
leds = [ledBlue, ledYellow, ledRed, ledGreen]

switch_map = dict(zip(buttons, leds))



def main():
    img = Image.new("1", (oled.width, oled.height))
    font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 10)
    # draw.text((0, 30), "Hello!", font=font, fill=255)
    oled.init_display()
    
    try:
        # GPIOの入力監視を開始
        while True:
            # OLEDに表示する画像の準備(リアルタイム)
            img = Image.new("1", (oled.width, oled.height))
            draw = ImageDraw.Draw(img)
            # トグルスイッチに対応するLEDのON, OFFを行う
            for btn, led in switch_map.items():
                if btn.is_pressed:
                    led.on()
                else:
                    led.off()
            ledStatus = ["ON" if i.is_active else "OFF" for i in leds ]
            text = "   ".join(ledStatus)
            
            draw.text((0, oled.height/2), text, font=font, fill=255)    
            oled.image(img)
            oled.show()
            
    except KeyboardInterrupt:
        print("stop")
        [led.off() for led in leds]
        # clear display
        oled.fill(0)
        oled.show()

    return

if __name__=="__main__":
    main()