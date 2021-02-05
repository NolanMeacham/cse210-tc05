from console import Console
from jumper import Jumper
from word_processor import Word_processor
class Director:
    """
    A code template for a person who directs the game. The responsibility of 
    this class of objects is to keep track of the score and control the 
    sequence of play.
    
    Attributes:
        

    General Workflow:
        get_inputs
        do_updates
        do_outputs
    """
    def __init__(self):
        self.
        self.keep_playing = True
        self.
        self.play_again = True
        self.
        self.jumper = Jumper()
        self.word_processor = Word_processor

    def start_game(self):
        """
        Starts the game loop
        """

        while self.keep_playing:
            
            self.do_updates()
            self.do_outputs()
            self.get_inputs()

    def get_inputs(self):
        """
        Asks the user input
        """
        self.console.read("Guess a letter [A-Z]: ")


    def do_updates(self):
        """
        This will adjust data based off of user's choices

        """
        if self.user_H_L_choice == self.dealer.determine_result():
            self.points += 100
        elif self.user_H_L_choice != self.dealer.determine_result():
            self.points -= 75
        else:
            self.points += 0

    def do_outputs(self):
        """
        Outputs the last bit of data, as well as some last minute proccessing
        """
        self.highscore.get_highscore()
        check_points = int(self.points)
        self.highscore.check_highscore(check_points)
        self.highscore.save_highscore
        if self.points <= 0:
            print('YOU LOSE')
            self.keep_playing == False
            quit()
        else:
            print(f'Points = {self.points}')
            self.get_choice = input("Keep Playing? [y/n] ")

            if self.get_choice == 'y':
                self.keep_playing == True
            elif self.get_choice == 'n':
                self.highscore.get_highscore()
                check_points = int(self.points)
                self.highscore.check_highscore(check_points)
                self.highscore.save_highscore()
                print(f'Your highscore was: {self.highscore.highscore}')
                self.keep_playing == False
                quit()
