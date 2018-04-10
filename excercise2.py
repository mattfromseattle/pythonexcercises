# Question 1
name = input('Enter your name: ')
print('Hello ' + name)

# Question 2
hours = input('How many hours were worked?')
rate = input('What was the wage?')
pay = int(hours) * int(rate)
federalMinimum = round(int(pay) / (int(hours) * 7.25) * 100, 2)
seattleMinimum = round(int(pay) / (int(hours) * 15) * 100, 2)
print('The pay for this work is $' + str(pay) + '!')
print('This is ' + str(federalMinimum)  + '% of the federal minimum wage')
print('This is ' + str(seattleMinimum) + '% of the Seattle minimum wage')


# Question 3
farenheit = input('What is the temperature?')
celsius = (int(farenheit) - 32) * (5/9)
print('The temperature in Celsius is ' + str(celsius) + ' degrees')

# Question 4
bill = input('What is the bill?')
person1 = input('What is the first income?')
person2 = input('What is the second income?')
person3 = input('What is the third income?')

# Calculate what percentage of the bill is owed based on income
percentage1 = int(person1) / ((int(person1) + int(person2) + int(person3)))
percentage2 = int(person2) / ((int(person1) + int(person2) + int(person3)))
percentage3 = int(person3) / ((int(person1) + int(person2) + int(person3)))

# Calculate the total owed by each person for the bill
totalOwed1 = round(float(percentage1) * int(bill), 2)
totalOwed2 = round(float(percentage2) * int(bill), 2)
totalOwed3 = round(float(percentage3) * int(bill), 2)

# Display what is owed by each person
print('The person making $' + str(person1) + ' should pay $' + str(totalOwed1) + '.')
print('The person making $' + str(person2) + ' should pay $' + str(totalOwed2) + '.')
print('The person making $' + str(person3) + ' should pay $' + str(totalOwed3) + '.')
