while True:

   while True:  

      try:

         nmb1 = float(input("entre nember 1 : "))
         break

      except ValueError:
         print("invalid input. please enter a numric value : ") 

   while True:
      try:
         operation = input("entre operation type : ")
         if operation in ("+", "*", "-", "/", "%"):
            break
         else:
            raise ValueError
      except ValueError:
          print("invalide operator , please enter +, -, /, %, * ")

   while True:
      try:
         nmb2 = float(input("entre nember 2 : "))
         if nmb2 != 0:
           break
         else:
            raise ValueError
      except ValueError:         
         print("invalid input. please enter a numric value! ") 

   if operation == "+":
      result = nmb1 + nmb2

   elif operation == "-":
     result = nmb1 - nmb2

   elif operation == "*":
      result = nmb1 * nmb2
     
   
   if operation == "/":      
         result = nmb1 / nmb2 
   
   
   if operation == "%":
      result = nmb1 % nmb2          

   if result != None:
      print("resalt is : ",result)
   else:
      result = None

   
   
   print(result)    
   
   repeat = input("do you to perform another operation (y:n) : ")
   if repeat == "n":
      break
      
print("program exited")