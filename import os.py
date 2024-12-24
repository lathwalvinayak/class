import os

new_dir = "new_directory"
if not os.path.exists(new_dir):
    os.mkdir(new_dir)
    print(f"Directory '{new_dir}' created.")

print("\nFiles and directories in the current working directory:")
print(os.listdir())

file_path = os.path.join(new_dir, "new_text_file.txt")
with open(file_path, "w") as file:
    file.write("This is a sample text written to the new text file.")
    print(f"\nFile '{file_path}' created and content written.")

with open(file_path, "r") as file:
    content = file.read()
    print("\nContent of the new text file:")
    print(content)

new_file_name = os.path.join(new_dir, "renamed_text_file.txt")
os.rename(file_path, new_file_name)
print(f"\nFile renamed to '{new_file_name}'.")

print("\nFiles and directories in the new directory after renaming the file:")
print(os.listdir(new_dir))

os.remove(new_file_name)
os.rmdir(new_dir)
print(f"\nDirectory '{new_dir}' and its contents have been deleted.")
