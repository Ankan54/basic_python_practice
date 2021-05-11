#!/usr/bin/env python
def find_binary(decimal):
    binary_list = ""
    while decimal>0:
        binary_list+=str(decimal%2)
        decimal= decimal//2
    return str(binary_list)[::-1].rjust(32,"0")

def twos_complement(result):
    ones= ""
    for i in result:
        ones+=("0" if i=="1" else "1")
    twos= int(ones,2)+1
    twos= bin(twos)
    return str(twos[2:])

inputnum = input().strip()
inputlist= inputnum.split()
inputlist= [int(i) for i in inputlist]
output=""
for decimal in inputlist:
    count=0
    result= find_binary(abs(decimal))
    if decimal<0:
      result = twos_complement(result)
    for i in result:
        if i=="1":
            count+=1
    output+=str(count)+" "

print(output.strip())
