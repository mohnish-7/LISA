

import time 
from text_to_speech import Voice_out as speak
import pickle
from colorama import init,Fore,Style
init()
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

class User :

	def __init__(self,f_name=None,u_name=None,password=None) :

		self.f_name = f_name
		self.u_name = u_name
		self.password = password

	def __str__(self) :

		return 'Current user is '+self.name

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# To Clear the Screen
def clean_slate() :

	from os import system
	__clean__ = system('cls')

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# To Align The Output
align = '\n'*15 

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

def check(l,s):

	flag = False
	for word in l:

		if word in s:

			return True

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

def getPass() :

	import getch
	ft = True
	password =''
	
	while True :
		
		x = getch.getch()
		x = x.decode('utf-8')


		if x == '\r' or x == '\n' :
			
			break

		else:
			
			print('*',end='',flush=True)
			password += x

	return password

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

def file_save(obj,fname,mod='wb') : 
	
	with open(fname,mod) as fw : 

		pickle.dump(obj,fw,pickle.HIGHEST_PROTOCOL)

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

def file_load(obj,fname) :

    fr = open(fname,'rb')
    obj = pickle.load(fr)
    return obj

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>


def signup() :

	clean_slate()
	print(align+':)'.center(130))
	speak('Alright then ! Lets get you started !')

	clean_slate()

	print(align+'Your full name -->   '.rjust(70),end='')
	f_name = input()
	clean_slate()

	print(align+'Set a new Username -->   '.rjust(70),end='')
	u_name = input()
	clean_slate()

	print(align+'Set a new Password -->   '.rjust(68),end='')
	u_pass = getPass()
	clean_slate()

	print(align+'Creating a new User...'.center(130))
	time.sleep(2)
	clean_slate()

	try:	
		admin = User(f_name,u_name,u_pass)
		file_save(admin,'User_data.pkl')
		
		speak(' New user creation successfull !')
		
	
	except :
		speak(' Some error occured ! ')
	

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

def login() :

	clean_slate()
	speak('You need to log in access LISA ! ')
	
	while True :

		clean_slate()
		print(align+'Login ? '.center(130))
		ans = input('\n'.center(125))



		if ans.lower() in 'yes okay alright yup yea ok' :

			clean_slate()
			speak(' Enter your log in credentials. ')

			while True :

				clean_slate()
				
				print(align+'Username -->   '.rjust(70),end='')
				un = input()
				print('Password -->   '.rjust(70),end='')
				ps = getPass()
				clean_slate()

				adm = User()
				adm = file_load(adm,'User_data.pkl')

				if adm.u_name == un and adm.password == ps :

					print(align+'Loging in...'.center(130))
					time.sleep(3)
					clean_slate()
			
					print(align+':)'.center(130))

					speak(' Access Granted ! ')
					time.sleep(5)

					return True 			



				else :

					print(align+'Loging in...'.center(130))
					time.sleep(3)
					speak('Uh oh ! Wrong Password.')
					clean_slate()
					print(align+' Try Again ? '.center(125))
					a = input('\n'.center(120))

					if a in 'yes okay ok yea yup':
						continue
					else:
						return False 			



		elif ans.lower() in 'no nope nah ' :
			
			clean_slate()
			return False

		else :

			speak('Invalid response. Try again !')
			continue 			

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>		
	
def intro() :

	import misc_methods as mm 
	import time
	mm.clean_slate()
	print('\n'*5+Fore.YELLOW+'''                                                                    

			                                                                                            
		                                                                                                       		 											                                                                                                      
	     *                                *               *  *  *  *  *  *  *  *                      *  *  *                                                                         
	     *                                *             *                                            *       *                                                                      
	     *                                *             *                                           *         *                                                                     
	     *                                *               *  *  *  *  *  *  *  *                   *  *  *  *  *                                                                  
	     *                                *                                      *                *             *                                                               
	     *                                *                                      *               *               *                                                                  
	     *  *  *  *  *  *  *              *              *  *   *  *  *  *  *  *                *                 *''',end='')

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>		
	
def choice(s=' ') :

	while True :

		clean_slate()
		print(align+s.center(130))
		a = input('\n'.center(125))
		if a in 'yes yea s ok alright yep yup no nah nope' :
			return a
		else :
			speak('Invalid response . Try again !')
			continue

#choice('enter :')
