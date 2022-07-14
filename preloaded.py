class RegExp:
    def __init__(self, *args):
        self.args = args

    def __repr__(self):
        args = ", ".join(map(repr, self.args))
        return f"{self.__class__.__name__}({args})"

    def __eq__(self, other):
        return type(self) is type(other) and self.args == other.args


class Any(RegExp):
    pass


class Normal(RegExp):
    pass


class Or(RegExp):
    pass


class Str(RegExp):
    pass


class ZeroOrMore(RegExp):
    pass
