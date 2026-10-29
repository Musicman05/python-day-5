bank_dict = {
    "Priya": {"balance": 100, "pin": "4821"},
    "Carlos": {"balance": 300, "pin": "1092"},
    "Amira": {"balance": 0, "pin": "0000"},
    "Jordan": {"balance": 7788, "pin": "9999"},
}

'''
Name: Pin and Name Check
Task: Check if name and pin are in the system assosiated together
Input: Name and Pin
Side Effects: If not in the system respond "you don't have an accont"
Return: If not found- "not value" or the person information
'''
def print_welcome():
    print("=== Welcome To Berklee Bank ===")

def get_username():
    name = input("what is your name?")
    return name

def get_pin():
    pin = input("what is your pin")
    return pin

def get_menu_choice():
    choice = input("do you want to deposit. withdraw balance or quit")
    return choice

def verify_identity(username, pin):
    if bank_dict.get(username):
        user_values = bank_dict.get(username)
        if pin == users_values.get

def get_balance(username):
    if bank_dict.get(username)
    balance = users_values.get("balance")
    Print("your balance is: ", balance)

    return None

def deposit_money(username):
   deposit_amount = int(input("how much would ou like to deposit"))
    
    return None






'''
Name- Balance
Task- check balance
Input- Balance
Return- Current Balance

Name- Deposit
Task- add money to balance
Input- Money to add
side-effect- "your money has been added to your account"
Return- new balance

Name- Withdraw
Task- subtract money from balance
input- money to subtract
side-effect- "your money has been subtracted" / If not more than funds you have available, then prompts "not sufficient funds"
return- new balance

Name- Quit
Task- to exit
Input- Quit
side-effect- goodbye
return- STOP

teacher answer:

name: get_username
task: prompt user for name
input; none
SE print; "what is name'
return; return useranme

name: get_pin
task: prompt user for pin
input; na
SE print; "what is pin'
return; the pin

name: verify_identity
task: take name + pin. See if in system. if so, get data. If not fail
input; username + pin
SE print; no exist "access denied"
return; return balance of user

name: print_menu
task: print options for user offered by the bank
input; None
SE print; "deposit, balance, withdraw, quit"
return; none

name: get_balance
task: gets balance and prints it
input; username
SE print; the balance
return; na

name: deposit_money
task: Ask user how much to despoit, add to balance
input; n/a
SE print; 
return; none

name: withdraw_money
task:
input; 
SE print; 
return; na

name: quit
task:
input; 
SE print; 
return; na

name: 
task:
input; 
SE print; 
return;

name: 
task:
input; 
SE print; 
return;

name: 
task:
input; 
SE print; 
return;

name: 
task:
input; 
SE print; 
return;
name: 
task:
input; 
SE print; 
return;
name: 
task:
input; 
SE print; 
return;








'''

def run_tests():
    withdraw_money



def main():
    print_welcome
    name = get_username
    pin = get_pin()
    valid = verify_identity(name,pin)
    if not valid:
        return


    while True:
        choice =get_menu_choice()
        if users choice == "balance":
            get_balance(name)

            elif users_choice == "withdraw"
    
main()