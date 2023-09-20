"""OUTPUT
  A B C D E 
  F G H I J 
  K L M N O 
  P Q R S T 
  U V W X Y 
  Z [ \ ] ^
  """ 



ch="A"
for i in range(1,7):
    for j in range(1,6):
         print(ch,end=" ")
         ch=chr(ord(ch)+1)
    print("")  