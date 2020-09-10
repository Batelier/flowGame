#A case that is an extremity, inherit from Case
import Case

class End(Case.Case):

    def __init__(self, color):
        super().__init__(color)
        line = "line"