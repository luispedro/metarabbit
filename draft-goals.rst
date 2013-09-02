I basically have a similar view to Titus' view. I will also write a post by
playing rationalists taboo with the word reproducibility and recomputation.

**The ability to regenerate the results by starting from a known state of the
world is, by itself, not very useful**

Let's say I have the following software (which is not even that hard to do): It
starts a standard VM with stock Ubuntu and I log in. Then, everything I type in
plus everything that was gotten from the web is logged as a script. If I do all
my work in that environment, then I get perfect reproduction: just reran the
same input to the virtual machine and you will get a virtual machine that has
the final state of the world.

What you get is the possibility to perform archeology on the computation.

What I think are important goals are the following:

**The code should be correct**

Every once in a while, someone comments *who cares about unit tests and all
that as long as the code works? It's just a waste of time.*

This is perfectly true, of course, except that it ignores that **humans are falible**.

Why have controls in an experiment (using up valuable wells in a plate or lanes
on a gel) as long as the experiment is performed correctly? Why show the
intermediate steps in a proof as long as you get a theorem that is true? Why
have a safety net as long as you do not fall?

*Because humans are falliable and science is hard*. Things that are wasteful in
the perfect case provide safety in the imperfect world.

This leads to a few sub-goals:

1. It should be possible to inspect the whole pipeline.
2. It should be possible to execute all steps from a clean state to avoid reuse
   of stale results.

If I had perfect memory, I would never worry about reusing stale results or
getting my software versions confused. If I never made coding mistakes, then
there would be less reasons for me to open source my code.

We tend to discuss these matters as if incentives did not matter (or, as Tyler
Cowen would put it, without solving for the equilibrium), but it is not that we
want people to do X and then open source it. By requiring open source, we make
them do X differently.

**Others should be able to avoid rewriting the same code**

This is actually very different. 


