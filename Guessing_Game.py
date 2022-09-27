# 猜數字遊戲
# 遊戲會隨機產生0~99的數字,如果猜錯會提示是否猜得太高或太低,直到猜中答案為止

from random import randint

answer = randint(0, 99)
#print(answer)

def guess_number():
    times = 0
    runnig = True

    while runnig:
        guess_number = int(input('please guess a number between 0 to 99: '))
        if guess_number > answer:
            print("It's too large!")
            times += 1
        elif guess_number < answer:
            print("It's too small!")
            times += 1
        else:
            print("You guess the answer!")
            runnig = False
            times += 1
    print('You guess '+ str(times)+ " times")

guess_number()