I while back, I got a bug report for mahotas-imread [#]_:


The first thing I noticed was that this was a 16 bit image. If you've been
coding for as long as I have, you'll immediately think: It's a byte-endiness
issue [#]_. So, I tested::

    imshow(im.byteswap())

and saw the following:

.. image:: byteswap0.png

Not good. The I looked at the hint that the original poster provided and
it did seem to be true: ``imshow(~f)`` worked reasonably well. My working
hypothesis was thus that there is a flag whereby the PNG data needs to be
interpreted after a bit reversion. I also noticed another thing, though::

    max_16bit_value = 2**16-1
    imshow(max_16bit_value - f)

Also looks decent.

The TIFF format does allow you to specify whether zero is supposed
to be white or black. Maybe PNG has a similar "feature."

I read through the libpng documentation (which is not great), a bit through its
source, and through online descriptions of PNG format. Along the way, I noticed
that converting the image to TIFF (with ImageMagick) and loading it with imread
also gave the wrong result. Perhaps the TIFF reader had the same bug or
ImageMagick [#]_.

Eventually, I realised that *PNG files are in network order* (i.e., in
big-endian format) and the code did not convert them to little-endian. Thus, my
initial intuition had been right!

But in this case, why did ``imshow(f.byteswap())`` result in a mangled image?

I stated to suspect that ``matplotlib`` had a bug. I tried to do::

    imshow(f.byteswap() / 2.**16)

and it resulted in the correct image.

As it turned out, `matplotlib does not do the right thing when given 16 bit
files <https://github.com/matplotlib/matplotlib/issues/2499>`__.

A single bug is often easy to debug, but when you have multiple bugs interacting; the complexity.

§

**Hairy details:** You may want to stop reading now.

Consider the following identities::

    255 == 0xff
    -f == (f ^ 0xff + 1)
    2**16 - f = -f + 2**16 == -f (because of overflow)

Thus, it should not be surprising that flipping the bits or subtracting the
image resulted int , in two-bit complement, ``~f`` is roughly ``-f``.  Not
exactly, but similarly enough that, by eye, it is hard to tell apart.

Finally, it all makes sense when you realise that matplotlib assumes that non-8
bit images are floating point and does::

    final_image = (input_image * 255)
    final_image = final_image.astype(np.uint8)

Because what is multiplying by 255? It's the same as multiplying by -1! Thus,
matplotlib would multiply by -1 and then take the low order bits. Th

.. [#] People don't always appreciate how valuable good bug reports are.
   Seriously, they are a huge help: you are testing the software for me.
   Unfortunately, either shyness or past bad experiences will often cause
   people who see something worng to not report it.

.. [#] I now have over 15 years of experience coding (having had a relative
   late start [I didn't care much about computers until I was close to college
   age], I've caught up.) If there is an area where I really feel that my
   experience shines through is debugging: I've seen enough mistakes and errors
   that my guesses as to what the bug is are more and more accurate (this is
   true even in code I have not seen).

.. [#] One of the reasons I started mahotas-imread was that I had not found a
   single library that could read the formats I wanted without a lot of bugs.
   So, I trust no one on this. In this case, the paranoia was unwarranted, as
   we'll see.

