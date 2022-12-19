# 6. Create a generator to produce first n prime numbers




def prime_no(num):
    for num in range(2, num+ 1):
            for i in range(2, num):
                if (num % i) == 0:
                    break
                else:
                    yield(num)
prime_no(10)

for x in prime_no(int(input("Enter a Number\t"))):
     print(x,end=' ')


