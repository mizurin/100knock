def cipher(s):
    result=""
    for w in s:
        if w.islower():
            w2=chr(219-ord(w))
        else:
            w2=w
        result+=w2
    return result        

if __name__ == "__main__":

    s="I couldn’t believe that I could actually understand what I was reading : the phenomenal power of the human mind ."
    print("元の文")
    print(s)
    print("暗号文")
    print(cipher(s))
    print("暗号文を再度暗号化")
    print(cipher(cipher(s)))

"""
    元の文
I couldn’t believe that I could actually understand what I was reading : the phenomenal power of the human mind .
暗号文
I xlfowm’g yvorvev gszg I xlfow zxgfzoob fmwvihgzmw dszg I dzh ivzwrmt : gsv ksvmlnvmzo kldvi lu gsv sfnzm nrmw .
暗号文を再度暗号化
I couldn’t believe that I could actually understand what I was reading : the phenomenal power of the human mind .
"""