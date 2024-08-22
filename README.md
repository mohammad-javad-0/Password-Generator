# Password Generator

This project is a GUI-based Password Generator built with Python and PyQt6. It allows users to generate strong, customizable passwords and provides options to include different character types like uppercase, lowercase, numbers, symbols, and spaces. The application also stores a history of generated passwords.

## Features

- Customizable Passwords: Choose the length and character types (uppercase, lowercase, numbers, symbols, spaces) for your password.
- Password History: Review previously generated passwords directly within the application.
- Error Handling: Ensures that at least one character type is selected and that the password length is a minimum of 6 characters.

## Installation

### Dependencies

- PyQt6: Used for creating the graphical user interface.

## Usage

1. Run the Application:
   - Start the application by running the Python script.
   
2. Configure Password Settings:
   - Set the desired password length.
   - Select the character types you want to include (Upper case, Lower case, Numbers, Symbols, Spaces).

3. Generate Password:
   - Click the "CREATE" button to generate a password based on your selected settings.
   - The generated password will appear in the text box.

4. Save or View Password History:
   - Optionally save the generated password to the history.
   - Click the "HISTORY" button to view all previously saved passwords.

## Project Structure

- main.py: The main script containing the GUI and logic for the password generator.
- history.txt: File where the history of generated passwords is saved.

## Contributing

If you wish to contribute, feel free to fork the repository and submit a pull request. Contributions for improving features, fixing bugs, or enhancing the user interface are welcome.
