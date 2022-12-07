class Directory:
    def __init__(self, parent=None):
        self.parent = parent
        self.directories = dict()  # name: pointer
        self.files = dict()  # name: size

    def size(self):
        return sum(v for k, v in self.files.items()) + sum(v.size() for k, v in self.directories.items())

    def find_seq_100k(self):
        s = 0
        if self.size() <= 100000:
            s += self.size()
        for k, v in self.directories.items():
            s += v.find_seq_100k()
        return s


root = Directory()
current_folder = None

lines = [l.strip() for l in open('input.txt').readlines()]
for line in lines:
    if line.startswith("$ cd "):
        enter = line.split(' ')[-1]
        if enter == '/':
            current_folder = root
        elif enter == '..':
            current_folder = current_folder.parent
        else:
            if enter not in current_folder.directories.keys():
                current_folder.directories[enter] = Directory(parent=current_folder)
            current_folder = current_folder.directories[enter]
    elif line.startswith("$ ls"):
        continue
    elif line.startswith("dir"):
        folder = line.split(' ')[-1]
        if folder not in current_folder.directories.keys():
            current_folder.directories[folder] = Directory(parent=current_folder)
    else:
        size, name = line.split(" ")
        current_folder.files[name] = int(size)

print(root.find_seq_100k())
