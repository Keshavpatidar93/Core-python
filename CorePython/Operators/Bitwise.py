a = 60                     #0011 1100
b = 20                     #0001 0100
c = 0
c = a and b            # 0001 0100  = 20
print("a and b =>",c)
c = a or b              # 0011 1100  = 60
print("a or b =>",c)
c = a^b                 # 0010 1000
print("a ^ b =>",c)
c = a>>2               #  60/4 = 15  (1101)
print("a>>2 is =>",c)
c = a<<2               # 60 * 4 = 240
print("a<<2 is =>",c)