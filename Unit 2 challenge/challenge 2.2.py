'''Implement a class player that represents a cricket player. The player class should have a method calledplay() which prints "The player is playing cricket. Derive two classes,
Batsman and bowler, from the player class. Override the play()
method in each derived class to print "The batsman is battling"
and "The bowler is bowling", respectively. Write a program to 
create objects of both the Batsman and Bowler classes and call
the play() method for each object.'''

# Define the base class Player
class Player:
  def play(self):
    print("The player is playing cricket.")

# Define the derived class Batsman
class Batsman(Player):
  def play(self):
    print("The batsman is battling.")

# Define the derived class Bowler
class Bowler(Player):
  def play(self):
    print("The bowler is bowling.")

# Create objects of Batsman and Bowler classes
batsman= Batsman()
bowler= Bowler()

# Call the play() method for each object
batsman.play()
bowler.play()
  
  