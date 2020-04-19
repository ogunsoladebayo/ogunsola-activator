print("Welcome to our guessing game...")
print("Please, select the level you wish to play.\nPress 1 for Easy.\nPress 2 for Medium \nPress 3 for Hard")
level = input("Enter a level number here: ")
if level == "1":
   # easy level
   print("You have selected Easy Level")
   secretNunber = 6
   guess = 0
   guessCount = 0
   guessLimit = 6
   outOfGuesses = False

   # Check if the guess is correct and user is still within guess limit
   while guess != secretNunber and outOfGuesses == False:
      if guessCount < guessLimit:
         try:
            guess = int(input("Guess a number between 1 - 10: "))
            # converts guess input to eger
            if guess == secretNunber:
               print("You got it right!")
            elif guess > 10:
               print("The value you entered is greater than 10")
            else:
               print("That was wrong")
               guessCount += 1
               print("You have " + str(guessLimit - guessCount) + " guesses left")

         # If the user enters anything other than a number
         except:
            print("The value you entered is not a number.")
      # When the user is out of guess limit
      else:
         outOfGuesses = True
         print("Game over!")


elif level == "2":
      # Medium
      print("You have selected Medium Level")
      secretNunber = 12
      guess = 0
      guessCount = 0
      guessLimit = 4
      outOfGuesses = False

      while guess != secretNunber and outOfGuesses == False:
         if guessCount < guessLimit:
            try:
               guess = int(input("Guess a number between 1 - 20: "))
               if guess == secretNunber:
                  print("You got it right!")
               elif guess > 20:
                  print("The value you entered is greater than 20")
               else:
                  print("That was wrong");
                  guessCount+=1
                  print("You have " + str(guessLimit - guessCount) + " guesses left")

            except:
                  print("The value you entered is not a number.")
                  

         else:
            outOfGuesses = True;
            print("Game over!");

elif level == "3":
   # Hard
      print("You have selected Hard Level")
      secretNunber = 43
      guess = 0
      guessCount = 0
      guessLimit = 3
      outOfGuesses = False

      while guess != secretNunber and outOfGuesses == False:
         if guessCount < guessLimit:
            try:
               guess = int(input("Guess a number between 1 - 50: "))
               if guess == secretNunber:
                  print("You got it right!")
               elif guess > 50:
                  print("The value you entered is greater than 50")
               else:
                  print("That was wrong")
                  guessCount += 1
                  print("You have " + str(guessLimit - guessCount) + " guesses left")

            except:
                  print("The value you entered is not a number.")
                  

         else:
            outOfGuesses = True
            print("Game over!")
else:
   print("You have entered an invalid number")