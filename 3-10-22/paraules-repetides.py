from yogi import *

par1 = scan(str)
repes = 0

if par1 is not None:
  par2 = scan(str)
  while par2 is not None:
    if par1 == par2:
      repes += 1
    par1 = par2
    par2 = scan(str)
print(repes)


