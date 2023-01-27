#1
num_list=[1,5,7,15,16,22,28,29]
def get_odd_num(num_list):
    num2_list=[]
    for i in num_list:
        if i%2==1:
            num2_list.append(i)
    return num2_list

print(get_odd_num(num_list))

#2
num_list=[1,5,7,15,16,22,28,29]
def get_odd_num(num_list):
    temp_list=num_list.copy()
    for i in num_list:
        if i%2==0:
            temp_list.remove(i)
    return temp_list

print(get_odd_num(num_list)) 
    
#3
num_list=[1,5,7,15,16,22,28,29]
def get_odd_num(num_list): 
    result=[i for i in num_list if i%2==1]
    # for,if문의 값이 리스트 i에 자동저장
    return result

print(get_odd_num(num_list)) 

