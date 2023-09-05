

def save_to_file(file_content, file):
    with open(file, 'w') as f:
        f.write(file_content)


def read_file(filename):
    with open(filename, 'r') as file:
        return file.read()

