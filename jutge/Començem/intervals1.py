from yogi import read

start1 = read(int)
end1 = read(int) 

start2 = read(int)
end2 = read(int)


if start2 <= end1 and start1 < end2 or start1 <= end2 and start2 < end1:
    print(f"[{max(start1, start2)},{min(end1, end2)}]")

else:
    print("[]")
