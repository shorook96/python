from Car import Car
from Employee import Employee
from Office import Office


shorookCar=Car("BMW",100,180)
rabyaCar=Car("Nissan",90,150)

shorook= Employee("shorook",2000,"Happy",100,1,shorookCar,"shorook@gmail.com",3000,40)
rabya= Employee("rabya",2000,"Lazy",100,2,rabyaCar,"rabya@gmail.com",2500,50)
employees=[shorook,rabya]
office = Office("ITI",employees)

print(end="\n")
print("--------------------------------------------------------------------------------")
shorook.sleep(7)
print("******* shorook's mood after sleeping 7 hours = ",shorook.mood,"      ********")
shorook.work(9)
print("******* shorook's mood after working 9 hours = ",shorook.mood,'       ********')
print(end="\n")
print("--------------------------------------------------------------------------------")
print("****** shorook's money at the beginning of month  = ",shorook.money,"    ********")
shorook.buy(14)
print("****** money left with shorook after buying 14 items = ",shorook.money," ********")
print(end="\n")
print("--------------------------------------------------------------------------------")
print("****** shorook's Health = ",shorook.healthRate,"                               ********")
shorook.eat(2)
print("****** shorook's health after having 2 meals = ",shorook.healthRate,"           ********")

shorook.send_mail("rabya@gmail.com","vacation","would you like to take a vaccation?","rabya")

