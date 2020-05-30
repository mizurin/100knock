if __name__ == "__main__":
    a="Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
    a=a.replace(".","").replace(",","").split()
    dic={}
    idx=(1,5,6,7,8,9,15,16,19)
    for i,word in enumerate(a,start=1):
        if i in idx:
            dic[word[0:1]]=i
        else:
            dic[word[0:2]]=i
    print(dic)
    """
    {'H': 1, 'He': 2, 'Li': 3, 'Be': 4, 'B': 5, 'C': 6, 'N': 7, 'O': 8, 'F': 9, 'Ne': 10, 'Na': 11, 'Mi': 12, 'Al': 13, 'Si': 14, 'P': 15, 'S': 16, 'Cl': 17, 'Ar': 18, 'K': 19, 'Ca': 20}
    """