# overall database variable
database = ["All user details: "]
# individual user variable
each_user = {}
counter = 0
# this for loop allow collection of details multiple times
for i in database:
   first_name = input("Please, enter your first name: ")
   last_name = input("Please, enter your last name: ")
   email = input("Please, enter your email address: ")
   f_name_spread = list(first_name)
   l_name_spread = list(last_name)
   import string
   import random
   f = ''
   for i in range(5):
      f = f + random.choice(string.ascii_letters)
   suggest_password =(f_name_spread[0] + f_name_spread[1] + l_name_spread[-2] + l_name_spread[-1] + f)
   print('Welcome ' + first_name + ', Your default password is ' + suggest_password)
   counter = counter + 1
   each_user = {
               "ID" : counter,
               "First name" : first_name,
               "last name" : last_name,
               "email" : email}
   password_choice = input("Do you wish to change this password? Type 'Yes' or 'No' only: ")
   password_use = True
   while password_use:
      if password_choice == "No":
         each_user["password"] = suggest_password
         print("Your each_user have been saved")
         password_use = False
         new_user = False
      elif password_choice == "Yes":
         enter_password = True
         while enter_password:
            suggest_password = input("Enter a new password not less than 7 characters: ")
            if len(suggest_password) < 7 :
               print("Password is less than 7 characters")
            else:
               each_user["password"] = suggest_password
               print("Your password has been updated")
               enter_password = False
         password_use = False
   database.append(each_user)
   enter_new_user = input("Would you like to enter another user: ")
   if enter_new_user == "Yes":
      pass
   elif enter_new_user == "No":
      new_user = False
      print(database)
      break