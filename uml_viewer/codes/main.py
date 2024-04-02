import yaml

def load_yaml(file_path):
    with open(file_path, 'r') as file:
        data = yaml.safe_load(file)
    return data

def print_hierarchy(dictionary, parent='', indent=0):
    if parent:
        print(' ' * indent + parent)
    if parent in dictionary:
        for child in dictionary[parent][0]['inherits']:
            print_hierarchy(dictionary, child, indent + 4)

if __name__ == "__main__":
    file_path = 'uvm_class_tree.yml'
    data = load_yaml(file_path);

    for key, value in data.items():
        print( key + ": " + str(value))

    print_hierarchy(data)

