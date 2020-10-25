class Error(Exception):
    """Base class for exceptions in this module."""
    pass


class GuessNumberError(Error):
    """Base GuessNumberError class for exceptions in this module."""
    _message = None

    def __str__(self):
        if self._message is not None:
            return f'{self.__class__.__name__}: {self._message}'
        else:
            return f'{self.__class__.__name__}: ERROR '


class GuessValueError(GuessNumberError):
    """ Inappropriate argument or value """
    def __init__(self, *args):
        if args:
            self._message = args[0]
        else:
            self._message = None

