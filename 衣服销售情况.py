
"""
完成衣服销售数据的统计和分析
计算总销售额
计算平均每日销售数量
计算每个种类月销售量占比
上传代码到云端仓库，并把仓库地址发到组长，组长统一一下发到群里
"""
"""日期	服装名称	价格/件	库存数量	销售量/每日
1号	羽绒服	253.6	500	10
2号	牛仔裤	86.3	600	60
3号	风衣	96.8	335	43
4号	皮草	135.9	855	63
5号	T血	65.8	632	63
6号	衬衫	49.3	562	120
7号	牛仔裤	86.3	600	72
8号	羽绒服	253.6	500	69
9号	牛仔裤	86.3	600	35
10号	羽绒服	253.6	500	140
11号	牛仔裤	86.3	600	90
12号	皮草	135.9	855	24
13号	T血	65.8	632	45
14号	风衣	96.8	335	25
15号	牛仔裤	86.3	600	60
16号	T血	65.8	632	129
17号	羽绒服	253.6	500	10
18号	风衣	96.8	335	43
19号	T血	65.8	632	63
20号	牛仔裤	86.3	600	60
21号	皮草	135.9	855	63
22号	风衣	96.8	335	60
23号	T血	65.8	632	58
24号	牛仔裤	86.3	600	140
25号	T血	65.8	632	48
26号	风衣	96.8	335	43
27号	皮草	135.9	855	57
28号	羽绒服	253.6	500	10
29号	T血	65.8	632	63
30号	风衣	96.8	335	78
"""

print ("总销售额：",(253.6*239+135.9*207+86.3*517+96.8*292+65.8*469+49.3*120))
print("平均每日销售数量：",(140+90+24+45+25+60+129+10+43+63+10+60+63+60+58+140+48+43+57+10+63+60+78+43+63+63+120+72+69+35)/30)
print("羽绒服月销售量占比：",(140+30+69)/1844)
print("皮草月销售量占比:",(24+63+57+63)/1844)
print("牛仔裤月销售量占比:",(90+120+140+60+72+35)/1844)
print("风衣月销售量占比:",(25+43+60+43+78+43)/1844)
print("衬衫月销售量占比:",(120/1844))
print("T恤月销售量占比：",(45+129+63+58+48+63+63)/1844)