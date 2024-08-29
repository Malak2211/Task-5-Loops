
prime_number = int(input("Print prime numbers till number:  "))
prime=[]
for p in range(2, prime_number+1):
    for i in range(2, p):
        if p % i == 0:
            break
    else:
        prime.append(p)
     
          
print (prime)




