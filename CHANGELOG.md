# CHANGELOG

* v1.1.0 [2019-11-08]: Added a SmartAI computer opponent.
  Added strategy players.SmartAI
  None of the bugs have been fixed.

* v1.1.0 [2019-10-25]: First major release.
  This version is known to contain some bugs.
  
* v1.1.0 [2019-11-20]: Bug Fixing:
    * In file switch.py, Fixed a bug where the game didnt start by moving class initializer and method callers at the bottom outside class Switch()
    * In file switch.py, pick_up_card() method: Fixed a bug where game drew 1 less card than required by adding 1 to n when iterating using range() method.
        * ```Added ➡ n += 1```
    * In file cards.py, class Card: Fixed a bug where more than 52 cards were generated because of an extra Suit in the values.
        * ```values = '2 3 4 5 6 7 8 9 10 J Q K A A'.split() ➡ values = '2 3 4 5 6 7 8 9 10 J Q K A'.split()```
    
* v1.1.0 [2019-11-24]: Bug Fixing:
    * In file switch.py, can_discard() method: Fixed a bug where cards of the same suit or value could not be discarded 
    by fixing the return statement in else statement to return true when either value **OR** suit was same instead of
    **AND**
        *  ```card.suit == top_card.suit and card.value == top_card.value ➡ card.suit == top_card.suit or card.value == top_card.value```
    * In file test_switch.py, def test_can_discard__allows_ace() function: Fixing test case by changing value "K" to "A"
    for one of the tests
        * ```assert s.can_discard(Card('♠', 'K')) ➡ assert s.can_discard(Card('♠', 'A'))```
    * In file switch.py, discard_card() method: Changes made to discard_card() in switch.py to make sure the game
     properly draws 2 cards by changing the if statement condition so draw2 flag is true when card value 2 is discarded.
        * ```elif card.value == '4': ➡ elif card.value == '2':```
    * In file switch.py, discard_card() method: Changes made to self.direction variable in if statement when suit 'K'
    card is discarded to make sure the game properly changes direction
        * ```self.direction *= 1 ➡ self.direction *= -1```

* v1.1.0 [2019-11-26]: Bug Fixing:
    * In file switch.py, get_normalized_hand_sizes() method: Fixed hand size normalization by making sure the player 
    hand sizes were returned in the right order according to direction and turn order by changing range of index to
    change order of concatenation
        * ```sizes[:idx] + sizes[idx:] ➡ sizes[idx:] + sizes[:idx]```
    
    * In file switch.py, run_player() method: Fixed first part of the tests for draw2 and draw4 flags which were giving
     an error because a card was discarded after correct number of cards were drawn by putting the related code into
     the special_event() method
        * ***Note:** didn't use return after if statement to fix it because the README.md is unclear whether the player
        should be able to continue his turn after drawing cards or not so I decided to make it continue his turn*
    
    * In file switch.py, special_event() method: Fixed skip test and second error from the tests for draw2 and draw4 
    flags where flags weren't being set back to false after drawing the cards by changing equality operator to assigment
    operator. 
        *``` self.skip == False ➡ self.skip = False```
        * ```self.draw2 == False ➡ self.draw2 = False```
        * ```self.draw4 == False ➡ self.draw4 = False```
    
    * In file switch.py, run_player() method: Fixed issue where cards weren't being discarded properly by adding
    brackets and an argument to the self.can_discard() method call in the "discardable" variable
        * ```[card for card in player.hand if self.can_discard(card)] ➡ [card for card in player.hand if self.can_discard(card)]```

* v1.1.0 [2019-11-28]: Bug Fixing:
    * In file: player.py, SmartAI() function: Added a missing bracket at the end of sorted_choices variable
    * In file switch.py, run_round() method: Changed equation of variable 'i' inside if/else statement to work properly
        *   ``` i = i+self.direction % len(self.players) ➡ i = (i+self.direction) % (len(self.players))```
    
* In file switch.py, special_event() method, added return for skip, draw2 and draw4 to skip the turn after turn skipped or drawn cards

