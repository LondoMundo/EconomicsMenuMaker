from random import randint
__author__ = 'colin'
breakfast = ["Eggs and bacon", 'Rasin Bran', 'Waffles', 'Pancakes', 'Oatmeal', 'rasins', 'cat food', 'neko nomnoms']
lunch = ['Ham Sandwich with Cheese', 'Turkey Sandwich with cheese', 'Roast beef sandwich with cheese', 'Hot Pockets']
dinner = ['Hamburger with cheese', 'Chicken Fajitas', 'Fish Tacos', 'Salmon', 'Ham Sandwich']
BreakfastBuffer=[]
LunchBuffer=[]
DinnerBuffer=[]

days=7
counter=1
while counter<days:
    BreakfastBuffer.append(breakfast[randint(0,len(breakfast))])
    LunchBuffer.append(lunch[randint(0,3)])
    DinnerBuffer.append(dinner[randint(0, len(dinner))])
    counter+=1

print(BreakfastBuffer)
print(LunchBuffer)

#f=open('list.csv', mode='rw')
#f.write()
