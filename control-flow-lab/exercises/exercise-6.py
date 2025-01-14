# exercise-06 What's the  Season?

# Write the code that:
# 1. Prompts the user to enter the month (as three characters):
#      Enter the month of the year (Jan - Dec):
# 2. Then prompts the user to enter the day of the month: 
#      Enter the day of the month:
# 3. Calculate what season it is based upon this chart:
#      Dec 21 - Mar 19: Winter
#      Mar 20 - Jun 20: Spring
#      Jun 21 - Sep 21: Summer
#      Sep 22 - Dec 20: Fall
# 4. Print the result as follows:
#      <Mmm> <dd> is in <season> 

# Hints:
# Consider using the in operator to check if a string is in a particular list/tuple like this:
# if input_month in ('Jan', 'Feb', 'Mar'):
#
# After setting the likely season, you can use another if...elif...else statement to "adjust" if
# the day number falls within a certain range.
month = input('\nenter a month\n').lower()
day = input('\nenter a day\n')
if month=='dec':
    if day>=21:
        print('winter')
    else:
        print('fall')
elif month =='mar':
    if day<=19:
        print('winter')
    else:
        print('spring')
elif month=='jan' or month=='feb':
    print('winter')
elif month=='apr' or month=='may':
    print('spring')
elif month=='jul' or month=='aug':
    print('summer')
elif month=='sep':
    if day>=22:
        print('fall')
    else:
        print('summer')
elif month=='jun':
   if day<=20:
        print('spring')
   else:
        print('summer')