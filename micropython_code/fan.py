from machine import UART,Pin

uart = UART(0, 9600, tx=Pin(15), rx=Pin(13))

def fan_duty(i):
    if i < 10:text = f"00{i}"
    elif i < 100:text = f"0{i}"
    else:text = "100"
    uart.write(str(f"D{text}").encode())

fan_duty(0)
