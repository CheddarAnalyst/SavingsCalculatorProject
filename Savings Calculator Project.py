#Savings Calculator Project
#Project description
#Bob wonders how much money he can save in a year. Help him figure it out by writing a Python program for him.

#The program should calculate how much a person can save in a year based on their hourly income, hours worked, and weekly cost of living.

#We'll build up your program gradually, one step at a time.

greetings = "Hello "
name = "Bob "
print(greetings + name)

#Calculating weekly income
#Bob earns $20/hour and he works 40 hours per week. Store these numbers in the variables hourly_wage and hours_per_week.

hourly_wage = 20
hours_per_week = 40
income_per_week = hourly_wage * hours_per_week
weeks_per_year = 48
income_per_year = weeks_per_year * income_per_week
print(name + "your yearly income is:")
print(income_per_year)

#Paying rent
#We now know that Bob currently earns about $38k per year. But Bob must pay for food and rent. This costs him $400/week for all 52 weeks of the year.define a variable named spend_per_week which is 400 and then calculate spend_per_year as spend_per_week * 52.

spend_per_week = 400
spend_per_year = spend_per_week * 52
print(name + "your yearly spend on rent is:")
print(spend_per_year)

#Calculating savings
income_per_year = weeks_per_year * income_per_week
spend_per_year = spend_per_week * 52
savings_per_year = income_per_year - spend_per_year
print(name + "your yearly savings:")
print(savings_per_year)


