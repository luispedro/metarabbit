Using imread to save disk space

`Imread <http://imread.readthedocs.org/en/latest/>`__ recently gained the
ability to read&write metadata.

We deal with images around here and they can get very large in terms of disk
space. To make things worse, the microscope does not save them in compressed
form.

Imread, however, saves in compressed TIFF. So, we needed to (1) open the file
and (2) resave it. We also do not want to lose the metadata that comes with the
file. in the meanwhile.

This is what I ended up with:

::

    def resave_file(f):
        '''
        resave_file(f)

        Resave a file using imread preserving metadata

        Parameters
        ----------
        f : str
            Filename
        '''
        imdata, meta = imread.imread(f, return_metadata=True)
        tf = tempfile.NamedTemporaryFile('w',
                    prefix='imread_resave_',
                    suffix='.tiff',
                    delete=False,
                    dir=path.dirname(f))
        tf.close()
        imread.imsave(tf.name, imdata, metadata=meta)
        os.rename(tf.name, f)

On a test directory, disk usage went from 55GB down to 12GB.


