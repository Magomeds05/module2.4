numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
#Создайте пустые списки primes и not_primes.
primes =  []
not_primes = []
for i in numbers: #При помощи цикла for переберите список numbers.
    for i in range(len(numbers)):
        print(i)








#from functools import reduce
#n = 16 # Простые числа до 16
#primes = reduce(lambda r, x: r - set(range(x**2, n, x)) if x in r else r, range(2, int(n**0.5) + 1), set(range(2, n)))
#print(primes)











