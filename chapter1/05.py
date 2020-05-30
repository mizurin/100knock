def n_gram(s,n):
    return [s[i:i+n] for i in range(len(s)-n+1)]

if __name__ == "__main__":
    a="I am an NLPer"

    print("単語 bi-gram")
    print(n_gram(a.split(),2))
    
    print("文字 bi-gram")
    print(n_gram(a,2))

"""
単語 bi-gram
[['I', 'am'], ['am', 'an'], ['an', 'NLPer']]
文字 bi-gram
['I ', ' a', 'am', 'm ', ' a', 'an', 'n ', ' N', 'NL', 'LP', 'Pe', 'er']
"""