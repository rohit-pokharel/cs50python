# Converts emoticons :) and :( into their respective emoji 🙂 and 🙁.

def convert(text):
    # Replace :) with 🙂
    text = text.replace(":)", "🙂")

    # Replace :( with 🙁
    text = text.replace(":(", "🙁")

    # Return modified text
    return text

def main():
    # Prompt the user for input
    user_input = input("Enter text: ")

    # Convert the text and print the result
    print(convert(user_input))

main()
