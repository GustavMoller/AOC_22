from functions import text_parser

class directory:
    def __init__(self, path, parent_dir=None):
        self.path = path
        self.parent_dir = parent_dir
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
        for child_dir in self.child_dirs.values():
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
    all_dirs = ['/']
    root_dir = directory('/')
    current_dir = root_dir

    for line in raw_data:
        if line == '$ cd /':
            continue
        
        print("\n", line)
        line = line.split()
        # check for $ which changes location in file structure
        if line[0] == '$':
            if line[1] == 'cd':
                print('before cd', current_dir.path)
                if line[2] == '..':
                    current_dir = current_dir.parent_dir
                else:
                    current_dir = current_dir.child_dirs[current_dir.path+line[2]+'/']
                print('!after cd', current_dir.path)

        # add directory to current place in file structure
        elif line[0] == 'dir':
            new_dir_path = current_dir.path+line[1]+'/'
            if new_dir_path not in current_dir.child_dirs.keys():
                print('!found new directory:', new_dir_path)
                current_dir.add_child_dir(directory(new_dir_path, current_dir))
                all_dirs.append(new_dir_path)

        # add file to current place in file structure
        elif line[0].isdigit():
            f = file(line[1], int(line[0]))
            current_dir.add_file(f)
            print('!found new file:', f.path, f.size, 'added to:', current_dir.path)
    
    # update sizes of all directories
    root_dir.get_size()

    # part 1
    cum_count = 0
    for dir_path in all_dirs:
        dir = root_dir
        for p in dir_path.split('/')[1:-1]:
            dir = dir.child_dirs[dir.path+p+'/']
        if dir.total_size <= 100000:
            cum_count += dir.total_size
    print(cum_count)

    # part 2
    available = 70000000 - root_dir.total_size
    need_to_delete = 30000000 - available
    candidates = []
    for dir_path in all_dirs:
        dir = root_dir
        for p in dir_path.split('/')[1:-1]:
            dir = dir.child_dirs[dir.path+p+'/']
        if dir.total_size > need_to_delete:
            candidates.append(dir.total_size)
    print(min(candidates))