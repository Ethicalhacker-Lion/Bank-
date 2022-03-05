class Details:
    def information(self):
        print("BANK DETAILS")


class Bank(Details):
    def bank_details(self, bank_id, bank_name, bank_address, bank_phone_number):
        print("------------- BANK DETAILS -------------------------")
        print("BANK ID = ", bank_id)
        print("Bank Name = ", bank_name)
        print("Bank Address = ", bank_address)
        print("Bank Phone Number = ", bank_phone_number)
        print("----------------------------------------------------")


class Customer(Bank):
    def customer_details(self, customer_id, customer_name, customer_address, customer_phone_number, balance):
        self.balance = balance
        print("----------------- CUSTOMER DETAILS ------------------")
        print("Customer ID = ", customer_id)
        print("Customer Name = ", customer_name)
        print("Customer Address = ", customer_address)
        print("Customer Phone Number = ", customer_phone_number)
        print("Customer Balance = ", balance)
        print("-----------------------------------------------------")


class Withdraw(Customer):
    def withdraw_amt(self):
        # print(" You have 20000 in Your Bank Account! ")
        self.w = int(input("Enter Withdraw Amount = "))
        self.result = self.balance-self.w
        print("Balance = ", self.result)



class Deposite(Withdraw):
    def deposite_amt(self):
        self.d = int(input("Enter Deposit Amount = "))
        self.result = self.balance+self.d
        print("Balance = ", self.result)


if __name__==("__main__"):

    obj = Deposite()
    while True:

        print('''
        1-- BANK DETAILS--
        2-- CUSTOMER DETAILS--
        3-- WITHDRAW--
        4-- DEPOSIT--
        5-- Exit--
        ''')

        choice = int(input("Enter your Choice:- "))

        if choice == 1:
            obj.bank_details(1001, "HDFC", "Andheri", 9876553558)
        elif choice == 2:
            obj.customer_details(2045, "Hamza", "Jogeshwari", 8765324686, 20000)
        elif choice == 3:
            obj.withdraw_amt()
        elif choice == 4:
            obj.deposite_amt()
        elif choice == 5:
            break
        else:
            print(" Try Again! ")

