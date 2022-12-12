from functions import text_parser

class directory:
    def __init__(self, path):
        self.path = path
        self.child_dirs = {}
        self.files = {}
        self.total_size = 0
    
    def add_child_dir(self, child_dir):
        self.child_dirs[child_dir.path] = child_dir
    
    def add_file(self, file):
        self.files[file.path] = file
        self.total_size += file.size

    def get_size(self):
        self.total_size = 0
        for child_dir in self.child_dirs:
            child_dir.get_size()
            self.total_size += child_dir.total_size
        for file in self.files.values():
            self.total_size += file.size

class file:
    def __init__(self, path, size):
        self.path = path
        self.size = size

if __name__ == '__main__':
    raw_data = text_parser('day7.txt')
    
    # part 1
    current_dir = '/'
    all_dirs = {'/':directory(current_dir)}

    for line in raw_data:
        if line == '$ cd /':
            continue
        
        print("\n", line)
        line = line.split()
        # check for $ which changes location in file structure
        if line[0] == '$':
            if line[1] == 'cd':
                print('before cd', current_dir)
                if line[2] == '..':
                    current_dir = '/'.join(current_dir.split('/')[:-2])+'/'
                else:
                    current_dir += line[2]+'/'
                print('!after cd', current_dir)

        # add directory to current place in file structure
        elif line[0] == 'dir':
            new_dir = current_dir+line[1]+'/'
            if new_dir not in all_dirs:
                print('!found new directory:', new_dir)
                all_dirs[new_dir] = directory(new_dir)

        # add file to current place in file structure
        elif line[0].isdigit():
            f = file(line[1], int(line[0]))
            all_dirs[current_dir].add_file(f)
            print('!found new file:', f.path, f.size, 'added to:', current_dir)

    all_dirs['/'].get_size()

    # for path, dir in all_dirs.items():
    #     print(path, dir.total_size)

    for path, dir in all_dirs.items():
        print(path, dir.total_size, len([d for d in dir.child_dirs]), sum([d.total_size for d in dir.child_dirs]))

    print('\nroot dir size', all_dirs['/'].total_size)

    print("\nsupposed answer", sum([x.total_size for x in all_dirs.values() if x.total_size <= 100000]))