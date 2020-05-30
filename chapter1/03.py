import re
def count_word_length(s):
    a=s.replace(".","").replace(",","").split()
    b=[len(i) for i in a]
    return b
if __name__ == "__main__":
    a="Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
    b=count_word_length(a)
    print(b)
    
    """
    [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 8, 9, 7, 9]
    """