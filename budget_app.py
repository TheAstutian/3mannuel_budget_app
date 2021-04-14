database = {
        "budget_names": [],
        "budget_balances": []
    }
class Budget:

    def __init__(self, category, balance):
        self.category = category
        self.balance = balance

    def check_balance(self):
        return self.balance

    def deposit_funds(self):
        amount = int(input('How much do you want to deposit?\n'))
        self.balance = self.balance + amount
        return self.balance
    
    def withdraw_funds(self):
        amount = int(input('How much do you want to withdraw?\n'))
        if (self.balance<amount):
            print('Insufficient balance')
            withdraw_funds(self)
        else:
            self.balance = self.balance - amount
            return self.balance


def init():

    print('*' * 20)
    print('Welcome to My Budget Pal!')
    print('*' * 20)
    print('What do you want to do?')
    print('1. Create new budget category')
    print('2. Check balance for a specific budget category')
    print('3. Check balnce for all catgories')
    print('4. Deposit funds to a category')
    print('5. Withdraw funds from a category')
    print('6. Transfer funds from one budget to another')
    print('7. Exit app')

def create_category():
    budget_name = input('Enter name of new budget category \n')
    budget_balance = int(input('How much are you budgeting for %s ?  Enter 0 if nothing \n' % budget_name))
    new_budget= Budget(budget_name, budget_balance)
    database["budget_names"].append(budget_name)
    database["budget_balances"].append(budget_balance)
    print('You have created %s budget with a balance of $%d' % (new_budget.category, new_budget.balance))

def check_balance_all():
    if len((database["budget_names"]))<1 :
        print('Your budget list is empty')
    else:
        length=0
        print("*" * 30)
        print("Here are your budget balances")
        while length <  len(database["budget_names"]):
            print("%s: $%d" % (database["budget_names"][length],database["budget_balances"][length]))
            length = length+1

def check_balance_specific():
    specific= int(input('Enter name of budget category'))
    

