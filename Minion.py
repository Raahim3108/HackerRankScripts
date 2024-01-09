def minion(s):
    a,b,n = 0,0,len(s)
    for i in range(n):
        if s[i] in "AEIOU" or s[i] in "aeiou":
            a = a + n-i
            print("For " +s[i]+" , a is " +str(a))
        else:
            b = b + n-i
            print("For "+ s[i] +" , b is "+ str(b))
    
    print(f'Kevin {a}' if a>b else f'Stuart {b}' if a!=b else 'Draw')
    

if __name__ == '__main__':
    s = input()
    minion(s)