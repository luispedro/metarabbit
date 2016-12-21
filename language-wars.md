Why (computer) language wars make sense (even if they are stupid)


## Progamming languages have network effects

Some languages are better than others, but most of what it matters is not
whether the language itself is any good, but how large the ecosystem around it
is. You can have a perfect language, but if there is no support for it in your
favorite editor/IDE, no good HTTPS libraries which can handle HTTP2.0, then
working in it will be efficient or even less pleasant than working in Java.

Haskell is a pretty nice programming language, but working in it got much nicer
once [stack](https://docs.haskellstack.org/) appeared on the scene. The
language is the same, even the set of libraries is the same, but having a
better way to install packages is enough to fundamentally change your
experience. Still, it's enough of a niche language than nobody has yet written
a tool comparable to [ccache](https://ccache.samba.org/) for the C/C++ world
(instantaneous rebuilds are amazing for a compiled language).

## Your value and the value of your code increases if you program in a popular language

This is not strictly true: if your work is self-contained, then it may be very
useful on its own even if you wrote it in COBOL, but often the more people can
build upon your work, the more valuable that work is. So if your work is
written in C or Python as opposed to Haskell or Ada.

This is somewhat field-dependent. Knowing R is great if you're a
bioinformatician, but almost useless if you're writing webserver code. Even
general-purpose languages get niches based on history and tools. Functional
programming languages somehow seems to be more popular in the financial sector
than in other fields.

## Changing languages is easy, but costly

Sure, any decent programmer can "pick up" a new language in a few days. I can
probably even debug code in any procedural language even without having ever
seen it before. However, to really become proficient, it often takes much
longer: you need to encounter and internalize the most natural way to do things
in the new language, learn about different libraries and tools, &c. None of
this is "hard", but it all takes a long time.

§

In conclusion, I don't think it's completely irrational to become clubish about
programming languages.


