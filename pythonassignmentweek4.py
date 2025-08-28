def modify_content(content):
    # This function changes the content in some way.
    # Right now, it just turns everything into uppercase letters.
    return content.upper()

def read_and_write_file():
    # Ask the user which file they want to read
    filename = input("Hey there! What's the name of the file you'd like me to read? ")

    try:
        # Try opening the file to read its contents
        with open(filename, 'r') as file:
            print("Reading your file now...")
            original_text = file.read()

        # Modify the content (you can change this logic later if you want!)
        updated_text = modify_content(original_text)

        # Create a new filename to save the modified content
        new_filename = "modified_" + filename

        # Write the updated content to the new file
        with open(new_filename, 'w') as new_file:
            new_file.write(updated_text)

        print(f"All done! 🎉 Your updated file is saved as '{new_filename}'.")

    except FileNotFoundError:
        print(f"Oops! 😬 I couldn't find a file named '{filename}'. Double-check the name and try again.")
    except IOError:
        print(f"Yikes! Something went wrong while trying to read or write the file '{filename}'.")

# Let's run the whole thing
read_and_write_file()