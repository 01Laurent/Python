# file_handling_assignment.py

def create_and_write_file():
    try:
        # Create and open the file in write mode
        with open('my_file.txt', 'w') as file:
            # Write lines of text to the file
            file.write("Hello, this is the first line.\n")
            file.write("This is the second line with a number: 123.\n")
            file.write("Third line of text with another number: 456.\n")
    except (FileNotFoundError, PermissionError) as e:
        print(f"Error: {e}")
    finally:
        print("File creation and writing process completed.")

def read_and_display_file():
    try:
        # Open the file in read mode
        with open('my_file.txt', 'r') as file:
            # Read and display the content
            content = file.read()
            print("\nFile Content:")
            print(content)
    except (FileNotFoundError, PermissionError) as e:
        print(f"Error: {e}")
    finally:
        print("File reading process completed.")

def append_to_file():
    try:
        # Open the file in append mode
        with open('my_file.txt', 'a') as file:
            # Append additional lines of text
            file.write("Appending a new line to the file.\n")
            file.write("Another appended line with some text.\n")
            file.write("Final appended line with more content.\n")
    except (FileNotFoundError, PermissionError) as e:
        print(f"Error: {e}")
    finally:
        print("File appending process completed.")

# Run the functions
create_and_write_file()
read_and_display_file()
append_to_file()
read_and_display_file()  # Display the file content again to see the appended lines
