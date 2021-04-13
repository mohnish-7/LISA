#***********************************************************************************************************************************************************



#														Logically Interactive Software Algorithm (LISA)



#***********************************************************************************************************************************************************

#############################################################################################################################################################

# 																LISA's Frontend Functions

#############################################################################################################################################################

version = 3.0

import time 
import os
import playsound
from speech_to_text import Voice_in as listen
from text_to_speech import Voice_out as speak
from misc_methods import clean_slate,getPass,login,intro,check
from misc_methods import align,signup,file_load,file_save
import pickle,random
import logic_module as l
from misc_methods import User
from colorama import init,Fore,Style
from misc_methods import check

access = True
log = True

gbl = ['OK! See you later then. BYE ! ','Alright then ! Talk to you later !','So long....','See you later...','Bye','Goodbye','Until next time..']

init()

clean_slate()

time.sleep(1)

playsound.playsound('Tones/Intro.mp3',block=False)

time.sleep(2.9)

intro()

for i in range(25):

	intro()
	time.sleep(0.003)
	clean_slate()
	time.sleep(0.003)
clean_slate()
time.sleep(0.3)
intro()
time.sleep(1.4)
print('\b'+str(version),end=' ')
time.sleep(5)


class User_Count :

	def __init__(self,count=0):

		self.count = count


   

while log == True :

	try :
		
		ucf = open('User_count.pkl','rb')
		ucf = pickle.load(ucf)
    
  

	except  :

		ucf = User_Count()
		file_save(ucf,'User_count.pkl')
	
	if ucf.count == 0 :

		clean_slate()
		speak('No user data found ! Do you want to sign-up ? ')
			
		while True :

			clean_slate()
			print(align+' Sign Up ? '.center(130))
			ans = input('\n'.center(123))
			
			if ans.lower() in 's yes ok alright go ahead yup yea yep' :

				signup()
			
				ucf.count += 1
				file_save(ucf,'User_count.pkl')
				break

						

			elif ans.lower() in 'no nah nope' : 

				os.unlink('User_count.pkl')
				log = False
				break
				

			else :

				speak('Invalid response. try again !')
				continue

		

	else :
			access = login()
			
			break

if access == True and log == True :

	active = True
	clean_slate()
	print('\n'*15+Fore.YELLOW+':)'.center(132))
	l.greet()
	
	clean_slate()

	l.menu()

	speak('What can I do for you ?!')

	while active :
		
		cmd = listen()
		cmd = cmd.lower()

		print(align+':)'.center(130))

		

		if check(['bye','goodbye','talk to you later','later','good night','shutdown'],cmd) :

			n = random.randint(0,6)
			speak(gbl[n])
			active = False
			access = False




		elif check(['hi','hello','hey','hola','hey there','whats up'],cmd) :

			l.greetx()

		elif check(['your name','you called'],cmd) :

			l.name()

		elif check(['who are you','what are you'],cmd) :

			speak(' I\'m called Logically Interactive Software Algorithm, or LISA, in short')
			l.creator()
			l.techspex(version)

		elif check(['version'],cmd) :

			l.ver(version)

		elif check(['created','creator','born','designed'],cmd) :

			l.creator()

		elif check( ['inventory','see','show','what can you do ?'],cmd) :

			speak(' Some of the things I can do. ')
			l.menu()

		elif check(['song','music','play','favourite','songs'],cmd) :

			l.play_song()

		elif check(['date','today\'s'],cmd) :

			l.today_date() 
		
		elif check(['time','now'],cmd) :

			l.today_time()

		elif check(['age','old'],cmd) :

			l.age()

		elif check(['location','located','where am i right now'],cmd) :

			l.location()

		elif check(['wikipedia','wiki','search'],cmd) :

			l.wiki_search()

		elif check(['movies','movie','bored','suggest some movies','suggest','what to watch','recommend'],cmd):

			l.movie_prediction()


		elif check(['activate doomsday protocol','doomsday','protocol'],cmd) :

			status = l.doomsday_protocol()

			if status :
				
				exit()

			else :

				active = False
				access = False









		else:

			clean_slate()
			print(align+':('.center(130))
			speak('I\'m sorry. This might be beyond my abilities at the moment. ')



else :
	n = random.randint(0,6)
	speak(gbl[n])

clean_slate()

for i in range(10) :

	if i%2 == 0 :
	
		print(align+':('.center(130))
		time.sleep(0.5)
		clean_slate()	
	
	else :
	
		print(align+':)'.center(130))
		time.sleep(0.5)
		clean_slate()

time.sleep(3)
