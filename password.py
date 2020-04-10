def password (first_name, last_name):
   f_name_spread = list(first_name)
   l_name_spread = list(last_name)
   import string
   import random
   f = ''
   for i in range(5):
      f = f + random.choice(string.ascii_letters)
   suggest_password =(f_name_spread[0] + f_name_spread[1] + l_name_spread[-2] + l_name_spread[-1] + f)
   print('Welcome ' + first_name + ', Your default password is ' + suggest_password)
   return suggest_password