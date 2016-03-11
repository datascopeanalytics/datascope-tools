import itertools


def rank_sorted(sequence, start=1, key=None, reverse=True):
    """A combination of `enumerate` and `sort` iterators that also deals
    with tied ranks.

    """
    previous_value = object()  # won't compare equal to anything
    sorted_iterator = sorted(sequence, key=key, reverse=reverse)
    for index, item in enumerate(sorted_iterator, start=start):

        # use key function to choose value if given
        if key is None:
            value = item
        else:
            value = key(item)

        # only update rank when sort value changes
        if value != previous_value:
            previous_value = value
            rank = index

        yield rank, item


def itergrams(iterable, n, pad=False):
    """Iterate over "grams" of an iterable (like "n-grams" if the iterable
    is a list of words). This doesn't require having the whole
    iterable in memory, so can be used for streaming data.

    """
    # tee the original iterator into n identical iterators. Say we
    # start with [a, b, c, d], then it will look like three identical
    # iterators:
    # a, b, c, d
    # a, b, c, d
    # a, b, c, d
    streams = itertools.tee(iter(iterable), n)

    # advance the "cursor" on each iterator by an increasing offset
    # a b c d
    # ^
    # a b c d
    #   ^
    # a b c d
    #     ^
    for stream_index, stream in enumerate(streams):
        for i in range(stream_index):
            next(stream)

    # now, zip the offset streams back together to yield tuples. If
    # pad is True, then it will look like:
    # (a, b, c), (b, c, d), (c, d, None), (d, None, None)
    if pad:
        for i in itertools.izip_longest(*streams, fillvalue=None):
            yield i

    # Otherwise, it will look like:
    # (a, b, c), (b, c, d)
    else:
        for i in itertools.izip(*streams):
            yield i
