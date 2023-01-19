import os




def get_lines(filePath:str):
    """ Returns: Number of lines in a file on location `filePath` """
    try:
        with open(filePath) as f:
            return len(
                f.readlines()
            )
    except UnicodeError:
        with open(filePath, encoding='utf-8') as f:
            return len(
                f.readlines()
            )
    except Exception as e:
        return print(
            f'[Error in "{filePath}"] {e}'
        )


def get_total_lines(myDir:str, extension:str):
    """ Returns: Total lines in all `files.extension` in the `myDir` """
    totalLines = 0
    for rootDir, foldersList, filesList in os.walk(myDir):
        for f in filesList:
            myFile = os.path.join(
                rootDir,
                f
            )
            if myFile.endswith(extension):
                lines = get_lines(
                    myFile
                )
                if lines is None:
                    continue
                totalLines += lines
                print(f'-----> {myFile} ==== {lines}')
    
    return totalLines


def get_inputs() -> tuple[str, str] :
    """ Takes input for `directory-location` and `file-extension`.
    - If `directory-location` not passed, current dir path will be returned.
    """
    # Directory
    dirPath = input(
        '> Enter the directory location (press enter for current dir): '
    ) or os.getcwd()

    # File Type
    fileExt = input(
        '> Enter file extension (ex: txt OR press enter for all files): '
    )
    
    return (
        dirPath,
        fileExt
    )
    
    



if __name__ == "__main__":
    os.system('title Calculate Number of lines')                                                      # Set Title
    while True:
        try:
            dirPath, fileExt = get_inputs()                                                           # Directory & File type
            linesNum = get_total_lines(
                dirPath, 
                fileExt
            )                                                                                         # Main Function
        except Exception as e:  
            print(f'[Program Error] {e}')
        else:                   
            print(f'\n\nTotal lines in all ".{fileExt}" files of "{dirPath}" = {linesNum}')           # Output
        finally:                
            print('\n\n\n\n')

