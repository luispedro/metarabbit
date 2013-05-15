The Folk Theorem of Statistical Computing

Andrew Gelman calls this the `folk theorem of statistical computing
<http://andrewgelman.com/2008/05/13/the_folk_theore/>`__:

    When you have computational problems, often there’s a problem with your
    model.

(This is not a folk theorem per se, as it is not a theorem; but the name stuck.[#]_)

There is an interesting corollary:

    When you are performing parameter selection using cross-validation or a
    similar blind procedure, **the bad parameter choices take longer than the
    good ones**!

This reminds me of the advertising quip (typically attributed to `John
Wanamaker <http://www.quotationspage.com/quotes/John_Wanamaker/>`__) that *Half
the money I spend on advertising is wasted; the trouble is I don't know which
half*, except it is even worse: **most** of my computation is wasted; the
trouble is I don't know which bits.

Of course, you can reply: *if I knew the right parameters, then you would not
need to find them in the first place*. Still, understanding that your
computation is most wasted in the really bad cases can be actionable.

Here is an example from machine learning: if you are using a support vector
machine based system, you will often need to fit two parameters:

1. The SVM penalty $C$.
2. The kernel parameter (in the case of radial basis functions, the width
   $\sigma$).

A simple solution is to try a grid of these parameters::

    for c in [2**(-2), 2**(-1), 2**0,...]:
        for s in [2**(-2), 2**(-1), 2**0,...]:
            use cross validation to evaluate using c & s
    pick best one

There is a fair share of wasted computation. For example, let's say you have a
parameter choice that is so awful it gives you 100% error rate and another
which is so good it gives you 0% error. If you are lucky and you check the good
combination first, you can abort the bad parameter choices early: the first
time you see an error, you know it will never be as good.

This leads to the following algorithm::

    error = { param -> 0 for all parameters }
    forever:
        next_param = parameter with less error which has not run all folds
        run crossvalidation fold on next_param
        error[next_param] += error on this fold

        if error[ best_completed_parameter_value ] is minimum error:
            return best_completed_parameter_value

This aborts as early as possible with the best error.

This is implemented in my `machine learning package
<http://luispedro.org/software/milk>`__ (`github link
<http://github.com/luispedro/milk`__) by default.

Testing it on ``murphylab_slf7dna`` (with a bit of hacking of the internals to
print statistics), we see that this algorithm only runs 57% of cross validation
loops. Because the bad parameter choices are slower, we get an extra speed-up
and it only takes 49% of the time of running all the iterations.

.. [#] A really interesting question is whether you can formalise and prove it.
   A good model will often be one that has a nice little "fitness" peak, which
   is also easy to fit. Likelihood functions with local optima all over the
   place or ill-conditioned may correspond to worse models.

