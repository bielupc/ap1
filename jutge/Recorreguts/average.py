from yogi import tokens


len = 0.0
avg = 0.0

for n in tokens(float):
    len += 1.0
    avg += n

print("{:.2f}".format(avg / len))




