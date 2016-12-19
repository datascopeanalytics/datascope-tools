from datascope_tools.mixins import UniqueKey

import nose


def test_unique_key():

    class A(UniqueKey):

        def __init__(self, unique):
            self.id = unique

    class B(UniqueKey):

        def __init__(self, unique):
            self.id = unique

    class C(UniqueKey):

        UNIQUE_ATTRIBUTE = 'boogety'

        def __init__(self, unique):
            self.boogety = unique

    a_list = [A(1) for i in range(3)]
    assert len(set(a_list)) == 1

    a_set = {A(1), A(1), A(2), A(2), A(3)}
    assert len(a_set) == 3

    b_list = [B(1) for i in range(3)]
    assert len(set(b_list)) == 1

    ab_list = a_list + b_list
    assert len(set(ab_list)) == 2

    c_list = [C(1) for i in range(3)]
    assert len(set(c_list)) == 1

    abc_list = a_list + b_list + c_list
    assert len(set(abc_list)) == 3


def test_no_unique_key_attribute():

    class D(UniqueKey):

        def __init__(self, unique):
            self.boogety = unique

    # D does not over-ride UNIQUE_ATTRIBUTE, so the default is `id`,
    # but it does not have an `id` attribute
    d_list = [D(1) for i in range(3)]
    with nose.tools.assert_raises(AttributeError):
        set(d_list)
