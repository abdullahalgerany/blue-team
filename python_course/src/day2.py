# my_list= []
# for i in range(21):
#     #print (i)
#     if i % 2==0:
#         my_list.append(i)
    
# print (my_list)


# suspicious_ips = [x,ip for x in events ]

# class person:
#     def __init__(self, name, age, city):
#         self.name=name
#         self.age=age
#         self.city=city
#     def personal(self):
#         print(f"Hi, I'm {self.name}, {self.age} years old from {self.city}.")
# a1=person("abdullah",27,"Misuratau")
# a1.personal()      

class bank_account:
    def __init__(self, first_balance): 
            self.first_balance=first_balance
    def withdraw(self,amount):
            if amount > self.first_balance:
                 print(f"error")
            else:
                self.first_balance -= amount
            print(f"{self.first_balance}")
    def deposit(self,amount):
        if amount > 0:
            self.first_balance += amount
            print(f"new_balance: {self.first_balance}")
    def showbalance(self, first_balance):
         print(f"curent balance: {self.first_balance}")

account1= bank_account(100)
account1.deposit(300)
account1.withdraw(400)

        