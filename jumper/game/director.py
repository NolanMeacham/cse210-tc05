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

    """
    def __init__(self):
        self.letter = ''
        self.keep_playing = True
        self.play_again = True
        self.jumper = Jumper()
        self.word_processor = Word_processor()
        self.console = Console()

    def start_game(self):
        """
        Starts the game loop
        """

        while self.keep_playing:
            self.do_user_get_and_display()
            self.do_updates()


    def get_user_get_and_display(self):
        """
        Asks the user input
        """
        
        dashes = self.word_processor.set_hidden_word()
        self.console.write(dashes)
        jumper = self.jumper.update_chute()
        
        self.console.write('')
        self.console.write('---------------')
        

        self.letter = self.console.read("Guess a letter [A-Z]: ")


    def do_updates(self):
        """
        This will adjust data based off of user's choices

        """
        self.word_processor.check_input(self.letter)
        if self.word_processor.check_complete():
            self.console.write("Thanks for playing!")
            self.keep_playing == False
        

