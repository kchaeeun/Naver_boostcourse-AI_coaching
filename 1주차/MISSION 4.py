
def merge_dict(dict_first, dict_second):
    for sk,sv in dict_second.items():
        if sk in dict_first.keys():
            dict_first[sk]+=sv
        else:
            dict_first[sk]=sv
        
    return dict_first
    

dict_first={'사과':30,'배':15,'감':10,'포도':10}
dict_second={'사과':5,'감':5,'배':15,'귤':25}
print(merge_dict(dict_first, dict_second))
   
        



    