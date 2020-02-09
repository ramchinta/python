class point:
    def __init__(self,x,y):
        self.x = x
        self.y = y

def overlap(l1,r1,l2,r2):
    if (l1.x > r1.x  or l2.x > r2.x):
        return False
    if (l1.y < r2.y or l2.y < r2.y):
        return False
    return True

l1 = point(0,10)
r1 = point(10,0)
l2 = point(5,5)
r2 = point(15,0)
if overlap(l1,r1,l2,r2):
    print('Rectangles overlap')
else:
    print('Rectangles do not overlap')