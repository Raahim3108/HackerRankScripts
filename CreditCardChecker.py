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
