#n=input("enter your name:")
#print("helloooo",n)
#
#n=int(input("enter a number to check:"))
#
#l1=["apple","strawberry","kiwi","mango"]
#rint(l1)
#n=int(input("enter a number to add:"))
#a=int(input("enter another number to add:"))
#print(n+a)
message = "hello anjali"
print(message.upper())
V=["a","e","i","o","u","A","E","I","O","U"]
a=0
for i in range(len(message)):
    if message[i] in V:
        a=a+1
    else:        pass
print(a)
print(message[::-1])
same="madam"
if same==same[::-1]:
    print("palindrome")
else:
    print("not palindrome")
print(message.replace(" ","_"))
    
