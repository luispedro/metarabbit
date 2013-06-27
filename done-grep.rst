Public Service Announcement

If you have ever done this::

    grep -c '^>' big_file.fa | wc -l

or (even better because ``grep`` can count)::

    grep -c '^>' big_file.fa

Consider whether you should be doing::

    LC_ALL=C grep -c '^>' big_file.fa

§

Here are measurements on my computer::

    $ du -sh big_file.fa
    1.3G    big_file.fa

It's a large, but not absurdly large, file.

::

    $ time cat big_file.fa >/dev/null
    cat big_file.fa > /dev/null  0.01s user 2.04s system 99% cpu 2.056 total

Reading it from disk takes about two seconds (this is a network mounted share).

::
    time grep -c '^>' big_file.fa
    8310416
    grep -c '^>' big_file.fa  8042.37s user 14.15s system 98% cpu 2:15:43.41 total

Grepping it takes over **two hours**! CPU usage was 98% through the whole
process (the machine was doing a few other things, but nothing special).

Grepping it in the ``C`` locale takes about three seconds::

    $ time LC_ALL=C grep -c '^>' big_file.fa
    8310416
    LC_ALL=C grep -c '^>' big_file.fa  1.73s user 1.14s system 99% cpu 2.868 total

So in the ``C`` locale, ``grep`` took less than one second more when compared
to just reading the file from the network disk.

§

In my case, this was in the middle of a script and it was just computing some
statistics. Mapping these same reads to the human genome takes just over two
minutes (admitedly, we use 8 cores for that, but that comes out at ca twenty
minutes if we had just used one core).

I believe this is a common occurence in sequence based computing pipelines: the
mapping step is actually very fast. Then, a small performance bug here or there
makes the whole thing take much more than it should.

§

If you're wondering why grep is so bad outside the ``C`` locale:

By default, on my system (check yours), the UTF-8 locale is used. UTF-8 is a
wonderful thing, but grep is slow in handling it and we do not need it here.

More information `on 503 Service Unavailable
<http://rg03.wordpress.com/2009/09/09/gnu-grep-is-slow-on-utf-8/>`__

