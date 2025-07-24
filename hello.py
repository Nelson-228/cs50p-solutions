# This program asks for the user's name and greets them
# It demonstrates basic input/output and string formatting

def main():
    # This function contains the main logic of our program
    
    # Get the user's name and store it in a variable called 'name'
    # The input() function displays the message and waits for the user to type something
    name = input("Enter your name: ")
    
    # Print a greeting using the user's name
    # The f-string (f"...") allows us to embed variables inside the text
    # {name} gets replaced with whatever the user typed
    # So if they type "Alice", it prints "Hello, Alice"
    print(f"Hello, {name}")

# Call the main function to start the program
main()