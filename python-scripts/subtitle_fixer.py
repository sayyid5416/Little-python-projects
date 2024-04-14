import os
import sys



def save_modified_file(input_file_path, output_file_path):
    with open(input_file_path, 'r') as inputFile:
        # Get data
        inputData = inputFile.read()
        subtitleBlocks = inputData.split('\n\n')
        
        # Modify
        newSubtitleBlocks = []
        newNum = 0
        for block in subtitleBlocks:
            if not block:
                continue
            num, timestamp, text = block.strip().split('\n')
            
            # Remove bracketed subs
            if '(' in text or '{' in text or '[' in text:
                continue
            
            # Remove '-'
            if text.startswith('-'):
                text = text.removeprefix('-')
            
            # ADD Modified subtitle
            newNum += 1
            newSubtitleBlocks.append(
                f'{newNum}\n{timestamp}\n{text.strip()}'
            )
        
        # Save to new file
        with open(output_file_path, 'w') as outputFile:
                outputFile.write(
                    '\n\n'.join(newSubtitleBlocks)
                )


def get_input_file():
    _path = input('> Enter file path (.srt): ')
    _path = _path.strip('"').strip("'")
    if not _path or not _path.lower().endswith('.srt') or not os.path.exists(_path):
        raise ValueError(f'Incorrect Input Path: "{_path}"')
    return _path





if __name__ == "__main__":
    try:
        input_path = get_input_file()
        output_path = input_path.replace('.srt', ' new.srt')
        save_modified_file(input_path, output_path)        
    except Exception as e:
        print(f'\n[FAILURE] {e}')
    else:
        print(f"\n[SUCCESS] Modified subtitle file saved to: {output_path}")
    finally:
        input('\n> Enter to exit')
