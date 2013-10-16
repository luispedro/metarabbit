Why Python is Better than Matlab for Scientific Software

0. My argument only applies for new projects

If you have legacy code in MATLAB, then it may make sense to just continue
using it. If it works, don't fix it.

However, note that porting code is not the same as writing from scratch. You
can often convert code from MATLAB to Python in a small fraction of the time it
would take you to start from scratch.

1. Python has caught up with Matlab and is in the process of overtaking it.

The momentum is in the right direction.

This graph shows the number of lines of code in some important projects for
bioimage informatics. As you can see, the base projects on the top have been
stable for some years, while the more applied packages at the bottom have
exploded in recent years.

Right now, depending on what you are doing, Python may even better support it.
It is now, Matlab which is playing catch-up with open source software (for
example, the introduction of .. in Matlab is just a closed source version of 

2. It is a real programming language

Matlab is not.

This means that if you need to add some non-numerical capabilities

3. It can easily interface with other languages

Python can interfact with any language which can be interacted through C.



4. You can have a full open-source stack

This also means that you are allowed to, for example, ship a whole virtual
machine image with your paper.

5. Licensing issues are a pain. And expensive.

Note that I left the word expensive to the end, although in some contexts it
may be crucial. Besides the basic MATLAB licenses, you will often need to buy a
few more licenses for specific toolboxes. If you need to run the code on a
cluster, often that will mean more licenses.

However, even when you do have the money, this does not make the problem go
away: now you need admin for the licensing. When I was at CMU, we had
campus-wide licenses and, yet, it took a while to configure the software on
every new users computer (with some annoying minor issues like the fact that
your username needed to match the username you had on campus), you couldn't run
it outside the network (unless you set up a VPN, and it still presupposed you
had network access), &c. Every so often, the license server would go down and
stop everybody's work. These secundary costs can be as large as the licensing
costs.

Furthermore, using Python means you can more easily collaborate with people who
don't have access to Matlab. Even with a future version of yourself who decided
to economize on Matlab licenses (or if the number of users shrinks and your
institution decides to drop the campus licensing, you will not be one of the
few groups now forced to buy it out-of-pocket).

By the way, if you do want support, there are plenty of options for purchasing
it [#]_: larger companies as well as individual consultants available in any
city. The issue of support is orthogonal to the licensing of the software itself.

.. [#] However, because science is a third-world econonmy, it may be easier to
   spend 10k on Matlab licenses which come with phone support to spending 1k on
   a local Python consultant.

