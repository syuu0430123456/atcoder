sx, sy, gx, gy = map(int,input().split())
sy = - sy
# a:εΎγ b:εη
a = (gy-sy)/(gx-sx)
b = gy - a*gx
x = -b/a
print(x)