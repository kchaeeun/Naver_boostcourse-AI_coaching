score=[(100,100),(95,90),(55,60),(75,80),(70,70)]

def get_avg(score):
    index=0
    for x,y in score:
        avg=(x+y)/2
        index +=1
        print(f'{index}번, 평균 : {avg}')

get_avg(score)
    