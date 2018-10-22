from getpass import getpass


def accountmenu():
    """ Presents user with a menu and returns their choice as long as
    their choice is valid """

    print('\n',"MAIN MENU", '\n')
    print("1. Create an account")
    print("2. Log in")
    print("3. Quit", '\n')
    choice = input("Please make a selection: ").strip()
    while choice not in ["1","2","3"]:
        print("Invalid selection, choose either 1, 2, or 3")
        choice = ("Please make a selection: ").strip()
    return choice


def create_account():
    """ Prompts user to enter their first/last names and create a 4-digit
    PIN number. Names and PIN number must meet certain criteria before
    they are accepted. That information is then returned to the controller """

    print('\n')
    firstname = input("Please enter your first name: ").strip()
    while " " in firstname:
        print("Names cannot contain spaces")
        firstname = input("Please enter your first name: ").strip()
    while firstname.isalpha() == False:
        print("Names must contain letters only")
        firstname = input("Please enter your first name: ").strip()
    lastname = input("Please enter your last name: ").strip()
        while " " in lastname:
        print("Names cannot contain spaces")
        lastname = input("Please enter your last name: ").strip()
    while lastname.isalpha() == False:
        print("Names must contain letters only")
        lastname = input("Please enter your last name: ").strip()
    user_pin = getpass(prompt="Please create a 4-digit PIN number (*input will be hidden for security*): ")
    while len(user_pin) != 4:
        print("PIN number must be 4 digits in length")
        user_pin = getpass(prompt="Create a 4-digit PIN: ")
    user_pin2 = getpass(prompt="Please re-enter PIN number: ")
    while user_pin2 != user_pin:
        print("PIN numbers must match")
        user_pin2 = getpass(prompt="Re-enter PIN number: ")
    return [firstname, lastname, user_pin]


def creation_confirm(user_id, cardnumber):
    """ Prints a confirmation message on the screen for the user including
    their Luhn-verified credit card number and generated account ID
    
    user_id -- (str) User's account ID generated from the model
    cardnumber -- (str) User's card number generated from the model """

    print('\n')
    print("processing...", '\n')
    print(80*"-")
    print("Here is your computer-generated credit card number: {} {} {} {}".format(cardnumber[0:4], cardnumber[4:8], cardnumber[8:12], cardnumber[12:16]))
    print("Here is your account ID: {}".format(user_id))
    print(80*"-",'\n')
    print("Please save your account ID for future reference as it will be required (along with your PIN) to log in", '\n')


def loginprompt_id():
    """ Prompts the user to enter their ID and returns it to the controller """

    print('\n')
    user_id_input = input("Please enter your account ID: ")
    return user_id_input


def invalidloginid():
    """ Prints an error message if the entered account ID isn't recognized
    and asks the user to re-enter. Returns new input to controller """

    print("Account ID not recognized")
    user_id_input = input("Please enter your account ID: ")
    return user_id_input

def loginprompt_pin():
    """ Prints an error message if the entered account PIN doesn't match the
    PIN of the associated account ID. Prompts the user to re-enter and returns
    that value to the controller """

    user_pin_input = getpass(prompt="Please enter your account PIN (*input will be hidden for security*): ")
    while len(user_pin_input) != 4:
        print("PIN must be 4 digits in length")
        user_pin_input = getpass(prompt="Enter your account PIN: ")
    return user_pin_input
    
def login_success():
    """ Prints a success message to the user after entering a valid ID and
    PIN number """

    print('\n')
    print(80*"-")
    print("logging in...")
    print(80*"-",'\n')


def goodbye():
    """ Displays a farewell message to the user upon exit """

    print("Have a great day!")
    print("Goodbye...")


def mainmenu(name, user_id):
    """ Displays main menu to user after successful login in. Prompts the user
    to select an action and returns that selection to the controller as long
    as it is valid

    name -- (str) First name associated with account ID
    user_id -- (str) User's account ID generated from the model """

    print("Hello, {} ({})".format(name, user_id))
    print('\n', "MAIN MENU")
    print('\n')
    print("1. Check balance")
    print("2. Make a deposit")
    print("3. Make a withdrawal")
    print("4. Make a transfer")
    print("5. Quit")
    print('\n')
    log_in_choice = input("Please make a selection: ").strip()
    while log_in_choice not in ["1", "2", "3", "4", "5"]:
        log_in_choice = input("Invalid selection. Please choose either 1, 2, 3, 4, or 5: ").strip()
    return log_in_choice

def mainmenu_return():
    """ Gives the user the option to either return to the main menu or quit the
    program. Returns their choice to the controller as long as it is valid """

    return_choice = input("Would you like to return to the main menu? (y/n): ").strip().lower()
    while return_choice not in ["y","n"]:
        print("You must type either a 'y' or an 'n'")
        return_choice = input("Would you like to return to the main menu?: ")
    print('\n')
    return return_choice

def display_balance(balance):
    """ Prints the user's balance to the screen

    balance -- (str) User's balance called from the model """

    print("Your current balance is ${}".format(balance))

def deposit_ask():
    """ Prompts the user to enter an amount to be deposited, verifies that it
    is a positive number greater than or equal to 0.01, and returns that
    number to the controller """

    while True:
        try:
            print('\n')
            deposit_amount = round(float(input("Please enter deposit amount: ").strip()),2)
            while deposit_amount < .01:
                print("Deposit amount cannot be 0 or negative")
                deposit_amount = round(float(input("Please enter deposit amount: ").strip()),2)
            return deposit_amount
            break
        except ValueError:
            print("ERROR: not a valid number")

def deposit_return(balance):
    """ Prints the user's new balance to the screen

    balance -- (str) User's new balance called from the model """

    print('\n')
    print("depositing...")
    print(80*"-")
    print("Deposit accepted! Here is your updated balance: ${}".format(balance))
    print(80*"-")

def withdrawal_ask():
    """ Prompts the user to enter an amount to be withdrawn, verifies that it
    is a positive number greater than or equal to 0.01, and returns that
    number to the controller """

    while True:
        try:
            print('\n')
            withdrawal_amount = round(float(input("Please enter withdrawal amount: ").strip()),2)
            while withdrawal_amount < .01:
                print("Withdrawal amount cannot be 0 or negative")
                withdrawal_amount = round(float(input("Please enter withdrawal amount: ").strip()),2)
            return withdrawal_amount
            break
        except ValueError:
            print("ERROR: not a valid number")

def insufficient_funds():
    """ Prints an error message to the screen if the entered withdrawal amount
    is greater than the user's account balance """

    print("ERROR: Insufficient funds")


def withdrawal_return(balance):
    """ Prints the user's new balance to the screen

    balance -- (str) User's new balance called from the model """

    print('\n')
    print("dispensing...")
    print(80*"-")
    print("Please take your cash. Here is your updated balance: ${}".format(balance))
    print(80*"-")

def transfer_fee_declaration():
    """ Lets the user know about the transfer fee and asks if they'd like to
    continue. Valid response is then returned to the controller """

    print("NOTICE: All transfers will incur a transfer fee equal to 2 percent of transfer amount")
    choice = input("Do you wish to proceed? (y/n): ").strip().lower()
    while choice not in ["y","n"]:
        print("You must type either a 'y' or an 'n'")
        choice = input("Would you like to return to the main menu?: ").strip().lower()
    return choice
    


def transfer_id_ask():
    """ Prompts the user to enter the ID of the account they'd like to transfer
    money to. Returns that ID to the controller """

    print('\n')
    transfer_target = input("Please enter target account ID: ").strip()
    return transfer_target

def transfer_id_same():
    """ Prints an error message to the screen if the user enters their own
    account ID """

    print("Target account ID cannot be same as user account ID")

def transfer_id_false():
    """ Prints an error message to the screen if the user enters an account ID
    that is not in the database """

    print("Target account ID not recognized, try again")

def transfer_amount_ask():
    """ Prompts the user to enter an amount to be transferred, verifies that it
    is a positive number greater than or equal to 0.01, and returns that number
    to the controller """

    while True:
        try:
            print('\n')
            transfer_amount = round(float(input("Please enter transfer amount: ").strip()),2)
            while transfer_amount < .01:
                print("Transfer amount cannot be 0 or negative")
                transfer_amount = round(float(input("Please enter transfer amount: ").strip()),2)
            return transfer_amount
            break
        except ValueError:
            print("ERROR: not a valid number")

def transfer_return(balance):
    """ Prints the user's new balance to the screen

    balance -- (str) User's balance called from the model """
    
    print('\n')
    print("transferring...")
    print(80*"-")
    print("Transfer complete. Your updated balance is ${}".format(balance))
    print(80*"-")