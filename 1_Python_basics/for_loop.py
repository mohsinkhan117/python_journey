#range(start, stop, step) stop is exclusive 
for i in range(1,20,2): #20 is exclusive, ie if you cannot print 20 , you will have to go upto 21 then you can get 20
    print(i)

print("--------- second loop ------------")
for x in range(-15,21,3):
    print(x)


print("--------- table loop ------------")

n =int (input("Enter a number to get its table: "))
for t in range(n,(n*10)+1,n):
    print(t)

print("--------- string loop ------------")
#loops on strings 
#they use the index of the string 

a= "Mohsin khan"
for i in range(0,len(a)):
    print(a[i], end=" ")
print(end='\n')
print("---------strings through char  loop ------------")
# loops can iterated directly on the char of a string 

for i in a:
    print(i, end=" ")


print("---break, continue, else -----")

for i in range(1,21,1):
    if  i%5 == 0:
        continue
    else :
     print(i)

for i in range(1, 21, 1):
    if i % 5 == 0:
        print(f"Breaking at {i}")
        break  # Break occurs at i=5
    else:
        print(i, end=" ")
else:
    print("\n[ELSE runs only if NO break occurred]")


# VERSION 2: Using break but else still runs (break never triggers)
print("\n---Break never triggers---")
for i in range(1, 21, 1):
    if i > 100:  # This condition is NEVER true
        break
    else:
        print(i, end=" ")
else:
    print("\n✅ else ran because break never happened")