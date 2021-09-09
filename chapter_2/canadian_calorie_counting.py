# https://dmoj.ca/problem/ccc06j1

borgir = int(input())
side = int(input())
drink = int(input())
dessert = int(input())

calories = 0

menu = ['461', '431', '420', '100', '57', '70', '130', '160', '118', '167', '266', '75']

if borgir == 1:
    calories += int(menu[0])
elif borgir == 2:
    calories += int(menu[1])
elif borgir == 3:
    calories += int(menu[2])

if side == 1:
    calories += int(menu[3])
elif side == 2:
    calories += int(menu[4])
elif side == 3:
    calories += int(menu[5])

if drink == 1:
    calories += int(menu[6])
elif drink == 2:
    calories += int(menu[7])
elif drink == 3:
    calories += int(menu[8])

if dessert == 1:
    calories += int(menu[9])
elif dessert == 2:
    calories += int(menu[10])
elif dessert == 3:
    calories += int(menu[11])

print('Your total Calorie count is ' + str(calories) + '.')
