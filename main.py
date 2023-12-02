import pyfiglet

def transform_to_figlet(message):
    return pyfiglet.figlet_format(message)

if __name__ == "__main__":
    # Get user input from the terminal
    user_message = input("Enter a message: ")

    # Transform the message to Figlet format
    figlet_message = transform_to_figlet(user_message)

    # Display the result
    print(figlet_message)
