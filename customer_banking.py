# Import the create_cd_account and create_savings_account functions
# ADD YOUR CODE HERE
from utils import prompt_user
from cd_account import create_cd_account
from savings_account import create_savings_account
# Define the main function
def main():
    """This function prompts the user to enter the savings and cd account balance, interest rate,
    and the length of months to determine the interest gained.
    It displays the interest earned on the savings and CD accounts and updates the balances.
    """
    # Prompt the user to set the savings balance, interest rate, and months for the savings account.
    # ADD YOUR CODE HERE
    savings_balance = prompt_user("Enter your starting balance: ", "float")
    savings_interest = prompt_user("Enter your savings interest rate: ", "float")
    savings_maturity = prompt_user("Enter the months: ", "int")

    # Call the create_savings_account function and pass the variables from the user.
    updated_savings_balance, interest_earned = create_savings_account(savings_balance, savings_interest, savings_maturity)
    #new_balance = updated_savings_balance(savings_balance)

    # Print out the interest earned and updated savings account balance with interest earned for the given months.
    # ADD YOUR CODE HERE
    print(f"Your new savings balance is ${updated_savings_balance:,.2f}")
    print(f"Your interest rate is {savings_interest:.2f}%")
    print(f"you earned ${interest_earned:,.2f} over {savings_maturity} months")

    # Prompt the user to set the CD balance, interest rate, and months for the CD account.
    # ADD YOUR CODE HERE
    cd_balance = prompt_user("Enter your starting CD balance:", "float")
    cd_interest = prompt_user("Enter your CD interest rate:", "float")
    cd_maturity = prompt_user("Enter the CD months: ", "int")

    # Call the create_cd_account function and pass the variables from the user.
    updated_cd_balance, cd_interest_earned = create_cd_account(cd_balance, cd_interest, cd_maturity)

    # Print out the interest earned and updated CD account balance with interest earned for the given months.
    # ADD YOUR CODE HERE
    print(f"Your new CD balance is ${updated_cd_balance:,.2f}")
    print(f"Your interest rate is {cd_interest:.2f}%")
    print(f"you earned ${cd_interest_earned} over {cd_maturity} months.")

if __name__ == "__main__":
    # Call the main function.
    main()
