import json
import os
from random import randint


# Locate the json file in the ttrader directory wherever the python
# executable is run. os.path is preferred to literal paths in strings
# because it can run on Linux, Mac, or Windows without changing
# code.
thisdir = os.path.dirname(os.path.realpath(__file__))
jsonfilename = "bank_account_json.json"
JSONFILE = os.path.join(thisdir, jsonfilename)

# Note: keeping the data context of a module in a global variable will only
# work with very simple application:

# Global data store:
master_database = None
""" format of master_database:
{
    "4020000000000000": {
        "firstname": "Carter",
        "lastname": "Adams",
        "pin": "1234",
        "balance": 3.50
    },
    "4025000000000000": { ... etc.
}
"""


def initialize():
    """ Load master_database from permanent jsonfile or initialize empty master_database dict """

    # the global keyword allows a function to alter a global variabl
    global master_database
    if not os.path.isfile("bank_account_json.json"):
        master_database = {}
        return

    with open("bank_account_json.json", "r") as file_object:
        master_database = json.load(file_object)


def save():
    """ Write the updated master_database to the permanent json store """
    with open("bank_account_json.json", "w") as file_object:
        json.dump(master_database, file_object, indent=2)


def add_account(userid, sample_card_number,account_info):
    master_database[userid] = {
        "firstname": account_info[0],
        "lastname": account_info[1],
        "card number": sample_card_number,
        "pin": account_info[2],
        "balance": 0.00
    }

def generate_user_id():
    user_id = str(randint(1,999999))
    while user_id in master_database:
        user_id = str(randint(1,999999))
    return user_id

    # newnumber = None

    # while newnumber in master_database or newnumber is None:  # use 'is None & not == None
    #     newnumber = randint(10000, 99999)
    # return newnumber

def luhn(samplenumber):
    for i in range(14,-1,-2):
        samplenumber[i] = samplenumber[i]*2
    for i in range(14,-1,-2):
        if samplenumber[i] > 9:
            samplenumber.append(samplenumber[i] % 10)
            samplenumber[i] = 1
    if sum(samplenumber) % 10 == 0:
        return ("VERIFIED")
    else:
        return ("THIS IS AN INVALID CREDIT CARD")


def generate_and_check_card_number():
    sample_number_raw = str(randint(4*10**15, (5*10**15)-1))
    sample_number = []
    for i in sample_number_raw:
        sample_number.append(int(i))
    
    while luhn(sample_number) != "VERIFIED":
        sample_number_raw = str(randint(4*10**15, (5*10**15)-1))
        sample_number = []
        for i in sample_number_raw:
            sample_number.append(int(i))

    """ TODO: ADD REPEAT CHECK """
    
    return sample_number_raw


def validate_id(userid):
    if userid in master_database:
        return True
    else:
        return False


def validate_pin(userid, user_pin):
    if user_pin == master_database[userid]["pin"]:
        return True
    else:
        return False


def validate_withdrawal(userid, withdrawal_amount):
    if withdrawal_amount > master_database[userid]["balance"]:
        return False
    else:
        return True

def validate_transfer_id(userid, transferid):
    if transferid == userid:
        return "same"
    elif transferid not in master_database:
        return False
    else:
        return True


def validate_transfer_amount(userid, transfer_amount):
    if transfer_amount*1.02 > master_database[userid]["balance"]:
        return False
    else:
        return True


def get_name(userid):
    return master_database[userid]["firstname"]


def get_balance(userid):
    balance=str(round(master_database[userid]["balance"],2))
    if balance[-1] == "0":
        balance=balance+"0"
    return balance


def deposit(userid, deposit_amount):
    """ Add amount to the account's balance return nothing """
    master_database[userid]["balance"] += deposit_amount


def withdraw(userid, withdrawal_amount):
    """ Subtract the amount from user_id """
    master_database[userid]["balance"] -= (withdrawal_amount)


def transfer(userid, targetid, transfer_amount):
    master_database[userid]["balance"] -= (transfer_amount + transfer_amount*.02)
    master_database[targetid]["balance"] += transfer_amount
