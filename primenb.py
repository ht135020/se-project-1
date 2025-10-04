#check if nb is prime or not
nb = input("Enter a number: ")
nb = int(nb)
i=1
counter = 1
for i in range(1,nb // 2):
    if nb%i == 0:
        counter+=1

if counter > 1:
    print(nb, "is not prime")
else:       
    print(nb, "is prime")
