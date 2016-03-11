import datascope_tools.iterators as i

def test_itergrams():

    bunga = ['a', 'b', 'c', 'd']

    # check with a couple of different sizes
    assert list(i.itergrams(bunga, 2)) == [('a', 'b'), ('b', 'c'), ('c', 'd')]
    assert list(i.itergrams(bunga, 3)) == [('a', 'b', 'c'), ('b', 'c', 'd')]

    # check with the pad argument
    assert list(i.itergrams(bunga, 2, pad=True)) == \
        [('a', 'b'), ('b', 'c'), ('c', 'd'), ('d', None)]

    # make sure it works with a generator, not just a list
    bunga = iter(bunga)
    assert list(i.itergrams(bunga, 2)) == [('a', 'b'), ('b', 'c'), ('c', 'd')]
    
