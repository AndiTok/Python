from abc import ABC, abstractmethod


class Character(ABC): #
    '''Class: ABC This is an abstarct class "character"'''
    def __init__(self, first_name, is_alive=True):
        '''Constructor: ABC initialize first_name & is_alive '''
        self.first_name = first_name
        self.is_alive = is_alive

    @abstractmethod #
    def die(self):
        '''Method: ABC funtion/method that changes is_alive status'''
        self.is_alive = False

class Stark(Character):
    '''Class: Child concrete subclass of character'''
    def __init__(self, first_name, is_alive=True):
        '''Constructor: Child iniialize first_name & is_alive '''
        super().__init__(first_name, is_alive)
    def die(self):
        '''Method: Child use function/method'''
        super().die()

# abstract calss useses abc library lol, so is a subclass of abstract???
