# Julian Londono
# 11/12/2024
# P1HW2
# This program can be used to calculate travel expenses and compare it to an initial budget.

print('This program calculates and displays travel expenses')
print('\n')

budget = int(input('Enter Budget:'))
print('\n')

destination = input('Enter your travel destination:')
print('\n')

gas = int(input('How much do you think you will spend on gas?'))
print('\n')

accom = int(input('Approximately, how much will you need for accomodation/hotel?'))
print('\n')

food = int(input('Last, how much do you need for food?'))
print('\n')

print('------------Travel Expense------------')


print('Location:', destination)
print('Initial Budget:', budget)
print('\n')
print('Fuel:', gas)
print('Accomodation:', accom)
print('Food:', food)
bal = budget - gas - accom - food
print('\n')

print('Remaining Balance:', bal)




 
