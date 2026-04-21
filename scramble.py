# word scramble   
 
words =['python','javascript','java','automation','pytest','guvi','selenium']
print(len(words))

scramble="tpircsjava"
originalword=words[1]

for i in range(7):
 uservalue = input("Enter the string")

 if originalword == uservalue:
   
   print("Player guess correct")
   break
 else:
  print("Player guess wrong")
  

