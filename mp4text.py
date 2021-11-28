import os
import speech_recognition as sr
# import ffmpeg

''''
	THIS CODE LET'S YOU CONVERT AUDIO TO TEXT
	FROM A WAV FILE WITH speech_recognition
	
	YOU can also convert an mp4 to a wav file
	(passing through the convertion to an mp3
	using ffmeg) withget_way

	As the script won't work if the wav is more
	than 10k, I made the duration to 100 and
	the I made other call to the record function
	that will continue from 100 to the next 100
	unit of time... until it reaches the end (
	there will be an error and the exception
	will print just Done)

'''

def get_wav():
	com1 = "ffmpeg -i 48.mp4 speech.mp3"
	com2 = "ffmpeg -i speech.mp3 speech.wav"
	os.system(com1)
	os.system(com2)

get_wav() # uncomment to get the wav


r = sr.Recognizer()
try:
	# this is the name of the file from which you take
	# the audio to converti into text
	with sr.WavFile("speech.wav") as source:
		audio0 = r.record(source, duration=100)
		audio1 = r.record(source, duration=100)
		audio2 = r.record(source, duration=100)
		audio3 = r.record(source, duration=100)
		audio4 = r.record(source, duration=100)
		audio5 = r.record(source, duration=100)
		# audio = r.listen(source)
	# The language is in italian, you can put 'en' for english
	print(r.recognize_google(audio0, language='it'))
	print(r.recognize_google(audio1, language='it'))
	print(r.recognize_google(audio2, language='it'))
	print(r.recognize_google(audio3, language='it'))
	print(r.recognize_google(audio4, language='it'))
	print(r.recognize_google(audio5, language='it'))
except:
	print("Done")
