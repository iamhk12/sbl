def copy_file(source_filename, destination_filename):
    try:
        with open(source_filename, 'r') as source_file, open(destination_filename, 'w') as destination_file:
            content = source_file.read()
            destination_file.write(content)
        print(f"Content from '{source_filename}' copied to '{destination_filename}' successfully.")
    except FileNotFoundError:
        print("One or both files not found.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

source_file = "source.txt"
destination_file = "destination.txt"
copy_file(source_file, destination_file)
