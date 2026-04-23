from os import remove

tpl = ('a','b',1,4.5,"keshav")
tpl_2 = ('x','y',10,True,"patidar")
print(tpl)
print(tpl[1])
print(tpl[1:4])
print(tpl[:3])
print(tpl[2:])
print(tpl[:])
print(len(tpl))
print(tpl.count(4.5))
print(tpl.index('keshav'))
#print(tpl_2.index(True,1))
new_tpl = tpl * 2
print(new_tpl)
tpl_3 = tpl + tpl_2
print(tpl_3)
