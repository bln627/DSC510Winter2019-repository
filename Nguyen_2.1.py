# Purpose: Show understanding of variables, expressions, and statements
# Name: Brianna Nguyen
# Assignment #: 2.1

print('Welcome User')

# Retrieving company name from user
name = input('What is your company name?\n')

print(name)

# Retrieving number of feet of cable from user
length = input('How much fiber optic cable would you like to purchase?\n')

# Made sure to have appropriate type for length
int(length)
cost = float(.87)
#Calculating total cost based on user input
total_cost = int(length)*cost

print(total_cost)
#Wanted to insert spaces to isolate the receipt section
print('   ')
print('   ')
print('Customer Receipt\n')
print('Company Name:',name)
print('Cable Length (ft):',int(length))
print('Cost per feet:',cost)
print('Total Cost:',total_cost)



