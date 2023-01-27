# test score, mid : 50, final : 75

class Score():
    def __init__(self,mid,final):
        self.__mid = mid
        self.__final = final 
    #def __init__ 한줄에 mid,final 각각 선언
    #private 해주기 위해 각 인스턴스에 __ 표시 해주기 (pdf 17,43페이지 참고)
    
    @property
    def mid(self):
        return self.__mid
    @property
    def final(self):
        return self.__final
    #@property 데코레이터 사용해서 숨겨진 변수 mid,final 반환!(46페이지 참고)
    #처음에 한꺼번에 데코레이터를 사용했더니 오류가 났었습니다..

score = Score(50,75)
print(( score.mid + score.final ) / 2 )

#출력 예시
62.5