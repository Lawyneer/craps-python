'''
get_valid_input.py - function to ensure user input is valid.

Inputs:
    prompt - a prompt for what the user should enter.
    valid_values - acceptable inputs from the user.

Outputs:
    value - one of the valid_values.
'''

# Define function
def get_valid_input(prompt, valid_values):
    """Prompt until the user enters one of the valid values."""
    while(True):
        try:
            value = int(input(prompt))
        except(ValueError):
            print("Please enter a number.\n")
            continue
        # end try, except
        
        if(value in valid_values):
            return value
        # end if
        
        print("Check your input. Valid entries are:", valid_values, "\n")
    # end while
# end function