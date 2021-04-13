
# CONVERTING TEXT OUTPUT TO SPEECH OUTPUT

def Voice_out(txt,sl=False,bk=True) :
	
	import os
	from gtts import gTTS
	import playsound
	import random

	op = gTTS(text=txt,lang='en',tld='us',slow=sl)
	file_name = 'LISA_ResponseCache/LISA_response'+str(random.randint(0,100))+'.mp3'
	op.save(file_name)

	playsound.playsound(file_name,block=bk)

	os.unlink(file_name)


#Voice_out("Hey There ! Im LISA")
