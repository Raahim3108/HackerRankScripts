def count_substring(string, sub_string):
    c = 0
    for i in range(len(string)):                  #Goes from the beginning of the string and checks the substrings
        if string[i:].startswith(sub_string):     #Startswith functon checks if a string is starting with a particular substring
            c = c+1
    return c
    

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)
