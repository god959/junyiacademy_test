#請寫一個程式,Input 是一個數字,Output 是從 1 到這個數字,扣除掉所有 3 的倍數以及 5 的倍數,但是需要保留同時是 3 和 5 的倍數的總數字數。
def f(n):
    count=0
    for i in range(1,n+1):
        if (i%3!=0 and i%5!=0) or (i%(3*5)==0):
            count+=1
    return count
f(15)