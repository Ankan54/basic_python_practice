from math import sqrt

primes=[]
primes.append(2)

for i in range(3,32000,2):
    isPrime=True
    max_val= sqrt(i)+1
    for j in primes:
        if (i%j==0):
            isPrime= False
            break
        if (j>=max_val):
            break
        if isPrime:
            primes.append(i)

testcase= int(input("number of testcases:"))
for t in range(testcase):
    result = []
    M,N = input().split()
    M=int(M)
    N= int(N)
    max_val = sqrt(N) + 1
    if (M < 2):
        M = 2
    isPrime = [True] * 1000001
    for i in primes:
        if (i >= max_val):
            break
        if (i >= M):
            start = i * 2
        else:
            start = M + ((i - M % i) % i)
        false_val = [False] * len(isPrime[start - M:N + 1 - M:i])  # identifying all false values
        isPrime[start - M:N + 1 - M:i] = false_val
    for i in range(M, N + 1):
        if (isPrime[i - M] == True):
            result.append(i)  # finally storing all primes in result String
    if len(result)>0:
        print(max(result)-min(result)) # gives the difference of min and max prime numbers in the range
    else:
        print(-1)
