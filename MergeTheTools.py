def merge_the_tools(string, k):
    # your code goes here
    j=0
    arr = []
    for i in range(0,len(string),k):
        arr.append(string[j:j+k])
        j+=k
    
    
    for i in range(len(arr)):
        ch = arr[i]
        for j in range(len(ch)):
            print(ch[j])

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
