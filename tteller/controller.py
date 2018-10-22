from tteller import view
from tteller import model


def loginloop():
  
    choice = view.accountmenu()

    if choice == "1":  # create account
        create_account()
    
    if choice == "2":  # login
        user_id_input = view.loginprompt_id()
        while True:
            if model.validate_id(user_id_input) == False:
                view.invalidloginid()
                user_id_input = view.loginprompt_id()
            else:
                break
        
        user_pin_input = view.loginprompt_pin()
        while True:
            if model.validate_pin(user_id_input, user_pin_input) == False:
                user_pin_input = view.loginprompt_pin()
            else:
                break
        view.login_success()
        mainloop(user_id_input)
        

    if choice == "3":
        exitprogram()


def exitprogram():
    model.save()
    view.goodbye()
    quit()


def create_account():
    account_info = view.create_account()
    user_id = model.generate_user_id()
    user_card_number = model.generate_and_check_card_number()
    model.add_account(user_id, user_card_number, account_info)
    view.creation_confirm(user_id,user_card_number)
    return loginloop()


def mainloop(user_id):
    login_menu_choice = view.mainmenu(model.get_name(user_id), user_id)
    if login_menu_choice == "1":
        balance = model.get_balance(user_id)
        view.display_balance(balance)
        return_choice = view.mainmenu_return()
        if return_choice == "y":
            mainloop(user_id)
        else:
            exitprogram()
    
    if login_menu_choice == "2":
        deposit_amount = view.deposit_ask()
        model.deposit(user_id, deposit_amount)
        view.deposit_return(model.get_balance(user_id))
        return_choice = view.mainmenu_return()
        if return_choice == "y":
            mainloop(user_id)
        else:
            exitprogram()
    
    if login_menu_choice == "3":
        withdrawal_amount = view.withdrawal_ask()
        while model.validate_withdrawal(user_id, withdrawal_amount) == False:
            view.insufficient_funds()
            withdrawal_amount = view.withdrawal_ask()
        model.withdraw(user_id, withdrawal_amount)
        view.withdrawal_return(model.get_balance(user_id))
        return_choice = view.mainmenu_return()
        if return_choice == "y":
            mainloop(user_id)
        else:
            exitprogram()
    
    if login_menu_choice == "4":
        transfer_fee_response = view.transfer_fee_declaration()
        if transfer_fee_response == "y":
            transfer_id = view.transfer_id_ask()
            while model.validate_transfer_id(user_id, transfer_id) == "same":
                view.transfer_id_same()
                transfer_id = view.transfer_id_ask()
            while model.validate_transfer_id(user_id, transfer_id) == False:
                view.transfer_id_false()
                transfer_id = view.transfer_id_ask()
            transfer_amount = view.transfer_amount_ask()
            while model.validate_transfer_amount(user_id, transfer_amount) == False:
                view.insufficient_funds()
                transfer_amount = view.transfer_amount_ask()
            model.transfer(user_id, transfer_id, transfer_amount)
            view.transfer_return(model.get_balance(user_id))
            return_choice = view.mainmenu_return()
            if return_choice == "y":
                mainloop(user_id)
            else:
                exitprogram()
        else:
            mainloop(user_id)
    else:
        exitprogram()


def run():
    model.initialize()
    loginloop()


if __name__ == "__main__":
    run()
