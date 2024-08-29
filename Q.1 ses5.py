n=int(input('please enter your number: '))
fib=[0,1]


for i in range(2,n):
  x=fib[i-1]+fib[i-2]
  fib.append(x)

print('your fibonacci number is:',fib[n-1])


