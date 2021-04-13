# Imports
import os



def main_____fctn(current_dir, extension):
    
    directory_data = os.walk(current_dir)
    
    final_num = 0
    for root, folders_list, files_list in directory_data:
        for f in files_list:
            my_file = os.path.join(root, f)
            my_file_extension = my_file.split('.')[-1]
            if extension == my_file_extension:
                try:
                    with open(my_file) as target:
                        length = len(target.readlines())
                        final_num += length
                        print(f'-----> {my_file} ==== {length}')
                except UnicodeError:
                    with open(my_file, encoding='utf-8') as target:
                        length = len(target.readlines())
                        final_num += length
                        print(f'-----> {my_file} ==== {length}')
                except Exception as e:
                    print(f'[Error in {my_file}] {e}')
                    
    return final_num




if __name__ == "__main__":
    while True:
        os.system('title Calculate Number of lines')                                            # Title
        
        try:
            dir_ = input('> Enter the directory location: ')                                    # Inputs
            file_ext = input('> Enter file extension: ')
            if dir_  == '':
                dir_ = os.getcwd()
            number_of_lines = main_____fctn(dir_, file_ext)                                     # Main Function
        except Exception as e:
            print(f'[Main Error] {e}')
        else:
            print(f'\n\nTotal Number of lines in all ".{file_ext}" files of {dir_} = {number_of_lines}\n\n')            # Output
        finally:
            print('\n\n\n\n')

