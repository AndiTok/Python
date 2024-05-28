from S1E9 import Character


class Baratheon(Character):
    '''Representing the Baratheon family.'''
    def __init__(self, first_name, is_alive=True):
        super().__init__(first_name, is_alive)
        self.family_name = "Baratheon"
        self.eyes = "brown"
        self.hairs = "dark"
    def die(self):
        super().die()

    @property #
    def __str__(self) -> str:
        return f"<bound method {type(self).__name__}.__str__ of Vector: \
{(self.family_name, self.eyes, self.hairs)}>"

    @property #
    def __repr__(self) -> str:
        return f"<bound method {type(self).__name__}.__repr__ of Vector: \
{(self.family_name, self.eyes, self.hairs)}>"
        # return f"Vector: {(self.family_name, self.eyes, self.hairs)}"


class Lannister(Character):
    '''Representing the Lannister family.'''
    def __init__(self, first_name, is_alive=True):
        super().__init__(first_name, is_alive)
        self.family_name = "Lannister"
        self.eyes = "blue"
        self.hairs = "light"
    def die(self):
        super().die()

    @property #
    def __str__(self) -> str:
        return f"<bound method {type(self).__name__}.__str__ of Vector: \
{(self.family_name, self.eyes, self.hairs)}>"

    @classmethod
    def create_lannister(clsm, first_name, is_alive):
        return clsm(first_name, is_alive)
