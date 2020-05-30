def n_gram(s,n):
    return [s[i:i+n] for i in range(len(s)-n+1)]

if __name__ == "__main__":
    a="paraparaparadise"
    b="paragraph"
    X=n_gram(a,2)
    Y=n_gram(b,2)
    union=set(X)|set(Y)
    intersection=set(X)&set(Y)
    X_Y=set(X)-set(Y)
    Y_X=set(Y)-set(X)
    print("和集合", union)
    print("積集合", intersection)
    print("差集合 X-Y", X_Y)
    print("差集合 Y-X", Y_X)
    print(a,"にseが含まれているか",{"se" in a})
    print(b,"にseが含まれているか",{"se" in b})
    """
    和集合 {'di', 'ad', 'ph', 'ag', 'gr', 'ra', 'pa', 'is', 'se', 'ar', 'ap'}
積集合 {'ra', 'ar', 'pa', 'ap'}
差集合 X-Y {'se', 'ad', 'is', 'di'}
差集合 Y-X {'ph', 'ag', 'gr'}
paraparaparadise にseが含まれているか {True}
paragraph にseが含まれているか {False}
"""