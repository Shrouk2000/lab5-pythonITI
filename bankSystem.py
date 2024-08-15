class Account:
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return True
        return False

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            return True
        return False

    def transfer(self, target_account, amount):
        if self.withdraw(amount):
            target_account.deposit(amount)
            return True
        return False

    def get_balance(self):
        return self.balance

    def get_statement(self):
        return f"Account {self.account_number}: Balance {self.balance}"


class Customer:
    def __init__(self, customer_id, name):
        self.customer_id = customer_id
        self.name = name
        self.accounts = {}

    def add_account(self, account):
        self.accounts[account.account_number] = account

    def remove_account(self, account_number):
        if account_number in self.accounts:
            del self.accounts[account_number]

    def transfer_money(self, from_account_number, to_account_number, amount):
        if from_account_number in self.accounts and to_account_number in self.accounts:
            return self.accounts[from_account_number].transfer(self.accounts[to_account_number], amount)
        return False

    def getAccountData(self):
        statements = []
        for account in self.accounts.values():
            statements.append(account.get_statement())
        return statements


class Bank:
    def __init__(self, name):
        self.name = name
        self.customers = {}

    def add_customer(self, customer):
        self.customers[customer.customer_id] = customer

    def remove_customer(self, customer_id):
        if customer_id in self.customers:
            del self.customers[customer_id]

    def getCustomerData(self, customer_id):
        if customer_id in self.customers:
            customer = self.customers[customer_id]
            return customer.getAccountData()
        return None

    def get_all_customers(self):
        return list(self.customers.values())



my_bank = Bank("MyBank")

customer1 = Customer(1, "shrouk")
customar2 = Customer(2, "customar2")

my_bank.add_customer(customer1)
my_bank.add_customer(customar2)

customer1_savings = Account("SAV123", 1000)
customer1_checking = Account("CHK123", 500)
customar2_savings = Account("SAV456", 2000)

customer1.add_account(customer1_savings)
customer1.add_account(customer1_checking)
customar2.add_account(customar2_savings)

customer1.transfer_money("SAV123", "CHK123", 200)  
customer1_savings.deposit(500)  

customer1.transfer_money("CHK123", "SAV456", 50)  

print(customer1.getAccountData())
print(customar2.getAccountData())
print(my_bank.getCustomerData(1)) 
print(my_bank.get_all_customers())  