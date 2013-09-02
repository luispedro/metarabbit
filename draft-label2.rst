A basic labeling principle

In any machine learning based application, you often need labeled data. This
often means asking "experts" to label your data.

**Whenever you ask experts to label data, always get some data independently
labeled by more than one.**

I have seen projects where two people are deemed capable of labeling data,
simply split the data 50/50. If you cannot afford to have the two labelers
label all the data, split it 40-20-40, please: 40% for labeler 1, 40% for
labeler 2, and 20% overlap.

§

There is so much evidence that human labelers can be unreliable and that
inter-operator differences can be huge, that it always worth to have some data
to quantify this effect for your problem.

§

It often even works for the advantage of the automated method. When your method
gets 90% accuracy, it is nice to be able to compare to what a human could do.

In fact, in bioimage informatics, it is often the case that the conversation
goes like this (rarely so clean and nice for my side, but it's my blog and I'll
abridge if I want to):

**Me**: Our automated method gets 90% accuracy.

**Audience member**: Doesn't that just show that it's not ready for prime time?
I mean, if it fails 10% of the time...

**Me**: The alternative right now is human visual analysis.

**Audience member**: Experts will know better.

**Me**: We measured, they don't. You think this is an easy problem by picturing
extreme phenotypes in your mind. Many real cells are actually much more subtle,
especially in high throughput data.

**Audience member**: OK, that's a fair point. How well do people do?

**Me**: 90%, give or take.

**Audience member**: Oh. And could I use this automated method on my problem?

