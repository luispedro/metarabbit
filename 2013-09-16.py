import numpy as np
import mahotas as mh
canvas = np.zeros((384,256),np.uint8)
for y in xrange(512):
    for x in xrange(512):
        if (x-128)**2+1.8*(y-64)**2 <  61*64:
            canvas[y,x] = 4
        if (x-128)**2+1.8*(y-64)**2 <  61*60:
            canvas[y,x] = 1
        if (x-128)**2+1.8*(y-192)**2 <  61*64:
            canvas[y,x] = 2
        if (x-128)**2+1.8*(y-320)**2 <  61*60:
            canvas[y,x] = 3

for y in xrange(-21,21):
    for x in xrange(-21,21):
        if x**2 + y**2 < 14*14:
            canvas[332+y,62+x] = 3

r,g,b = (canvas == 1), (canvas == 2), (canvas == 3)
mh.imsave('2013-09-16.png',mh.as_rgb(r,g,b))
