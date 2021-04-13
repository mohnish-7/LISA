#############################################################################################################################################################

# 															LISA's Backend Functions

#############################################################################################################################################################

from speech_to_text import Voice_in as listen
from text_to_speech import Voice_out as speak
from time import sleep
from misc_methods import align,clean_slate,choice
import pickle



 

def age():

	from datetime import date
	original = date(2020,7,13)
	today = date.today()
	age = today - original
	speak('Well....i was created on July 13th ,2020.')
	speak('So that means.....I\'m '+str(age.days)+' days old .')





def greet() :

	from datetime import datetime as dt 
	now = dt.now()
	ct = int(now.strftime('%H'))
	fd = open('User_data.pkl','rb')
	adm = pickle.load(fd)

	if ct < 12 :

		speak(' Good Morning,'+adm.f_name+'!')

	elif ct < 17 :

		speak(' Good Afternoon, '+adm.f_name+' ! ')

	else :

		speak('Good Evening, '+adm.f_name+' ! ')





def menu() :

	clean_slate()

	print('\n'*4+''' 
					Some of the things I can do  :)


								>	Introduce myself
								
								>	I can play your favourite music
								
								>	Get you the current date or time

								>	Do a Wikipedia search !

								>	Recommend some movies
							
				\n\n\n			
				

				<.>   Just ask me " What can you do ? " , to see this Inventory again.   <.>
							''')
	sleep(7)


def interact(cmd) :

	pass

def name() :

	clean_slate()

	print(align+':)'.center(130))

	speak(' I\'m technically called Logically Interactive Software Algorithm. But, you can call me LISA ! ')




def ver(v) :

	speak(' My current operating version is '+str(v)+'.')




def creator() :

	clean_slate()

	print(align+':)'.center(130))

	speak('I was created by Moh nish on July 13th, 2020.')




def techspex(v):

	clean_slate()

	print(align+':)'.center(130))

	speak(" I'm a Virtual Voice Assistant built using Python 3. I can also function as a ChatBot.")

	speak(' My current operating version is '+str(v)+'.')




def play_song() :

	import vlc
	import os
	import random
	import getch
	playing = True
	
	s_dir = 'C:/Users/mohni/Documents/Personal/Projects/LISA/Songs/'
	song_list = os.listdir(s_dir)
	n = None
	
	
	while playing :

		c = 0
		m = random.randint(0,len(song_list))
		while m == n :
			m = random.randint(0,len(song_list))
		n = m


		try :
			
			song = song_list[n]
		
			s = vlc.MediaPlayer(s_dir+song)
			clean_slate()
			print(align+':)'.center(130))
				
			try :
				
				speak(f'PLaying : {song[:-4]} ',bk=False)
				s.play()

			except:
				
				print('error')


			while True :
				
				clean_slate()
				

				if c%2 == 0 :

					print('\n'*16+"|>".center(132))

				else :

					print('\n'*16+'||'.center(132))

				print('\n'*15+'<..>   Press SPACEBAR to pause and ENTER to stop playing   <..>'.rjust(100))
				print('\n'+'<.>  Press X to skip this song  <.>'.rjust(85))

				try :

					sleep(0.1)
					x = getch.getch()
					x = x.decode('utf-8')
					x = x.lower()

					if x == ' ' :

						s.pause()
						c += 1
			
					elif x.lower() == 'x' :

						c = 0
						clean_slate()
						print('\n'*16+">>".center(132))
						s.stop()
						speak('Skipping this song.')	
						break

					elif x == '\r' :

						clean_slate()
						print('\n'*16+'::'.center(132))
						playing = False
						s.stop()
						break

				except :

					continue

		except :

			continue



def today_date() :

	from datetime import datetime

	x = datetime.now()
	d = x.strftime("%A . %B %d , %Y")
	speak('Today is : '+d)

def today_time() :

	from datetime import datetime

	c = 0
	x = datetime.now()
	t = x.strftime(" %I:%M %p")
	speak('The current time is : '+t,bk=False)

	while c < 10 :

		clean_slate()
		y = datetime.now()
		ti = y.strftime(" %I:%M:%S %p")
		print(align+ti.center(133))
		sleep(1)
		c += 1


def greetx() :

	from random import randint
	clean_slate()
	g = ['Hello !','Hi !','Hola !','Hey there !','Well hello there !','Hey !']
	op = randint(0,5)
	speak(g[op])


def personal_mode() :

	clean_slate()

	talking = True

	speak('Alright then ! Switching to personal mode .')
	print(align+'\n'*15+'<.> Just say " Switch back to Virtual Assistant " to use LISA as an Virtual Assistant <.>'.center(134))





def wiki_search() :

		
		from wikipedia import summary as wiki
	

		clean_slate()

		search = True

		while search == True :

			clean_slate()
			speak('What do you want to search for ?')
			query = listen(z=False)

			while True :

				clean_slate()
					
				try :

					data = wiki(query,sentences=2)
					clean_slate()
					print(align+query.center(130))
					speak(data)
					sleep(2)
					clean_slate()

				except :

					clean_slate()
					speak('Hmm. No data found.')

				
				a = choice('Was that what you were looking for ?')

				if a in ' yes yeah s yea yep yup ' :

					break
					
				else :
					clean_slate()
					print(align+'Kindly type in your search term :\n '.center(134))
					query = input('\n'.center(120))
					continue

			clean_slate()
			speak('Do you want to search for anything else ?\n')
			
			a = choice('Wanna search another term ?')

			if a in ' yes yeah s yea yep yup okay alright ' :

				continue

			else :
				
				speak('Okay !')
				sleep(1)
				search = False





def location() :

	import requests
	import json

	send_url = "http://api.ipstack.com/check?access_key=4451c6bc43183503744b9f5b2f948aff"
	geo_req = requests.get(send_url)
	geo_json = json.loads(geo_req.text)
	latitude = geo_json['latitude']
	longitude = geo_json['longitude']
	country = geo_json['country_name']
	state = geo_json['region_name']
	city = geo_json['city']
	speak('You\'re currently in : '+city+' , '+state+' , '+country)



def movie_prediction():

	# Importing required libraries and reading the dataset. 


    import pandas as pd
    import numpy as np
    from sklearn.metrics.pairwise import cosine_similarity
    from sklearn.feature_extraction.text import CountVectorizer
    from pickle import load,dump
    from os import system
    df = pd.read_csv('Datasets/movies_data.csv')
    clean_slate()
    # Function to create a string of important features for each movie.

    def get_imp_features(data) :
        important_features = []
        for i in range(0,data.shape[0]): 
            important_features.append(data['Title'][i]+' '+data['Certificate'][i]+' '+data['Genre'][i]+' '+data['Director'][i]+' '+data['Star1'][i]+' '+data['Star2'][i])

        return important_features

    # Getting the title from the user.
    speak('Enter the most recent movie you watched: ')
    title = input(align+'Movie:  '.rjust(60))

    # Function to find a similar title to the one user has entered.

    def alt_title(df,title):

        cm1 = CountVectorizer().fit_transform([title]+list(df['Title']))
        cs1 = cosine_similarity(cm1)
        scores = list(enumerate(cs1[0]))
        sorted_scores = sorted(scores,key = lambda x : x[1], reverse = True)
        sorted_scores = sorted_scores[1:]
        t = df['Title'][sorted_scores[0][0]-1]
        return t

    # Vectorizing all the important features and creating a cosine-similarity matrix.

    df['imp_features'] = get_imp_features(df)
    cm = CountVectorizer().fit_transform(list(df['imp_features']))
    cs = cosine_similarity(cm)

    # Findig the movie id of the title the user entered.

    f= 0
    try:
        mov_id = df[df.Title == title]['movie_id'].values[0]
    except:
        f=1
        title = alt_title(df,title)
        mov_id = df[df.Title == title]['movie_id'].values[0]

    # Creating a list, where each element is a tuple having the index and similarity score as its elements, and sorting it.

    scores = list(enumerate(cs[mov_id]))
    sorted_scores = sorted(scores,key = lambda x : x[1], reverse = True)
    if f == 0:
        sorted_scores = sorted_scores[1:]


    # Printing the the most recommended movies.

    m = 0
    clean_slate()
    speak('The 7 most recommended movies are: ')
    print('\n'*10)
    for item in sorted_scores:
        movie_title = df[df.movie_id == item[0]]['Title'].values[0]
        sleep(0.5)
        print('\n',str(m+1).rjust(55),movie_title)
        m += 1
        if m > 6:
            break
    if f == 1:
        speak('Due to insufficient data, these results might not be 100 percent accurate.')

    sleep(5)  




























def doomsday_protocol():

	from misc_methods import getPass,file_load,align,User
	import os,time,shutil
	from colorama import init,Fore
	
	atv = True
	attempts = 3

	speak('Activating this protocol will erase me permanently from your computer. To confirm, please enter your password.')
	
	while atv:

		if attempts == 0:
			speak('Sorry you are out of attempts. PROTOCOL activation failed.')
			return False
		else:
			speak('You have '+str(attempts)+' attempts left.')
		clean_slate()
		print(align+'Password -->   '.rjust(70),end='')
		password = getPass()
		boss = User()
		boss = file_load(boss,'User_data.pkl')

		if password == boss.password :
			
			clean_slate()
			speak('Activating DOOMSDAY PROTOCOL in:')

			speak('3')
			time.sleep(0.1)
			speak('2')
			time.sleep(0.1)
			speak('1')
			time.sleep(1)
			print(align+Fore.RED+'DOOMSDAY PROTOCOL ACTIVATED'.rjust(80))
			speak('Goodbye '+boss.f_name)
			time.sleep(2)
			os.startfile('C:/Users/mohni/Documents/Personal/Projects/LISA/GOODBYE.txt')
			os.unlink('C:/Users/mohni/Documents/Personal/Projects/LISA/LISA.py')
			os.unlink('C:/Users/mohni/Documents/Personal/Projects/LISA/logic_module.py')
			os.unlink('C:/Users/mohni/Documents/Personal/Projects/LISA/misc_methods.py')
			os.unlink('C:/Users/mohni/Documents/Personal/Projects/LISA/speech_to_text.py')
			os.unlink('C:/Users/mohni/Documents/Personal/Projects/LISA/text_to_speech.py')
			os.unlink('C:/Users/mohni/Documents/Personal/Projects/LISA/Version_Log.txt')
			os.unlink('C:/Users/mohni/Documents/Personal/Projects/LISA/User_count.pkl')
			os.unlink('C:/Users/mohni/Documents/Personal/Projects/LISA/User_data.pkl')
			shutil.rmtree('C:/Users/mohni/Documents/Personal/Projects/LISA/Songs')
			shutil.rmtree('C:/Users/mohni/Documents/Personal/Projects/LISA/LISA_ResponseCache')
			shutil.rmtree('C:/Users/mohni/Documents/Personal/Projects/LISA/__pycache__')
			shutil.rmtree('C:/Users/mohni/Documents/Personal/Projects/LISA/Tones')
			atv = False
			return True

		else :
			
			speak('Wrong password! Wanna try again ?')
			ans = choice('Try again ?')
			
			if ans in 'yes yeah ye yup yep ok k alright':
				attempts -= 1
				continue
			
			else:
				return False


