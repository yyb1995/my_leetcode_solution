import re
import os

def rename(folder_path='./'):
    # This function is used to rename file name to format like 'num Chinesename.md'
    success, fail, noneed = 0, 0, 0
    for file in os.listdir(folder_path):
        filename, suffix = os.path.splitext(file)
        if suffix == '.md' and filename != 'README':
            with open(file, 'r') as f:
                new_name = re.findall(r'(?<=title:\s)\d+.+', f.read())
            if len(new_name) != 1:
                print('Wrong format: ' + file)
                fail += 1
                continue
            else:
                if filename != new_name[0]:
                    os.rename(file, new_name[0] + suffix)
                    success += 1
                else:
                    noneed += 1
        else:
            noneed += 1

    print('All file rename finish.\nSuccess: {0} Fail: {1} Noneed: {2}'.format(success, fail, noneed))
        

if __name__ == "__main__":
    rename()