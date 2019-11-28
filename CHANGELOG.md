# CHANGELOG

* v1.1.0 [2019-11-08]: Added a SmartAI computer opponent.
  Added strategy players.SmartAI
  None of the bugs have been fixed.

* v1.1.0 [2019-10-25]: First major release.
  This version is known to contain some bugs.
  
* v1.1.0 [2019-11-20]: Bug Fixing:
    * Fixed a bug where the game didnt start by moving class and method callers outside class Switch()
    * Fixed a bug where game drew 1 less card than required by adding 1 to iterator
    * Fixed a bug where more than 52 cards were generated because of an extra Suit in card generator
    
* v1.1.0 [2019-11-24]: Bug Fixing:
    * Fixed a bug where cards of the same suit or value could not be discarded by fixing the can_discard() method in
    class Switch()
    * Fixing test case for ace value (test_can_discard__allows_ace) by changing value "K" to "A"
    * Changes made to discard_card() in switch.py to make sure the game properly skips players or draws cards
    * Changes made to discard_card() in switch.py to make sure the game properly changes direction

* v1.1.0 [2019-11-26]: Bug Fixing:
    * Fixed hand size normalization by making sure the player indexes were in the right order according to direction
    * Fixed first part of the tests for draw2 and draw4 flags which were giving error by isolating part of run_player() 
    method in switch()
    * Fixed second part of the tests for draw2 and draw4 flags where flags weren't being set back to false after drawing
    the cards
    * Fixed issue in run_player() method where cards weren't being discarded properly by making sure card variable used
    can_discard() method properly

* v1.1.0 [2019-11-28]: Bug Fixing:
    * Added a missing bracket in SmartAI() function in players.py
    * In file switch.py, run_round method: Changed equation of variable 'i' inside if/else statement to work properly
        *   i = i+self.direction % len(self.players) ---to---> i = (i+self.direction) % (len(self.players))
    
    (skip test)
