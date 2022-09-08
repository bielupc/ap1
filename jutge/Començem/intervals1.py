from yogi import read

a1 = read(int)
b1 = read(int) 

a2 = read(int)
b2 = read(int)

if b1 > a2 or b2 > a1:
   print("[]")

elif a2 < b1:
    print(f"[{b1},{a2}]")
    
    
