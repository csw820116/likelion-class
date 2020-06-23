
word1 = input("끝말잇기를 시작합니다 : ")

if (len(word1) == 3) :
    
    while True:
    
        word2 = input()
        
    
        if (len(word2) ==3) and ((word2[0]) == word1[2]):
            print("정답입니다")
            
        else:
            
            print("오답입니다")
            break
    
else:
    print("오답입니다")
    
print("게임이 끝났습니다")
    
