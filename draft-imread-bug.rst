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

Also looks decent. This should not be surprising, in two-bit complement, ``~f``
is roughly ``-f``. Roughly, but similarly enough that, by eye, it is hard to
tell apart. The TIFF format does allow you to specify whether zero is supposed
to be white or black. Maybe PNG has a similar "feature."

I read through the libpng documentation (which is not great), a bit through its
source, and through online descriptions of PNG format. Along the way, I noticed
that converting the image to TIFF (with ImageMagick) and loading it with imread
also gave the wrong result. Perhaps the TIFF reader had the same bug or
ImageMagick [#]_.

Eventually, I realised that *PNG files are in network order* (i.e., in
big-endian format) and the code did not convert them to little-endian. Thus, my
initial intuition had been right!

Why did ``imshow(f.byteswap())`` result in a mangled image, however?

I stated to suspect that ``matplotlib`` had a bug. I tried to do::

    imshow(f.byteswap() / 2.**16)

and it resulted in the correct image.



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

