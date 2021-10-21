def import_and_create_bank(filename):
    '''
    This function is used to create a bank dictionary.  The given argument is the filename to load.
    '''

    bank = {}
        
    with open(filename) as fin:
        
        lines = fin.readlines()
        for line in lines:
            line = line.strip().split(":")
            
            if len(line) <= 1:
                continue
                
            key = line[0].strip()
            value = line[1].strip()
            try:
                value = float(value)
                bank[key] = bank.get(key, 0) + value
            except:
                continue
    return bank

def signup(user_accounts, log_in, username, password):
    '''
    This function allows users to sign up.
    '''
    upper = []
    lower = []
    number = []
    
    def valid(password):
        
        if username in user_accounts.keys() or len(password) < 8 or username == password:
            return False
        else:
            for i in password:
                if i.isnumeric() == True:
                    number.append(i)
                elif i.isupper() == True:
                    upper.append(i)
                else:
                    lower.append(i)
        if len(upper) >= 1 and len(lower) >= 1 and len(number) >= 1:
            user_accounts[username] = password
            log_in[username] = False
            return True
        else:
            return False
    
    checker = valid(password)
    
    if checker is True:
        return True
    else:
        return False

def import_and_create_accounts(filename):
    '''
    This function is used to create an user accounts dictionary and another login dictionary.  The given argument is the
    filename to load.
    '''

    user_accounts = {}
    log_in = {}

    with open(filename) as fin:
        
        lines = fin.readlines()
        
        for line in lines:
            
            line = line.strip().split("-")
            
            if len(line) <= 1:
                continue
                
            key = line[0].strip()
            value = line[1].strip()
            
            checker = signup(user_accounts, log_in, key, value)
            
            if checker:
                user_accounts[key] = value
                log_in[key] = False

    return user_accounts,log_in

def login(user_accounts, log_in, username, password):
    '''
    This function allows users to log in with their username and password.
    '''

    if username not in user_accounts.keys() or user_accounts[username] != password:
        return False
    else:
        log_in[username] = True
        return True

def update(bank, log_in, username, amount):

    if log_in[username] != True:
        return False
    elif username not in bank.keys():
        if amount >= 0:
            bank[username] = amount
            return True
        else:
            return False
    else:
        if bank.get(username) + amount >= 0:
            bank[username] = bank.get(username) + amount
            return True
        else:
            return False

def transfer(bank, log_in, userA, userB, amount):

    if userA in bank.keys() and log_in[userA] == True and userB in log_in.keys() and bank.get(userA) > amount and amount > 0:
        bank[userA] = bank.get(userA, 0) - amount
        bank[userB] = bank.get(userB, 0) + amount
        return True
    else:
        return False

def change_password(user_accounts, log_in, username, old_password, new_password):
    '''
    This function allows users to change their password.
    '''

    def valid(password):
        
        upper = []
        lower = []
        number = []
        
        if len(password) < 8 or username == password:
            return False
        else:
            for i in password:
                if i.isnumeric() == True:
                    number.append(i)
                elif i.isupper() == True:
                    upper.append(i)
                else:
                    lower.append(i)
        if len(upper) >= 1 and len(lower) >= 1 and len(number) >= 1:
            return True
        else:
            return False
        
    checker = valid(new_password)
    
    if username in user_accounts.keys() and log_in[username] == True and user_accounts[username] == old_password and old_password != new_password and checker == True:
        user_accounts[username] = new_password
        return True
    else:
        return False

def delete_account(user_accounts, log_in, bank, username, password):
    '''
    Completely deletes the user from the online banking system.
    '''

    if username in user_accounts.keys() and password == user_accounts[username] and log_in[username] == True:
        user_accounts.pop(username)
        log_in.pop(username)
        bank.pop(username)
        return True
    else:
        return False

def main():

    bank = import_and_create_bank("bank.txt")
    user_accounts, log_in = import_and_create_accounts("user.txt")

    while True:
        print('bank:', bank)
        print('user_accounts:', user_accounts)
        print('log_in:', log_in)
        print('')

        option = input("What do you want to do?  Please enter a numerical option below.\n"
        "1. login\n"
        "2. signup\n"
        "3. change password\n"
        "4. delete account\n"
        "5. update amount\n"
        "6. make a transfer\n"
        "7. exit\n")

        if option == "1":
            username = input("Please input the username\n")
            password = input("Please input the password\n")

            login(user_accounts, log_in, username, password)

        elif option == "2":
            username = input("Please input the username\n")
            password = input("Please input the password\n")

            signup(user_accounts, log_in, username, password)
        elif option == "3":
            username = input("Please input the username\n")
            old_password = input("Please input the old password\n")
            new_password = input("Please input the new password\n")

            change_password(user_accounts, log_in, username, old_password, new_password)
        elif option == "4":
            username = input("Please input the username\n")
            password = input("Please input the password\n")

            delete_account(user_accounts, log_in, bank, username, password)
        elif option == "5":
            username = input("Please input the username\n")
            amount = input("Please input the amount\n")
            try:
                amount = float(amount)

                update(bank, log_in, username, amount)
            except:
                print("The amount is invalid. Please reenter the option\n")

        elif option == "6":
            userA = input("Please input the user who will be deducted\n")
            userB = input("Please input the user who will be added\n")
            amount = input("Please input the amount\n")
            try:
                amount = float(amount)

                transfer(bank, log_in, userA, userB, amount)
            except:
                print("The amount is invalid. Please re-enter the option.\n")
        elif option == "7":
            break
        else:
            print("The option is not valid. Please re-enter the option.\n")

if __name__ == '__main__':
    main()