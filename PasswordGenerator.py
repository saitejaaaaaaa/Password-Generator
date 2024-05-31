from tkinter import *
import string
import random
import pyperclip

# Function to generate a password based on user choice
def generator(): 
    # Define character sets
    small_alphabets = string.ascii_lowercase
    capital_alphabets = string.ascii_uppercase
    numbers = string.digits
    special_characters = string.punctuation

    # Concatenate all character sets
    all_characters = small_alphabets + capital_alphabets + numbers + special_characters

    # Get password length from the Spinbox widget
    password_length = int(length_Box.get())

    # Generate password based on user choice
    if choice.get() == 1: 
        generated_password = ''.join(random.sample(small_alphabets, password_length))
	
    elif choice.get() == 2: 
        generated_password = ''.join(random.sample(small_alphabets + capital_alphabets, password_length))
	
    elif choice.get() == 3: 
        generated_password = ''.join(random.sample(all_characters, password_length))
	

    # Insert the generated password into the Entry widget
    passwordField.delete(0, END)  # Clear any existing content
    passwordField.insert(0, generated_password)


# Function to copy the generated password to clipboard
def copy(): 
    random_password = passwordField.get()
    pyperclip.copy(random_password)


# Create the main Tkinter window
root = Tk()
root.config(bg='pink')
root.title("Password Generator")

# Variable to hold the user choice (1 for weak, 2 for medium, 3 for strong)
choice = IntVar()

# Define font style
Font = ('Arial', 13, 'bold')

# Label for the title
passwordLabel = Label(root, text='Password Generator', font=('Times New Roman', 20, 'bold'), bg='gray20', fg='white')
passwordLabel.grid(pady=10)

# Radio buttons for password strength selection
weakradioButton = Radiobutton(root, text='Weak', value=1, variable=choice, font=Font)
weakradioButton.grid(pady=5)

mediumradioButton = Radiobutton(root, text='Medium', value=2, variable=choice, font=Font)
mediumradioButton.grid(pady=5)

strongradioButton = Radiobutton(root, text='Strong', value=3, variable=choice, font=Font)
strongradioButton.grid(pady=5)

# Label and Spinbox for password length selection
lengthLabel = Label(root, text='Password Length', font=Font, bg='gray20', fg='white')
lengthLabel.grid(pady=5)

length_Box = Spinbox(root, from_=5, to_=18, width=5, font=Font)
length_Box.grid(pady=5)

# Button to generate password
generateButton = Button(root, text='Generate', font=Font, command=generator)
generateButton.grid(pady=5)

# Entry widget to display generated password
passwordField = Entry(root, width=25, bd=2, font=Font)
passwordField.grid()

# Button to copy password to clipboard
copyButton = Button(root, text='Copy', font=Font, command=copy)
copyButton.grid(pady=5)

root.mainloop()