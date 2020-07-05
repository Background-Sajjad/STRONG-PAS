"""Coded by Background-Sajjad  (Sajjad)"""
import os
change=(("S","$"),("a","@"),("s","5"),("j","J"),("i","!"),("and","&"),("123","321"),("y","Y"),("o","0"),("(","["),(")","]"),("A","4"),("T","7"),(" ","_"),("e","E"),("I","!!"),(".","?"))
os.system("clear") 
print("""\033[1;91m
	 ____ ___ ____ ____ _  _ ____    ___  ____ ____ 
	 [__   |  |__/ |  | |\ | | __ __ |__] |__| [__  
	 ___]  |  |  \ |__| | \| |__]    |    |  | ___] 
	""")                                                         
print("\t    \033[1;0;104m	 >>> [Coded by Sajjad] <<<","\033[1;0;0m")
  
print("   \033[1;0;101m:: github: https://www.github.com/Background-Sajjad ::","\033[1;0;0;m")        
  
print("""\033[0;92m""")

print("")
print("")
while(True):
    def secure(password):
        for a,b in change:
            password=password.replace(a,b)
            
        return password
    if __name__=="__main__":
         password=input("\n\033[1;96m Enter you password:")
         print(" ")
         password=secure(password)
         print(" \n\033[1;92m Your strong password is: ",password)
         print(" ")
         a=input("\n\033[1;94m Do you want to continue [y/n]:").lower()
         print("\033[0m")
         if(a!="y"):
             break
             
            
         
             
                 
             
         
    
           
    
        
