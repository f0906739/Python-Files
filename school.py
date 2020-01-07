# def lines(num=int(input("Enter max number: "))):
#     yield [f"{list(reversed(range(1,line+1)))}" for line in reversed(range(1, num+1))]

# print('TEST LIST: ',[f"{list(reversed(range(1,line+1)))}" for line in reversed(range(1, 5+1))])

# for i in lines():
#     for line in i:
#         # print(line)
#         temp = line
#         print(*temp)

# print(*temp)
# print(*"hello sir".upper())


# word = 'hello'
# print(word)
# print(word.index('h'))
# print(word[word.index('h')])
# letter = str(input("Enter letter you want to change: "))
# if letter in word:
#     word = word[:word.index(letter)]+'z' + word[word.index(letter)+1:]
#     print("".join(word))
# else:
#     print('letter not in word. srry')

def find_dups(iterable):
    dups = []
    for index, i in enumerate(sorted(iterable)):
        if index != 0 and i == sorted(iterable)[index-1]:
            if i not in dups:
                dups.append(i)
    return dups


print(find_dups(['a', 'b', 'a']))

import random

def randlist(num):
    opt=list('abcdefghijklmnopqrstuvwxyz')+[1,2,3,4,5,6,7,8,9,0]
    res=[]
    for x in range(num):
        res.append(opt[random.randint(0,len(opt)-1)])
    return res

def dups2(inp):
    catalog={a:inp.count(a) for a in set(inp)}
    dups=[a for a,b in catalog.items() if b>1]
    return dups
random_list=sorted(randlist(100),key=str)
print(dups2(randlist(100)),'\n\n',random_list)
