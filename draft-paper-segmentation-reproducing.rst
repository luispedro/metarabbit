In the last post, I described my nuclear segmentation paper.

It has a `reproducible research archive
<https://github.com/luispedro/segmentation>`__.

§

If you now download that code, **that is not the code that was used for the
paper**!

In fact, the version that generates the tables in the paper does not run
anymore, because it only runs with old versions of numpy! [#]_ In order for it
to compute the computation in the paper, I had to update the code.

.. [#] The issue is the changed semantics of the histogram function.

