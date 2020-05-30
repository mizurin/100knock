import random

def Typoglycemia(s):
    if len(s)<=4:
        return s
    else:
        word=s[1:-1]
        word=("".join(random.sample(list(word),len(word))))
        word=s[0]+word+s[-1]
        return word

if __name__ == "__main__":
    a="I couldn’t believe that I could actually understand what I was reading : the phenomenal power of the human mind ."
    a=a.replace(".","").replace(":","").split()
    for word in a:
        print(Typoglycemia(word))