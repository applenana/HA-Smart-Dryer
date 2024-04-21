from machine import Pin
from dht import DHT22 as dht
import time

dht22 = dht(Pin(14))

def get_data():
    dht22.measure()
    return (dht22.temperature(),dht22.humidity())

print(get_data())