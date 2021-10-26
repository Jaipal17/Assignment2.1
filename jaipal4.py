#ASSIGNMENT 2.1

#METHODS OF DICTIONARY 

#CLEAR
# a={
#  "jai":"1",
#  "John":"2",
#  "jerry":"3"
#  }

# a.clear()
# print(a) 

#COPY
# a={
#     "jai":"1",
#     "john":"2"
# }
# b=a.copy()
# print(b)

#FROMKEYS
# a=("key1","key2","key3")
# b=0,1,2
# thisdict=dict.fromkeys(a,b)
# print(thisdict)

#GET
# a={
#     "jai":"1",
#     "john":"2"
# }
# b=a.get("jai")
# print(b)

#ITEMS
# a={
#     "jai":"1",
#     "john":"2"
# }
# b=a.items()
# print(b)

#KEYS
# a={
#     "jai":"1",
#     "john":"2"
# }
# b=a.keys()
# print(b)

#POP
# a={
#     "jai":"1",
#     "john":"2"
# }
# a.pop("jai")
# print(a)

#POPITEM
# a={
#     "jai":"1",
#     "john":"2"
# }
# a.popitem()
# print(a)

#SETDEFAULT
# a={
#     "jai":"1",
#     "john":"2"
# }
# b=a.setdefault("jai")
# print(b)

#UPDATE
# a={
#     "jai":"1",
#     "john":"2"
# }
# a.update({"jerry" : "3"})
# print(a)

#VALUES
# a={
#     "jai":"1",
#     "john":"2"
# }
# b=a.values()
# print(b)

#SETS

#ADD
# a={"1","2","34"}
# a.add("5")
# print(a)

#CLEAR
# a={1,2,34}
# a.clear()
# print(a)

#COPY
# a={"jai","john","jerry"}
# b=a.copy()
# print(b)

#DIFFERENCE
# a={"jai","hop","jyg"}
# b={"jai","jhb","jbk"}
# c=b.difference(a)
# print(c)

#DIFFERENCE UPDATE
# a={"jai","john","jerry"}
# b={"jay","jai","joy"}
# a.difference_update(b)
# print(a)

#DISCARD
# a={"jai","john","jerry"}
# a.discard("jai")
# print(a)

#INTERSECTION
# a={"jai","john","jerry"}
# b={"joy","jay","jai"}
# c=a.intersection(b)
# print(c)

#INTERSECTION UPDATE
# a={"jai","john","jerry"}
# b={"jai","jay","jou"}
# a.intersection_update(b)
# print(a)

#ISDISJOINT
# a={"jai","jau","jay"}
# b={"jou","joy","jnb"}
# c=a.isdisjoint(b)
# print(c)

#ISSUBSET
# a={"jai","joy","jap"}
# b={"joy","jaz","john","jap","jai"}
# c=a.issubset(b)
# print(c)

#ISSUPERSET
# a={"kas","kaz","kan"}
# b={"jai","kan","kaz"}
# c=a.issuperset(b)
# print(c)

#POP
# a={"jai","john","jay"}
# a.pop()
# print(a)

#REMOVE
# a={"jai","john","jerry"}
# a.remove("jai")
# print(a)

#SYMMETRIC DIFFERENCE
# a={"jai","john","jerry"}
# b={"jai","jnm","jbl"}
# c=a.symmetric_difference(b)
# print(c)

#SYMMETRIC DIFFERENCE UPDATE
# a={"jai","john","jerry"}
# b={"joy","jai","jan"}
# a.symmetric_difference_update(b)
# print(a)

#UNION
# a={"jai","john","jerry"}
# b={"jnb","jai","john","jknl"}
# c=a.union(b)
# print(c)

#UPDATE
# a={"jai","john","jerry"}
# b={"jan","jnlm","jkl"}
# a.update(b)
# print(a)

#STEP FUNCTION(FOR LOOP)

# for x in range(0,10):
#     print(x)

# for x in range(-5,0):
#     print(x)

# list=[1,2,3,4,56,7,8,88]
# for x in range(0,len(list)):
#     print(x)

# l=[1,2,3,4,5,6,7,88]
# for x in range(0,l[7]):
#     print(x)

# a=int(input("enter value:"))
# l=[1,2,34,5,6,78,98]
# for x in range(0,len(l),a):
#     print(x)

#TRIANGLE PATTERN(FOR LOOP)
# num=int(input("Enter the number of rows"))
# for i in range(0,num):
#     for j in range(0,num-i-1):
#         print(end=" ")
#     for j in range(0,i+1):
#         print("*",end=" ")
#     print()  

#CHANGE VALUE IN TUPLE
# a=("jai","jou","jan")
# b=list(a)
# b[1] = "jay"
# a = tuple(b)
# print(a)

#CHANGE VALUE OF A KEY
# a={
#     "jai":"1",
#     "john":"2"
# }
# a["jai"]="2"
# print(a)


     
