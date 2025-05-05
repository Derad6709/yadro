import sys


def search_lines(file_path, search_string):
    with open(file_path, 'r') as file:
        for line in file.read().splitlines():
            if search_string in line:
                print(line)


if __name__ == "__main__":
    '''Usage: search_path.py <file_path> <search_string>'''
    file_path = sys.argv[1]
    search_string = sys.argv[2]
    search_lines(file_path, search_string)
