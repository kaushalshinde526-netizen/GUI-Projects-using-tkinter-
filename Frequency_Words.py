#WAPP to count the frequency of each word in a given string.
def feq_words():
    str=input("Enter a string : ")
    li=str.split()
    d={}
    for i in li:
        if i in d:
            d[i]=d[i]+1
        else:
            d[i]=1
    print("Frequency of each word is : ",d)
feq_words()