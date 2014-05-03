Why Haskell is like C++

I really love these two languages and I also find them very similar in feel.


They are both large languages designed by committees
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

They are and they feel like it.

They are both research languages
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Both C++ and Haskell can be seen as answering the same research question: **can
a language be built around the core set of small principles?**

In Haskell, it is (i) type-correctness, (ii) purity, and (iii) lazyness [#]_;
in C++ it is (i) type-correctness, (ii) efficiency, and (iii) abstraction.

The C++ research programme of trying to get a high-level language that is as
efficient as hand-written C is not any less "researchy" than the Haskell goal
of a pure lazy language. It is impressive that C++ is still one of the few
programming languages where you can write a type-checked, type and criterion
flexible ``sort`` function that is as efficient as C with macros. [#]_

IT is a field dominated by people who are ignorant about IT [#]_. In the 1990s,
people would say things like "Java is a more advanced C++" because it had
garbage collection (a technology from the 1950s), while C++ was doing template
metaprogramming and getting stuck in all sorts of weird corners. Of course,
people should have said "C++ is too advanced and researchy, we should use more
basic tools like Java until C++ is ready for production."

They are both languages with large baggage
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Both have quasi-deprecated builtin string types. In C++'s case, the raw C-style
string stuck around so long that it is now making a bit of a comeback with
UTF-8. The ``std::string`` type is always a bit of an embarrassement as it is
not even look like an STL-container.

Interestingly, they are both languages prone to fads: *X is the right to do Y,
look at the power of X!!!* and then a year or so later: *X is actually very
limited, nobody uses X anymore; but X' is great*. While the core of both
languages is stable, there is a lot of innovation around the edges.

.. [#] Yes, I should have written non-strictness.

.. [#] D might also support this, but D is C++ 2.0, no?

.. [#] Many people paid to program cannot actually write a for loop to save
   their lives.
