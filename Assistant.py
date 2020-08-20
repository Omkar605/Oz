import os

import pyttsx3



pyttsx3.speak("Welcome to coding World ")
def menu() :
	print("*\tMenu\t*")
	print("	1. OPEN BROWSER\n ")
	print("	2. OPEN TEXT EDITOR\n ")
	print("	3. OPEN MEDIA PLAYER\n ")
	print("	4. SHOW DATE\n ")
	print(" 5. QUIT\n ")

menu()		
		

def editor() :
		print("1.NOTEPAD")
		print("2.WORDPAD")
		print("3.SUBLIME_TEXT")
		print("4.RETURN TO MAIN MENU ")
		

		while True : 
			try :
				pyttsx3.speak("Which Text Editor you want to open  :")
				n = int(input("Which Text Editor you want to open  : "))
				
				if n == 1: 
					os.system("notepad")
					i = input("Enter Anything to return menu : ")
				
					print()
					menu()
					main()
					break
									
				elif n== 2 : 
					os.system("start wordpad")
					i = input("Enter Anything to return menu : ")
					print()
					menu()
					main()		
					break
				elif n == 3 :
					os.system("sublime_text")	
					i = input("Enter Anything to return menu : ")
					print()
					menu()
					main()
					break
				elif n == 4 : 
					
					menu()	
					main()
					break
			
				else :
					print("Invalid Choice!!! \n Enter Between 1 - 5")
					editor()	
					break

			except : 
				print("Must be a Number between 1 - 5")
			
def main() :	
		
	
	while True :
				
		try : 
			pyttsx3.speak("Enter here What you want from me")
			p =int(input("What do you want... : "))
			
			if p == 1: 
				os.system("chrome")
				
				main()
				

			elif p == 2 :
				editor()
				break
				
			elif p == 3 : 
				os.system("wmplayer")
				
				
			elif p == 4 : 
				from datetime import date 
				today = date.today()
				print("Today's date:", today)		
					
					
			elif p == 5 : 
				pyttsx3.speak("Thanks for Visiting us ")
				break
			else :
				pyttsx3.speak("Invalid Choice")
				print("Invalid Option \n Enter Valid Choice...!")
				main()	
				break
			
		except : 
			print("Invalid choice...! \n Must be a Number Between 1 - 5")
			main()
			break

			

main()				

	
			
