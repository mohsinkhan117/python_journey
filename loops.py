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


#loops on strings 
#they use the index of the string 

a= "Mohsin khan"
for i in range(0,len(a)):
    print(a[i])