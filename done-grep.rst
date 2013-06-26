Public Service Announcement

If you have ever done this::

    grep -c '^>' Large_file.fa | wc -l

or (even better because ``grep`` can count)::

    grep -c '^>' Large_file.fa

Consider whether you should be doing::

    LC_ALL=C grep -c '^>' Large_file.fa

§

Here are measurements on my computer::

    $ du -sh $big_file
    1.3G    $big_file

It's a large, but not absurdly large, file (I've masked the filename as it is
not relevant).

::
    $ time cat $big_file >/dev/null
    cat $big_file > /dev/null  0.00s user 1.73s system 99% cpu 1.736 total

Reading it from disk takes about two seconds.

::

Grepping it takes ! CPU usage was 100% through the whole process.

Grepping it in the ``C`` locale takes about two seconds::



§

This is because by default, on my system (check yours), the UTF-8 locale is
used. UTF-8 is a wonderful thing, but grep is slow in handling it and we do not
need it here.

More information `on 503 Service Unavailable
<http://rg03.wordpress.com/2009/09/09/gnu-grep-is-slow-on-utf-8/>`__

