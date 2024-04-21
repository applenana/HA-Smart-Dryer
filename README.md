# HA-Smart-Dryer —— 接入homeassistant的智能烘干箱
## Feature特点
- 接入homeassistant，可实现与其它的设备联动控制
- 使用PTC加热和风扇增加对流，快速升温干燥
- 增加填充分子筛的开槽，透出内部的湿气，使得不再是蒸桑拿
- 外部湿气难以倒灌入箱内
- 使用esp8266作为单片机控制各种模块
- 使用dht22测量温湿度更加精准
- 模块化(才不是懒的画pcb)
## Preparation准备
如果你准备制作一个这样的烘干箱，你需要准备以下材料
| 项目        | 数量 |  价格（仅供参考） | 链接(不必相同，仅供参考)
| --------   | -----:  | :----:  | :----:  |
| PTC加热板  | 1   |   18     |  [300wPTC](https://item.taobao.com/item.htm?abbucket=20&id=563415661367&ns=1&skuId=3565575760927&spm=a21n57.1.item.4.1897523cvbE5XP)  |
| esp12f |   1   |   4.63   |  [esp12f](https://item.taobao.com/item.htm?abbucket=20&id=45081050416&ns=1&skuId=3853228016770&spm=a21n57.1.item.4.159d523cQ1aH30)  |
| esp12系列转接板  |    1    |  0.45  |  [转接板](https://item.taobao.com/item.htm?id=520221832314&spm=a1z10.3-c-s.w4002-24881783314.19.5fea546euLPdTO)  |
| 3.3v ams117稳压管 | 1 | 0.15 | [ams117](https://item.taobao.com/item.htm?id=7971982435&spm=a1z10.3-c-s.w4002-24881783314.10.1401546ez5vihc) |
| DHT22模块 | 1 | 5.5 | [DHT22](https://item.taobao.com/item.htm?id=551955065907&skuId=4811271041525&spm=a1z10.3-c-s.w4002-24881783314.16.474e546eQZNuJb) |
| 5v低电平触发继电器模块 | 2 | 2.6 | [继电器模块](https://item.taobao.com/item.htm?id=21846804090&spm=a1z10.3-c-s.w4002-24881783314.23.514a546eKgqN7a) |
| PWM脉冲频率占空比可调模块XY-LPWM | 1 | 6.3 | [PWM模块](https://item.taobao.com/item.htm?id=681446228861&spm=a1z10.3-c-s.w4002-24881783314.56.2f0b546eMika5C&skuId=5057633359537) |
| 线仔跳线焊接线导线飞线电子连接线镀锡双头PCB电路板22AWG | 100 | 6.96 | [线仔](https://detail.tmall.com/item.htm?ali_refid=a3_430582_1006:1104520036:N:3f1DeK820Ch4vDl/9bzLTgvW6uFNKReq:47e9fb801e1668e095424b92650be01b&ali_trackid=1_47e9fb801e1668e095424b92650be01b&id=15697720009&skuId=3712626350139&spm=a21n57.1.item.46) |
| 二脚插头带线 | 1 | 3.6 | [电源线](https://item.taobao.com/item.htm?abbucket=20&id=730243629516&ns=1&spm=a21n57.1.item.92.159d523cQ1aH30&skuId=5062860261490) |
| 耐高温特软硅胶线航模锂电池铜芯电线导线国标18AWG 5m | 1 | 6.9 | [软线](https://item.taobao.com/item.htm?_u=l20bv0ctvucddd&id=615789757622&spm=a1z09.2.0.0.67002e8dq1b0cy&skuId=4858829261009) |
| 8*6双面焊接洞洞板 | 1 | 3.33 | [洞洞板](https://detail.tmall.com/item.htm?_u=l20bv0ctvu6192&id=17952641393&skuId=5089150435057&spm=a1z09.2.0.0.67002e8dC8TkfS) |
| 总计 | 110 | 58.42 | 
## Help教程
待续
