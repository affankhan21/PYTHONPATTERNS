#OUTPUT : A B C D E 
#         A B C D E
#         A B C D E
#         A B C D E
#         A B C D E

ch="A"
for i in range(1,6):
    for j in range(1,6):
         print(ch,end=" ")
         ch=chr(ord(ch)+1)
print("\n")  