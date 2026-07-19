a = input()
if("@" in a[0]):
    if(5<len(a)<=15):
        if(a[1:].isalnum()):
                print("Correct")
        else:
            print("Incorrect")
    else:
        print("Incorrect")
        
      
 

else:
    print("Incorrect")
