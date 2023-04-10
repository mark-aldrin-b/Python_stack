from classes.deck import Deck

bicycle = Deck()

bicycle.show_cards()


class Game_2_nine:
    
    def __init__(self):
        self.cardsdeck = []
    
    def drawcards(self):
        print(self.random.randint(1,13))
        
        return self

    def play(self):
        pass

aldrin = Game_2_nine()

aldrin.drawcards()
