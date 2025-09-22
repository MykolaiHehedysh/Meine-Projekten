#Das ist ein Milchautomat, dass man fortsetzen/stoppen kann. 
#Im Prinzip kann man maximal 1,5L Milch bekommen 




a = 0 
b = 1500 
is_running = False
user = input ("Push botton 'start' to continue !")
if user == "start":
  is_running = True
  print ("the milk runs!")
  
while is_running and a<= b:
    a+= 10
    print (f' {a}')

    if a >= 1500:
       print ("You finished")
       break
    user_2 = input ("\n you can stop the process!")
    if user_2 == "stop":
      is_running = False
      print("You stopped the process!")
    else:
       input("Press Enter to continue...")  

    if a == 1500:
      print ("You finished")
      break
      


          
