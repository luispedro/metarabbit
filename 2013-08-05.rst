Let me highlight a good example of continuous improvement in mahotas and the
advantages of `eating your own dog food
<http://en.wikipedia.org/wiki/Eating_your_own_dog_food>`__.

I was using `mahotas <http://mahotas.rtfd.org>`__ to compute some wavelets, but I couldn't remember
the possible parameter values. So I got some error::

    [1]: mh.daubechies(im, 'db4')

    ---------------------------------------------------------------------------
    ValueError                                Traceback (most recent call last)
    <ipython-input-6-2e939df57e6a> in <module>()
    ----> 1 mh.daubechies(im, 'db4')

    /home/luispedro/work/mahotas/mahotas/convolve.pyc in daubechies(f, code, inline)
        492     '''
        493     f = _wavelet_array(f, inline, 'daubechies')
    --> 494     code = _daubechies_codes.index(code)
        495     _convolve.daubechies(f, code)
        496     _convolve.daubechies(f.T, code)

    ValueError: 'db4' is not in list

I could have just looked up the right code and moved on. Instead, I considered
the unhelpfulness of the error message a bug and fixed it (`here is the commit
<https://github.com/luispedro/mahotas/commit/1cc50e6e0142cfb759483d382efec7e13f7fc666>`__)

Now we get a better error message::

    ValueError: mahotas.convolve: Known daubechies codes are ['D2', 'D4', 'D6',
    'D8', 'D10', 'D12', 'D14', 'D16', 'D18', 'D20']. You passed in db4.

You still get an error, but at least it tells you what you should be doing.

**Good software works well. Excellent software fails well too.**

