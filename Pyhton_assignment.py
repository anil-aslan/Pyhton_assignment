number = int(input("How long to continue: "))
a = 0
b = 1  
fibonacci = [a,b]
for i in range(number):
    a,b = b,a+b         #We put b in a, a + b in b
    fibonacci.append(b) #we add it to the list.
print(fibonacci)
