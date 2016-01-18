import sys
import functools
import logging
import os
import cPickle as pickle
import hashlib
import time


class cache(object):
    """Decorator. Caches a function's return value each time it is called.
    If called later with the same arguments, the cached value is returned
    (not reevaluated).
    """

    def __init__(self, cache_dir='.cache', expire_after=float('inf')):
        self.cache_dir = cache_dir
        self.expire_after = expire_after
        self.nicename = 'function'

    def __call__(self, function):

        # Create a human-readable function name that is suitable for
        # log message and the filename on disk.
        self.nicename = '%s.%s' % (function.__module__, function.__name__)

        @functools.wraps(function)
        def decorated(*args, **kwargs):

            # ensure the cache directory exists
            if not os.path.isdir(self.cache_dir):
                os.makedirs(self.cache_dir)

            filepath = self.create_filename(function, *args, **kwargs)

            if self.is_fresh(filepath):

                message = 'Reading result for `%s` from cache' % self.nicename
                logging.debug(message)

                # read from disk
                with open(filepath, 'rb') as infile:
                    return pickle.load(infile)

            message = 'Caching call to `%s` with args `%s`' % \
                (self.nicename, str(args))
            logging.debug(message)

            # run the function
            result = function(*args, **kwargs)

            # write result to diskbefore returning
            with open(filepath, 'wb') as outfile:
                pickle.dump(result, outfile, protocol=pickle.HIGHEST_PROTOCOL)

            return result
        return decorated

    def in_cache(self, filepath):
        """Test to see whether the file is in the cache."""
        return os.path.isfile(filepath)

    def is_fresh(self, filepath):
        """Test to see whether or not the file is in the cache and whether or
        not it has been in the cache longer than expire_after
        seconds.

        """
        if self.in_cache(filepath):
            last_modified = os.path.getmtime(filepath)
            age = time.time() - last_modified
            return age <= self.expire_after

    def create_filename(self, function, *args, **kwargs):
        """Create a filename to use on disk."""

        # but for arguments, just hash them to avoid any craziness
        # with trying to make them OK for filename
        suffix = hashlib.md5(str(args) + str(kwargs)).hexdigest()

        filename = '%s-%s.pickle' % (self.nicename, suffix)
        return os.path.join(self.cache_dir, filename)
