class UniqueKey(object):

    UNIQUE_ATTRIBUTE = 'id'

    def __eq__(self, other):
        return hash(self) == hash(other)

    def __hash__(self):
        try:
            unique_value = getattr(self, self.UNIQUE_ATTRIBUTE)
        except AttributeError:
            msg = (
                "{} has no attribute {}, but {}.UNIQUE_ATTRIBUTE = {}"
            ).format(
                repr(self),
                repr(self.UNIQUE_ATTRIBUTE),
                self.__class__.__name__,
                repr(self.UNIQUE_ATTRIBUTE),
            )
            raise AttributeError(msg)
        else:
            return hash((self.__class__, unique_value))
