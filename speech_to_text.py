
# CONVERTING SPEECH INPUT TO TEXT INPUT

def Voice_in(z=True):

	from text_to_speech import Voice_out
	from misc_methods import align,clean_slate
	import speech_recognition as srg 
	import playsound
	store = srg.Recognizer()
	
	while True :	

		with srg.Microphone() as s :
			
			clean_slate()
			
			playsound.playsound('Tones/Siri - start.mp3',block='False')
			print(align+'Listening...'.center(130))
			
			if z :
				print('\n'*19+'<..> Say  "Bye" to end the conversation .'.rjust(135))
			
			store.adjust_for_ambient_noise(s)
			
			try :
				audio_in = store.listen(s,timeout=3)
			except :
				continue

			clean_slate()
			
			playsound.playsound('Tones/Siri - stop.mp3',block='False')
			print(align+'Stop'.center(130))

				

			try :
				text_out = store.recognize_google(audio_in)
				clean_slate()
				return text_out
				#print(text_out)
				break
					
			except:

				clean_slate()
				print(align+':('.center(130))
				Voice_out(" I'm sorry. I couldn't hear you clearly .")
				


			
