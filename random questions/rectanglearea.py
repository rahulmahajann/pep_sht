ax1 = -2
ay1 = -2
ax2 = 2
ay2 = 2
bx1 = 3
by1 = 3
bx2 = 4
by2 = 4

cx1=max(ax1,bx1)
cx2=min(ax2,bx2)
cy1=max(ay1,by1)
cy2=min(ay2,by2)

# print(cx1,cx2,cy1,cy2)

new_x=cx2-cx1
new_y=cy2-cy1

print(new_x,new_y)

new_x=max(0,cx2-cx1)
new_y=max(0,cy2-cy1)

a_x=abs(ax2-ax1)
a_y=abs(ay2-ay1)

b_y=abs(by2-by1)
b_x=abs(bx2-bx1)

print((a_x*a_y)+(b_x*b_y)-(new_x*new_y))
print(new_x*new_y)