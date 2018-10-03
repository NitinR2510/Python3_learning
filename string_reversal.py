#the program accepts number oof characters in strings, the string... and then reverses it as output.
a = eval(input())  #specifies the number of characters to be entered in the string or number to be reversed
b = input()   #the actual string that has to undergo reversion. It may be a number as well.
c = a-1
d = ''
while c>=0:
    print(b[c],end='')
    c -=1
