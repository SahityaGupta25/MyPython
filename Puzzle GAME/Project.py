import random 
def main():
    score=0
    words=['MOTORCYCLE','MOBILE','AIRPLANE']
    words=random.sample(words,k=len(words))
    
    for word in words:
        score=printpuzzlequestion(word,score)
   
    print('Your Score is =',score)
# ----------------------------------------
def shuffleword(wrd):
    pw=random.sample(wrd,k=len(wrd))
    return ''.join(pw)
# -----------------------------------------
def printpuzzlequestion(word,score):
    problemword=shuffleword(word)
    print("\nArrange the word ")
    print(problemword)
    userword=input()
    print()
    if userword.upper()==word:
        print("Correct")
        score+=1
    else:
        print('Incorrect')
        score-=1
    return score
main()