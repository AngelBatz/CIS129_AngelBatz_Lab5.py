totalBottles = 0
counter = 1 
todayBottles = 0 
totalPayout = 0 
keepGoing = 'y'

while counter <= 7:
    todayBottles = int(input(f'What is the amount of bottles collected for the day? {counter}'))
    counter = counter + 1
    totalBottles = totalBottles + todayBottles
    totalPayout = totalBottles * .10
    
    
print(f'Total bottles so far this week: {totalBottles}')

print(f'The total payout is ${totalPayout:.2f}\n')

keepGoing = input('Do you want to put anoter week of data in?\n: ')

print()
