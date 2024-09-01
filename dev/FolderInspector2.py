# Output to file

import os

def list_files_and_folders(root_dir, indent=0, print_filenames=False, output_file=None):
    with open(output_file, 'a', encoding='utf-8') as file:
        for foldername, subfolders, filenames in os.walk(root_dir):
            file.write('  ' * indent + f'- {os.path.basename(foldername)}\n')
            if print_filenames:
                for filename in filenames:
                    file.write('  ' * (indent + 1) + f'- {filename}\n')
            for subfolder in subfolders:
                list_files_and_folders(os.path.join(foldername, subfolder), indent + 1, print_filenames, output_file)

if __name__ == "__main__":
    current_dir = os.getcwd()
    print_filenames = input("Do you want to print filenames (yes/no)? ").strip().lower() == 'yes'
    output_file = input("Enter the name of the output file: ")

    with open(output_file, 'w', encoding='utf-8') as file:
        file.write(f'Folder structure for: {current_dir}\n')
    
    list_files_and_folders(current_dir, print_filenames=print_filenames, output_file=output_file)

    print(f"Folder structure written to {output_file}")
