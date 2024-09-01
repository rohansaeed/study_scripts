#!python3

dictionary = {
        "key 1":"value 1",
        "key 2":"value 2"
        }


def print_dict1(diction):
    print(diction.items())
    print(diction)
    print(' '.join(diction))
    
def print_dict2(diction):
    for key, value in diction.items():
        print(key + ": " + value)
    
    


print_dict1(dictionary)
print_dict2(dictionary)