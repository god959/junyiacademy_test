#1. (A.) 請寫一個程式把裡面的字串反過來。
def f1(str1):
    return str1[::-1]

f1("junyiacademy")
#1. (B.) 請寫一個程式把裡面的字串，每個單字本身做反轉，但是單字的順序不變。
def f2(str2):
    words=[]
    for x in str2.split(" "):
        words.append(f2(x))
    return " ".join(words)

f2("flipped class room is important")