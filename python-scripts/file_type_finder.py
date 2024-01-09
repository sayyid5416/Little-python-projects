import os


def find_file_types(folder_path, file_extension):
    files_list = []

    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith(f'.{file_extension}'):
                files_list.append(os.path.join(root, file))

    return files_list



def main():
    folder_path = input('> Enter folder path where to find (press enter to use current folder) : ') or os.getcwd()
    file_extension = input('> Enter file extension to find (ex: py): ')
    
    all_files_list = find_file_types(folder_path, file_extension)
    
    print(f"List of .{file_extension} files (total {len(all_files_list)}) :")
    for i in all_files_list:
        print(i)



if __name__ == "__main__":
    main()
    input('\n>Press Enter to exit ')