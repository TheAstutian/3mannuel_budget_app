database_objects = [] #database containing objects instantiated with Budget class
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
            #if user wishes to withdraw more funds than is available
            insuff= int(input('Insufficient balance. 1. Try again 2. Go to menu \n'))
            if insuff==1:
                #sends user back to withdraw_funds function
                withdraw_funds(self)
            elif insuff==2:
                init()
                #sends user back to main menu
            else:
                print('Invalid option selected')
                interlude()
                #sends user back to interlude
        else:
            self.balance = self.balance - amount
            return self.balance

    #To transfer balance from one Budget category to another, we use two methods: 
    #one empties the budget we're transfering from and the other adds that amount
    #to the budget category we're transferring to

    #empties balance
    def empty_balance(self):
        balance = self.balance
        self.balance=0
        return balance
    
    #adds emptied amount to balance
    def add_balance(self, balance):
        self.balance= self.balance + balance
        return self.balance 

#initializes app
def init():

    print('*' * 20)
    print('Welcome to My Budget Pal!')
    print('*' * 20)
    print('What do you want to do?')
    print('1. Create new budget category')
    print('2. Check balance for specific budget category')
    print('3. Check balance for all catgories')
    print('4. Deposit funds to a category')
    print('5. Withdraw funds from a category')
    print('6. Transfer funds from one budget category to another')
    print('7. Exit app')
    init_choice = int(input('Choose an option and press enter \n'))
    if (init_choice==1):
        create_category()
    elif(init_choice==2):
        check_balance_specific()
    elif(init_choice==3):
        check_balance_alls()
    elif(init_choice==4):
        deposit()
    elif(init_choice==5):
        withdrawal()
    elif(init_choice==6):
        transfer()
    elif(init_choice==7):
        exit()
    else:
        print('Invalid option selected. Try again')
        init()
    #after executing any of the options, program goes to interlude
    interlude()

def interlude():
    interlude_bool = int(input('Do you want to perform another operation? 1. Yes 2. No \n'))
    if (interlude_bool ==1):
        init()
    elif(interlude_bool==2):
        logout()
    else:
        print('Invalid option selected')
        interlude()

def logout():
    logout_bool = int(input('Do you want to exit this app? 1. Yes 2. No \n'))
    if (logout_bool ==1):
        print('*' * 20)
        print('Goodbye!')
        print('*' * 20)
        exit()
    elif(logout_bool==2):
        init()
    else:
        print('Invalid option selected')
        logout()

def create_category():
    #creates a new Budget category by instantiating the Budget class
    budget_name = input('Enter name of new budget category \n')
    budget_balance = int(input('How much are you budgeting for %s ?  Enter 0 if nothing (enu gbe lol) \n' % budget_name))
    new_budget= Budget(budget_name, budget_balance)
    database_objects.append(new_budget) #adds new BUdget category to database containing objects
    print('*' * 20)
    print('You have added %s to your budget list with a balance of $%d' % (new_budget.category, new_budget.balance))
    print('*' * 20)


def check_balance_specific():
    specific= input('Enter name of budget category \n')

    for budget in database_objects:
        if (budget.category == specific):
            print('*' * 20)
            print('Your %s balance is $%d'% (budget.category,budget.check_balance()))
            print('*' * 20)
            interlude()
    print('Budget not found, try again')
    interlude()
        
    
def check_balance_alls():
    print("*" * 30)
    print("Here are your budget categories and balances:")
    for budget in database_objects: 
        print("%s : $%d" % (budget.category, budget.balance))
    print("*" * 30)

def deposit():
    specific= input('Enter name of budget category \n')
    for budget in database_objects:
        if (budget.category == specific):
            print('*' * 20)
            print('You now have $%d in your %s budget'% (budget.deposit_funds(), budget.category))
            print('*' * 20)
            interlude()
    print('Budget named "%s" not found, please add it and try again'% specific)
    interlude()

def withdrawal():
    specific= input('Enter name of budget category \n')
    for budget in database_objects:
        if (budget.category == specific):
            
            print('*' * 20)
            print('You now have $%d in your %s budget' % (budget.withdraw_funds(),budget.category))
            print('*' * 20)
            interlude()
    print('Budget named "%s" not found, please add it and try again'% specific)
    interlude()

def transfer():
    specific= input('Enter name of budget category you want to transfer from \n')
    for budget in database_objects:
        if (budget.category == specific):
            lebal= budget.empty_balance()
            print('You have emptied the %s budget of its $%d' % (budget.category, lebal))
            specific2= input('Enter name of budget category you want to transfer to \n')
            for budget in database_objects:
                if (specific2== budget.category):
                    print('You have added %d to your %s Budget'% (lebal,budget.category))
                    print('Your %s budget is now $%d' %(budget.category,budget.add_balance(lebal)))
                    interlude()
            print('Budget named "%s" not found, please add it and try again'% specific2)
            interlude()
    print('Budget named "%s" not found, please add it and try again'% specific)
    interlude()

init() 
