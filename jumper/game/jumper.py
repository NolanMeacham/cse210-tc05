

class Jumper():
    """Class that holds information regarding the jumper.

    Stereotype:
        Information Holder

    Attributes:
        self.num_guesses (int): counts the number of times the user has guessed a letter.
        self.is_alive (boolean): determines if the jumpe is still alive or not, based on how much chute is left.
        self.chute (): holds the string to display the jumpers parachute.
    """

    def __init__(self):
        """
        """
        self.num_guesses = 0
        self.is_alive = True
        self.head = 'O'
        self.chute = ['    ___',
                      '  /     \ ',
                      ' /_______\ ',
                      ' \       / ',
                      '  \     /  ',
                      '   \   /',
                      f'     {self.head}    ',
                      '    /|\   ',
                      '    / \   ']

    def update_chute(self, result):
        """
        Updates the parachute each turn.
        Updates the jumper head based self.is_alive boolean.

        Args:
            result (boolean): tells the update_chute whether or not the chute needs to be reduced. 
                              If False, the chute is reduced by one line.
                              If True, the chute is not changed
        
        Returns:
            chute (list): each line of the chute

        """
        self.num_guesses += 1
        if self.num_guesses > 6:
            self.is_alive = False

        # TODO: If result is True, the chute doesn't change. If result is Fale, the chute is reduced by one line.
        if result == False:
            self.chute.pop(0)

        # TODO: If is_alive is True, self.head = 'O', otherwise, self.head = 'X'
        if self.is_alive == False:
            self.chute[-3] = '     X    '

        # This is being used right now just to test the chute display
        # for line in self.chute:
        #     print(line)

        return self.chute



# # Test
# jumper = Jumper()
# jumper.update_chute(True)

# for line in jumper.chute:
#     print(line)
