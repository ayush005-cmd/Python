"""
Q no 1> create a class Fitnesstracker
   a)A private member (steps)nintialized to 0,to store the user's step count
   b)A fixed target of 1000 steps
Add steps to step var,if steps are +ve, return steps ahead.

check progress (checks how many steps are required to reach the target),if steps=0, if steps=1000,target achieved,else remaining steps"""


#
    













"""Q no. 2> Create a class Movie with the following attributes:
      1)An attribute titile that stores title of the movie.
      2)// ///duration /// in minutes
      3)// ///genre// // movie as string

Implement the  following method:
 
      1_)a method inputMovieDetail() that takes user input for movie title, duration and genre.
      
      2_)a method displayMovie() that prints the movie title, duration, genre to the console.

      3_)a method isLongMovie()that returns True if the movie's duration is more than 150 mins.
"""

class Movie:
    def __init__(self,title,duration,genre):
        self.title=title
        self.duration=duration
        self.genre=genre

    def inputMovieDetail(self):
        self.title=input("Enter the title: ")
        self.duration=int(input("Enter the duration: "))
        self.genre=input("Enter the genre: ")
    def displayMovie(self):
        print(self.title,self.duration,self.genre)

    def isLongMovies(self):
        if self.duration > 150:
            return True
        else:
            return False
        
m = Movie("",0,"")
m.inputMovieDetail()
m.displayMovie()
durex=m.isLongMovies()
print("Is it longer than 150 minutes?",durex)


"""
Qno 3)Create a Base class Payment,with attributes as amount that stores totl amount in float

Implement the  following method calculatr total() that returns the total amount any additional fee.

Create a child class CreditCardPayment that inherits the payment and applies a processing fee

   1)Override the Calculate total method to 3.5% processing fee.
      Formula, total payment= amount + (amount*0.035)
      For cash payment no fee
"""
class Payment:
    def __init__(self,amount):
        self.amount=amount