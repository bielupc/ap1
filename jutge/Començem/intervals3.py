from yogi import read

start1 = read(int)
end1 = read(int)

start2 = read(int)
end2 = read(int)


 
if start1 == start2 and end1 == end2:
    print(f"= , [{start1},{end1}]")

elif start2 <= start1 and end2 >= end1:
    print(f"1 , [{start1},{end1}]")

elif start1 <= start2 and end1 >= end2:
    print(f"2 , [{start2},{end2}]")
else:
    if start2 <= end1 and start1 < end2 or start1 <= end2 and start2 < end1:
        print(f"? , [{max(start1, start2)},{min(end1, end2)}]")

    else:
        print("? , []")
