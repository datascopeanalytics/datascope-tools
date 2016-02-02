def rank_sorted(sequence, start=1, key=None, reverse=True):
    """A combination or `enumerate` and `sort` iterators that also deals
    with tied ranks.

    """
    previous_value = object() # won't compare equal to anything
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
