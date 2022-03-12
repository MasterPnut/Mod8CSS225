#Ryne Bigueras
#3/12/22

#Problem 4


def leap(year):
    return year%4==0 and not(year%100==0 and not year%400==0)

year = int(input("Give a year: "))

print(leap(year))
