#Ryne Bigueras
#3/12/22

#Problem 5


list1 = ['pan',  'paper', 'idea', 'rope', 'groceries','slow']

task1 = ["rope, coat, first aid kit", not "slow"]

task2 = ["pan", "groceries", not "small"]

task3 = ["pen, paper, idea", not "confusion"]

check = any(item in list1 for item in task1)

if check is True:
    print(True)
else:
    print(False)


check2 = any(item in list1 for item in task2)

if check2 is True:
    print(True)
else:
    print(False)

check3 = any(item in list1 for item in task3)

if check is True:
    print(True)
else:
    print(False)
