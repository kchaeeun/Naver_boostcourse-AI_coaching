def find_string(inputs):
    word=""
    for i in inputs:
        if i.isdigit():
            word+=" "
        else:
            word+=i
    return word.split("  ")
    

inputs="cat32dog16cow5"

string_list = find_string(inputs)
print(string_list)
    


