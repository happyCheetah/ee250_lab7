import Adafruit_GPIO.SPI as SPI
import Adafruit_MCP3008
import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)

cnt = 0;
while (cnt < 5):
    GPIO.output(17,1)
    time.sleep(0.5)
    GPIO.output(17,0)
    time.sleep(0.5)
    cnt = cnt + 1

SPI_PORT = 0
SPI_DEVICE = 0

mcp = Adafruit_MCP3008.MCP3008(spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE))

for i in range(50):
    reading = mcp.read_adc(0)
    print(reading)
    if(reading  > 450):
        print("bright")
    else:
        print("dark")
    time.sleep(0.1)

cnt = 0

while (cnt < 4):
    GPIO.output(17,1)
    time.sleep(0.2)
    GPIO.output(17,0)
    time.sleep(0.2)
    cnt = cnt + 1

for x in range(50):
    time.sleep(0.1)
    reading = mcp.read_adc(1)
    print(reading)
    if ( reading > 300 ):
        GPIO.output(17,1)
        time.sleep(0.1)
        GPIO.output(17,0)
    else:
        GPIO.output(17,0)


GPIO.cleanup()


