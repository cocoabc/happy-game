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
    

