#WAPP TO CONVERT LIST INTO DICTIONARY
#list=[Naina,kimi,sheena]
#list2=[8523,7853,4521]
def list_to_dic():
    keys=[1,2,3]
    values={"one","two","three"}
    result=dict(zip(keys,values))
    print("Dictionary is : ",result)
list_to_dic()