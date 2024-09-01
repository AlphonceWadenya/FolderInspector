import os

def list_files_and_folders(root_dir, indent=0, print_filenames=False):
    for foldername, subfolders, filenames in os.walk(root_dir):
        print('  ' * indent + f'- {os.path.basename(foldername)}')
        if print_filenames:
            for filename in filenames:
                print('  ' * (indent + 1) + f'- {filename}')
        for subfolder in subfolders:
            list_files_and_folders(os.path.join(foldername, subfolder), indent + 1, print_filenames)

if __name__ == "__main__":
    current_dir = os.getcwd()
    print_filenames = input("Do you want to print filenames (yes/no)? ").strip().lower() == 'yes'
    print(f'Folder structure for: {current_dir}')
    list_files_and_folders(current_dir, print_filenames=print_filenames)

#TODO Fix bug. There are duplicate folders and files in output