# -*- coding: utf-8 -*-
"""
Created on Thu Dec 28 10:12:39 2023

@author: Raahim
"""


def merge(self, nums1, m, nums2, n):
  
    t = m + n
    hey = []
    for i in (nums1[:m]):
        hey.append(i)
    for i in (nums2[:n]):
        hey.append(i)
    hey.sort()
    nums1[:t] = hey[:t]
    
    print(nums1)
        


merge(merge, [1,2,3,4],4,[6,9,8],3)
#%%
if __name__ == '__main__':
    N = int(input())
    my_list = list()
    for _ in range(1,N+1):
        command = input().split()
        if command[0] == "insert":
            my_list.insert(int(command[1]), int(command[2]))
        elif command[0] == "print":
            print(my_list)
        elif command[0] == "reverse":
            my_list.reverse()
        elif command[0] == "pop":
            my_list.pop()
        elif command[0] == "append":
            my_list.append(int(command[1]))
        elif command[0] == "remove":
            my_list.remove(int(command[1]))
        elif command[0] == "sort":
            my_list = sorted(my_list)
        else:
            print("Wrong command")

    print(my_list)
# %%
def Validate(cc):
    if '-' in cc:
        tokens = cc.split('-')
        if len(tokens) != 4 or any(len(t) != 4 for t in tokens):
            return "Invalid"
        cc = ''.join(tokens)
    for c in set(cc):
        if c*4 in cc:
            return "Invalid"
    if len(cc) == 16 and cc.isdigit() and cc[0] in {'4','5','6'}:
        return "Valid"
    else:
        return "Invalid"
    
    
#print(Validate("4536258796157866"))
if __name__ == "__main__":
    n = int(input())
    for i in range(1,n+1):
        cc = str(input())
        print(Validate(cc))
       
# %%
