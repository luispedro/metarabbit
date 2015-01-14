Technical Cantilever or Why The Term "Technical Debt" is Misleading

In tech circles, "technical debt" is a common expression of the idea that problems with

However, this is not a very good metaphor. Instead I propose the term
"technical cantilever".



**Debt cannot be left alone, while computer systems can.** Debt always grows
bigger even if you ignore it. However, computer systems can often be ignored
for a long time, even years, if the environment is stable enough and you do not
wish to extend them. I can set up a server with a simple website, and if I do
not need to make any changes, then I can leave the site running for years
without touching it.

In some cases, the system is so hairy that one would ideally wish to extend it,
but does not do it because it is too hard. In those cases, yes, you are "paying
interest" of a kind. However, there are also cases where you can simply live
with a system that works well for many years without touching anything.

As in a physical cantilever, the concept of a technical one, implies that **you
can extend your existing system to amazing lengths, but it can also break
suddenly**. That is, you can often extend it by bits and pieces very far away
from where the original anchor is. This is what makes physical Cantilevers so
breath-taking: they seem to be impossible by our intuitive physics. However,
they have a limit, so that you can extend them by large lengths and then you
try just a little bit more and the whole building starts collapsing.

§

When writing code, I also often feel a difference between "foundational code",
which ends up in a library, solving generic problems, gets unit tests and heavy
documentation, and is generally pretty solid; versus the "application code"
which is normally messier and more specific to the problem at hand.



