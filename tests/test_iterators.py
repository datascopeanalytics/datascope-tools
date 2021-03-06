from datascope_tools.iterators import itergrams, rank_sorted


def test_itergrams():

    bunga = ['a', 'b', 'c', 'd']

    # check with a couple of different sizes
    assert list(itergrams(bunga, 2)) == [('a', 'b'), ('b', 'c'), ('c', 'd')]
    assert list(itergrams(bunga, 3)) == [('a', 'b', 'c'), ('b', 'c', 'd')]

    # check with the pad argument
    assert list(itergrams(bunga, 2, pad=True)) == \
        [('a', 'b'), ('b', 'c'), ('c', 'd'), ('d', None)]

    # make sure it works with a generator, not just a list
    bunga = iter(bunga)
    assert list(itergrams(bunga, 2)) == [('a', 'b'), ('b', 'c'), ('c', 'd')]


def test_rank_sorted():

    bunga = ['a', 'c', 'b', 'd']

    assert list(rank_sorted(bunga)) == [(1, 'd'), (2, 'c'), (3, 'b'), (4, 'a')]

    # try with reverse
    assert list(rank_sorted(bunga, reverse=False)) == \
        [(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd')]

    # now put in some ties
    bunga = [95, 95, 90, 85]
    assert list(rank_sorted(bunga)) == [(1, 95), (1, 95), (3, 90), (4, 85)]


def test_rank_sorted_with_key():

    import operator

    scores = [
        ('alex', 100),
        ('bo', 100),
        ('brian', 100),
        ('dean', 10),
        ('horatio', 90),
        ('irmak', 100),
        ('jess', 100),
        ('karlota', 90),
        ('melba', 90),
        ('meridith', 100),
        ('michael', 100),
        ('mike', 100),
        ('mollie', 100),
        ('vlad', 100),
    ]
    answer = [
        (1, ('alex', 100)),
        (1, ('bo', 100)),
        (1, ('brian', 100)),
        (1, ('irmak', 100)),
        (1, ('jess', 100)),
        (1, ('meridith', 100)),
        (1, ('michael', 100)),
        (1, ('mike', 100)),
        (1, ('mollie', 100)),
        (1, ('vlad', 100)),
        (11, ('horatio', 90)),
        (11, ('karlota', 90)),
        (11, ('melba', 90)),
        (14, ('dean', 10)),
    ]
    assert list(rank_sorted(scores, key=operator.itemgetter(1))) == answer
