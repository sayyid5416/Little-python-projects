import os




def get_lines(filePath:str):
    """ Returns: Number of lines in a file on location `filePath` """
    try:
        with open(filePath) as target:
            return len(target.readlines())

    except UnicodeError:
        with open(filePath, encoding='utf-8') as target:
            return len(target.readlines())
            
    except Exception as e:
        print(f'[Error in {filePath}] {e}')
        return


def get_total_lines(myDir, extension):
    """ Returns: Total lines in all `files.extension` in the `myDir` """
    totalLines = 0
    for rootDir, foldersList, filesList in os.walk(myDir):
        for f in filesList:
            myFile = os.path.join(rootDir, f)
            if myFile.endswith(extension):
                lines = get_lines(myFile)
                if lines is None: continue
                totalLines += lines
                print(f'-----> {myFile} ==== {lines}')   
    return totalLines




if __name__ == "__main__":
    os.system('title Calculate Number of lines')                                                                # Title
    while True:
        try:
            dir_ = input('> Enter the directory location: (press enter for current dir)') or os.getcwd()        # Directory
            fileExt = input('> Enter file extension: ')                                                         # File type
            linesNum = get_total_lines(dir_, fileExt)                                                           # Main Function
        except Exception as e:  print(f'[Main Error] {e}')
        else:                   print(f'\n\nTotal lines in all ".{fileExt}" files of "{dir_}" = {linesNum}')    # Output
        finally:                print('\n\n\n\n')

