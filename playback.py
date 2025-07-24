# This program takes user input and replaces spaces with three dots
# It's commonly used to create a "playback" effect where words are separated by pauses

def main():
    # This function contains the main logic of our program
    
    # Get input from the user and store it in a variable called 'user_input'
    # The input() function displays the message and waits for the user to type something
    user_input = input("Enter your text: ")
    
    # Replace all spaces in the user's text with three dots
    # The replace() method takes two arguments:
    # 1. " " (a single space) - what we want to replace
    # 2. "..." (three dots) - what we want to replace it with
    # Then print the result to the screen
    print(user_input.replace(" ", "..."))

# Call the main function directly
main()