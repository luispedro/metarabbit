Having just spent some posts discussing a paper on nuclear segmentation, let me
ask the question:

Is cell segmentation needed?

This is a common FAQ whenever I give a talk on my work which does not use
segmentation, for example, using local features for classification.

Here is my answer:

Remember Vapnik's dictum [#]_: *do not solve, as an step problem, a harder
problem than the problem you really need to solve.*

Thus the question becomes: *is your scientific problem dependent on cell
segmentation?* In the case, for example, of subcellular location determination,
it is not: all the cells in the same field display the same phenotype, your
goal being the find out what it is.


.. [#] I'm quoting from memory. It may a bit off. It sounds obvious when you
   put it this way, but it is still often not respected in practice.

