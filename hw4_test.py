import unittest
import hw4_cards as cards

# SI 507 Winter 2020
# Homework 4 - Code

#########################################
#####   Name: Lulu Guo              #####
#####   Uniqname:luluguo            #####
#########################################

## You can write any additional debugging/trying stuff out code here...
## OK to add debugging print statements, but do NOT change functionality of existing code.
## Also OK to add comments!

class TestCard(unittest.TestCase):
    # this is a "test"
    def test_0_create(self):
        card = cards.Card()
        self.assertEqual(card.suit_name, "Diamonds")
        self.assertEqual(card.rank, 2)

    # Add methods below to test main assignments. 
    def test_1_queen(self):
        card = cards.Card(rank=12)
        self.assertEqual(card.rank_name, "Queen")
    
    def test_2_clubs(self):
        card = cards.Card(suit=1)
        self.assertEqual(card.suit_name, "Clubs")

    def test_3_king_of_spades(self):
        card = cards.Card(suit=3, rank=13)
        self.assertEqual(card.__str__(), "King of Spades")

    def test_4_check_number(self):
        deck = cards.Deck()
        self.assertEqual(len(deck.cards), 52)       

    def test_5_deal_card_return(self):
        deck= cards.Deck()
        self.assertIsInstance(deck.deal_card(), cards.Card)      

    def test_6_deal_card_fewer(self):    
        deck = cards.Deck() 
        count = len(deck.cards)     
        deck.deal_card()
        #deck1 = cards.Deck()
        self.assertEqual(len(deck.cards),count - 1)
    
    def test_7_replace_card_less(self):
        deck = cards.Deck()         
        thecard=deck.deal_card()
        count = len(deck.cards) 
        deck.replace_card(card= thecard)
        self.assertEqual(len(deck.cards), count+1)

    def test_8_replace_card_same(self):
        deck = cards.Deck()
        count = len(deck.cards)
        for acard in deck.cards:
            deck.replace_card(card=acard)
            self.assertEqual(len(deck.cards), count)


############
### The following is a line to run all of the tests you include:
if __name__ == "__main__":
    unittest.main()
