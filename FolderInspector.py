import os

def list_files_and_folders(root_dir, output_file, indent=0, print_filenames=False):
    for foldername, subfolders, filenames in os.walk(root_dir):
        output_file.write('  ' * indent + f'- {os.path.basename(foldername)}\n')
        if print_filenames:
            for filename in filenames:
                output_file.write('  ' * (indent + 1) + f'- {filename}\n')
        for subfolder in subfolders:
            list_files_and_folders(os.path.join(foldername, subfolder), output_file, indent + 1, print_filenames)

if __name__ == "__main__":
    current_dir = os.getcwd()
    print_filenames = input("Do you want to print filenames (yes/no)? ").strip().lower() == 'yes'

    # Output file name
    output_file_path = "folder_structure.txt"
    
    # Open the file with utf-8 encoding to handle special characters
    with open(output_file_path, 'w', encoding='utf-8') as output_file:
        output_file.write(f'Folder structure for: {current_dir}\n')
        list_files_and_folders(current_dir, output_file, print_filenames=print_filenames)
    
    print(f'Folder structure has been written to {output_file_path}')


#TODO Fix bug. There are duplicate folders and files in output
