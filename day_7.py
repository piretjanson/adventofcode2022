import re


def create_new_dir_object(path_name):
    return {
        "name": path_name,
        "size": 0,
        "subdirs": []
    }


root = create_new_dir_object('/')

current_dir = root


def create_new_subdir(path_name):
    global current_dir
    new_dir = create_new_dir_object(path_name)
    current_dir.setdefault('subdirs', []).append(new_dir)
    return new_dir


def change_to_new_directory(path_name):
    global current_dir
    new_dir = create_new_subdir(path_name)
    current_dir = new_dir


def swich_to_subdir(path_name):
    global current_dir
    existing_subdir = list(filter(lambda x: x['name'] == path_name, current_dir['subdirs']))
    if len(existing_subdir) == 1:
        current_dir = existing_subdir[0]
    else:
        change_to_new_directory(path_name)


def find_parent(parent, current):
    if current in parent['subdirs']:
        return parent

    for subdir in parent['subdirs']:
        nested_parent = find_parent(subdir, current)
        if nested_parent:
            return nested_parent


def set_new_path(command):
    global current_dir
    global root
    path_name = command[2:].strip()
    if path_name == '/':
        current_dir = root
    elif path_name == '..':
        if current_dir['name'] == '/':
            return
        parent = find_parent(root, current_dir)
        current_dir = parent
    else:
        swich_to_subdir(path_name)


def add_size_to_parents(size):
    global root
    global current_dir
    parent = find_parent(root, current_dir)
    parent['size'] += size
    while parent['name'] != '/':
        parent = find_parent(root, parent)
        parent['size'] += size


def calculate_directories_sizes(lines):
    global current_dir
    global root
    for line in lines:
        if line.startswith('$'):
            command = line[2:].strip()
            if command.startswith('cd'):
                set_new_path(command)
        else:
            if line.startswith('dir'):
                path_name = line[4:].strip()
                create_new_subdir(path_name)
            else:
                match = re.search('([0-9]+) .*', line)
                size = list(map(int, match.groups()))[0]
                current_dir['size'] += size
                if current_dir['name'] != '/':
                    add_size_to_parents(size)


def map_directoris_sizes(dir, size, smaller):
    sizes = []
    if smaller and dir['size'] < size:
        sizes.append(dir['size'])
    elif not smaller and dir['size'] >= size:
        sizes.append(dir['size'])

    if 'subdirs' in dir:
        for sub in dir['subdirs']:
            sub_sizes = map_directoris_sizes(sub, size, smaller)
            sizes.extend(sub_sizes)

    return sizes


def find_dir_to_delete():
    global root
    disk_space = 70000000
    total_space_needed = 30000000
    need_to_free = total_space_needed - (disk_space - root['size'])
    return map_directoris_sizes(root, need_to_free, False)


def process_command_lines(lines, part1):
    global root
    calculate_directories_sizes(lines)

    if (part1):
        sizes = map_directoris_sizes(root, 100000, True)
        return sum(sizes)

    sizes2 = find_dir_to_delete()
    return sorted(sizes2)[0]


def reset_globals():
    global root
    root = create_new_dir_object('/')
    global current_dir
    current_dir = root


with open("resources/commands_output.txt", "r") as f:
    print('Part 1:')
    print(process_command_lines(f.readlines(), True))
    f.seek(0)
    reset_globals()
    print('Part 2:')
    print(process_command_lines(f.readlines(), False))
