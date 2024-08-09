def new_interest_balance(account_balance, apr, months):
    # Calculate interest
    interest_earned = account_balance * (apr/100 * months/12)
    # Update the balance
    account_balance += interest_earned
    # return the updated balence
    return account_balance, interest_earned

def is_float(str):
    return str.replace(".","",1).isdigit()

def check_input(prompt, return_type):
    while True:
        # Get input
        user_input = input(prompt)
        # clean input.
        user_input = user_input.strip()
        # make sure its valid
        match return_type:
            # for a float
            case 'float':
                if is_float(user_input):
                    user_input = float(user_input)
                    break
                else:
                    print(f"'{user_input}', is not a valid input. Please enter a number.")
            # for an int
            case 'int':
                if user_input.isdigit():
                    user_input = int(user_input)
                    break
                else:
                    print(f"'{user_input}', is not a valid input. Please enter a number.")
            # neither float or int exit
            case _:
                print(f"'{return_type}' No value entered. Exiting program")
                exit()

    return user_input

