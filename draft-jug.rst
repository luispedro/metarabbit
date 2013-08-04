This week-ended, I added new functionality to `jug
<http://luispedro.org/software/jug>`__ (`previous related posts
<http://metarabbit.wordpress.com/tag/python-jug>`__). Jug can now output the
final result of a computation **including metadata on all the intermediate
inputs**!

For example::

    from jug import TaskGenerator
    from jug.io import write_metadata # <---- THIS IS THE NEW STUFF

    @TaskGenerator
    def double(x):
        return 2*x

    x = double(2)
    x2 = double(x)

    write_metadata(x2, 'x2.meta.yaml')


When you execute this script (with ``jug execute``), the ``write_metadata``
function will **write a YAML description of the computation to the file**
``x.meta.yaml``!

This file will look like this::

    args:
    - args: [2]
      meta: {completed: 'Sat Aug  3 18:31:42 2013', computed: true}
      name: jugfile.double
    meta: {completed: 'Sat Aug  3 18:31:42 2013', computed: true}
    name: jugfile.double

It tells you that a computation named ``jugfile.double`` was computated at
18h31 on Saturday August 3. It also gives the same information recursively for
all intermediate results.

