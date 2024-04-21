import time
from machine import Pin,Timer
from wifi import connect
import json
from umqtt.simple import MQTTClient
from dht20 import get_data
from file import exist
from sparkfuc import spark
from fan import fan_duty

wifi_name = ""#填写wifi名
wifi_key = ""#填写wifi密码
mqtt_broker = ""#mqtt服务器地址

connect(wifi_name,wifi_key)

light = Pin(12,Pin.OUT)#开口左边
switch = Pin(5,Pin.OUT)#开口右边

switch.value(0)
light.value(1)
#初始化，关闭所有继电器

did = deviceID = "smartdrier"
mqtt_port = 1883
mqtt_user = "iotdrier"
mqtt_password = "drier123"
client_id = did + "123"
keepalive= 60

global data
if not exist("data.json"):
    with open("data.json","w",encoding="utf-8") as f:
        data = {'mode':'auto','fanMode':'auto','targetTem':24,'nowTem':24,'nowHum':50}
        json.dump(data,f)
else:
    with open("data.json","r",encoding="utf-8") as f:
        data = json.load(f)    

def callback(topic, msg):
    global data
    #print(topic.decode(),msg.decode())
    topic = topic.decode()
    msg = msg.decode()
    
    if topic == did+'/mc':
        data['mode'] = msg
        print(f'调整模式[{msg}]')
    elif topic == did+'/fc':
        data['fanMode'] = msg
        print(f'调整风扇挡位[{msg}]')
    elif topic == did+'/tc':
        data['targetTem'] = float(msg)
        print(f'调整目标温度[{msg}]')
    
    if topic in [did+'/'+i for i in ['mc','fc','tc']]:
        spark()
        client.publish(did+'/ms',data['mode'])
        client.publish(did+"/fs",data['fanMode'])
        client.publish(did+"/ts",str(data['targetTem']))
        with open("data.json","w",encoding="utf-8") as f:
            json.dump(data,f)
        print("写入数据")
    
    
# 连接到 MQTT 服务器
client = MQTTClient(client_id, mqtt_broker, mqtt_port, mqtt_user, mqtt_password,keepalive=keepalive)
client.set_callback(callback)
client.connect()

# 订阅主题
client.subscribe(did+"/mc")
client.subscribe(did+"/fc")
client.subscribe(did+"/tc")

client.publish(did+'/ms',data['mode'])
client.publish(did+"/fs",data['fanMode'])
client.publish(did+"/ts",str(data['targetTem']))

def timer_func():
    global data
    try:
        dhtdata = get_data()
        data['nowTem'] = tem = dhtdata[0]
        data['nowHum'] = hum = dhtdata[1]
    except Exception as e:
        print(f'发生错误{e}')
        tem = data['nowTem']
        hum = data['nowHum']
    
    if data['mode'] != 'off':
        if data['mode'] == 'heat':
            print('持续加热')
            switch.value(1)
        elif data['mode'] == 'auto':
            print('自动模式')
            if data['targetTem'] > tem:
                switch.value(1)
            else:
                switch.value(0)
        
        if data['fanMode'] == 'auto':
            if data['targetTem'] - tem >= 10:
                fan_duty(100)
            elif data['targetTem'] - tem >= 5:
                fan_duty(50)
            else:
                fan_duty(10)
        elif data['fanMode'] == 'high':fan_duty(500)
        elif data['fanMode'] == 'medium':fan_duty(250)
        elif data['fanMode'] == 'low':fan_duty(0)
            
    else:
        fan_duty(0)
        switch.value(0)
        print('关闭所有电器')
timer = Timer(-1)
timer.init(period=5000, mode=Timer.PERIODIC, callback=timer_func)   

print("进入mqtt循环")
count = 0
while True:
    try:
        count += 1
        client.wait_msg()
                        
    except Exception as e:
        if str(e) != '-1':
            if not exist("err.log"):
                with open("err.log","w",encoding="utf-8") as f:
                    f.write(str(e)+"\n---\n")
            else:
                with open("err.log","a",encoding="utf-8") as f:
                    f.write(str(e)+"\n---\n")
            client.publish(did+"/err",str(e))
            print(f"发生错误{e}")
        else:
            print(f"-被动心跳执行-{time.localtime()[3]}:{time.localtime()[4]}:{time.localtime()[5]}-")
        
        if str(e) == '[Errno 103] ECONNABORTED':
            print(f"网络断开……尝试重连")
            connect(wifi_name , wifi_key)
            client.connect()
        else:
            client.disconnect()
            client.connect()

        # 订阅主题
        client.subscribe(did+"/mc")
        client.subscribe(did+"/fc")
        client.subscribe(did+"/tc")
        client.subscribe("smartsensor/t")
        client.subscribe("smartsensor/h")
