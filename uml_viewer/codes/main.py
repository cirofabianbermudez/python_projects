import yaml

def load_yaml(file_path):
    with open(file_path, 'r') as file:
        data = yaml.safe_load(file)
    return data

def print_tree(map, prefix):

    item_prefix = prefix + "├── "
    sub_prefix  = prefix + "│   "

    lenght = len(map.values());
    # print(lenght)
    counter = 1   

    for key, value in map.items():

        if counter == lenght:
            sub_prefix  = prefix + "    "
            item_prefix = prefix + "└── "
            print(item_prefix + key)
        else:
            print(item_prefix + key)
            counter = counter + 1

        if value is not None:
            print_tree(value, sub_prefix)

if __name__ == "__main__":
    file_path = 'uvm_class_tree.yml'
    data = load_yaml(file_path);
    print_tree(data, "")





