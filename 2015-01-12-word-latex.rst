Plos One published `an awful paper
<http://www.plosone.org/article/comments/info%3Adoi%2F10.1371%2Fjournal.pone.0115069>`__
comparing Word vs LaTeX where the task was to copy down a piece of text.
Because Word users did better than LaTeX users at this task, the authors
conclude that Word is more efficient.

First of all, this fits perfectly with my experience: Word [#]_ is faster for
single page documents, where I don't care about precise formatting, such as a
letter. It says nothing about how it performs on large documents which are
edited over months (or years). The typical Word failure mode are "you paste
some text here and your image placement is now screwed up seven pages down" or
"how do I copy & paste between these two documents without messing up the
formatting?"

Of course, the authors are not happy with the conclusion that Word is better
for copying down a short piece of predefined text and instead generalize to
"that even experienced LaTeX users may suffer a loss in productivity when LaTeX
is used, relative to other document preparation systems." This is a general
failure mode of psychological research: here is a simple, well-defined
experimental result in a very artificial setting. Now, let me completely
overgeneralize to the real world (the authors of the paper use this `in their
defense <http://www.plosone.org/annotation/listThread.action?root=85170>`__:
"We understand that people who are not familiar with the experimental methods
of psychology (and usability testing) are surprised about our decision to use
predefined texts."

§

Now, why waste time bashing a Plos One paper in usability research?

Because one interesting aspect of the discussion is that several people have
pointed out that Word is better for collaboration because of the Track Changes
features. On the other hand, one of the large advantages of LaTeX is that you
can use version control on the files. With some text wrangling, you can easily
compare the text written today with a version from two months ago, it makes it
easier to have multiple people working, &c. Track Changes is still "pass the
baton" collaboration, whereby you email stuff around and say "now it's your
turn to edit it" [#]_.

However, this is only valid if you know how to use version control. In that
case, it's clear that using a text-based format is a good idea and it makes
collaboration easier. The same way, I actually think that some of the problems
that people had with LaTeX in the paper had to do with not using a
spell-checker on their editor.

The underlying concept is that LaTeX works in an ecosystem of tools working
together, which is a concept that we do not, in general, teach people. I have
been involved with `Software Carpentry <http://software-carpentry.org/>`__ and
even before that I was `trying to get to people who are not trained in
computers <http://luispedro.org/projects/pfs/>`__, but we do not do that great
of a job at teaching this concept as it is abstract and not directly clear to
students why it is useful.

Spending a few hours going through the basic Unix commands seems like
brain-dead activity when people cannot connect this to their other knowledge.
On the other hand, it is very frustrating when somebody comes to me with a
problem they have been struggling with for days and in a minute, I can give
them a solution. Then they ask "how could I learn that?" and I just don't have
an answer.

§

Finally, let me just remark that LaTeX is a particularly crappy piece of
software. It is so incredibly bad that it only survives because the
alternatives manage to be even worse. It's even sadder when you realise that
`LaTeX is now over 30 years old, while Word is an imitation of even older
technology <https://metarabbit.wordpress.com/2014/04/18/modernity-ii/>`__ We
still have not been able to come up with something that is clearly better.

§

This flawed paper probably had better altmetrics than anything I'll ever write
in science, again showing what `a bad idea altmetrics are
<https://metarabbit.wordpress.com/2014/02/05/impact-or-how-i-learned-to-start-worrying-and-fear-altmetrics/>`__.

.. [#] feel free to read "Word or Word-like software" in this and subsequent
   sentences. I actually often use Google Docs nowadays.

.. [#] Actually, for collaboration, the Google Docs model is vastly superior as
   you don't have to email back-n-forth.  It also includes a bit of version
   control.

