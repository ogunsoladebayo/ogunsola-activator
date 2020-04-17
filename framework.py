# overall database variable
database = ["All user details: "]
# individual user variable
each_user = {}
counter = 0
# function to generate random password
def func_password(first_name, last_name):
   import string
   import random
   f = ''
   for i in range(5):
      f = f + random.choice(string.ascii_letters)
   suggest_password =(first_name[:2] + last_name[-2:] + f)
   return suggest_password



# this loop continues to run until user does not wish to add new details
for i in database:
   # updates counter value that will be used as ID for the user
   counter = counter + 1

   # collect First Name, Last name and email address
   first_name = input("Please, enter your first name: ")
   last_name = input("Please, enter your last name: ")
   email = input("Please, enter your email address: ")
   password = func_password(first_name, last_name)

   
   # stores all user details collected in a dictionary
   each_user = {
               "ID" : counter,
               "First name" : first_name,
               "last name" : last_name,
               "email" : email,
               "password" : password
               }

   # prints name and password generated               
   print('Welcome ' + first_name + ', Your default password is ' + password)

   
   # Asks user if they want to change the password
   password_use = True
   
   error = True
   while error:
      password_choice = input("Do you wish to change this password? Type 'Yes' or 'No' only: ")
      if password_choice.lower() != "no" and password_choice.lower() != "yes":
         print("You entered an invalid option")
      else:
         while password_use:
            if password_choice.lower() == "no":
               # save password if user does not wish to change generated password
               each_user["password"] = password
               print("Your details have been saved")
               password_use = False


            elif password_choice.lower() == "yes":
               # setting new password
               enter_password = True

               while enter_password:
                  password = input("Enter a new password not less than 7 characters: ")
                  # when password is less than 7 characters
                  if len(password) < 7 :
                     print("Password is less than 7 characters")

                  else:
                     # if password is greater than or equal to 7 characters
                     each_user["password"] = password
                     print("Your password has been updated")
                     enter_password = False
               password_use = False
            error = False
   database.append(each_user)

   
   # to register another user
   enter_new_user = input("Would you like to enter another user? Type 'Yes' or 'No' only: ")
   if enter_new_user.lower() ==  "yes":
      pass
   elif enter_new_user.lower() == "no":
      # breaks entire for loop
      print(database)
      break