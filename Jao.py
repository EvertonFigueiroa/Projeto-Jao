#pip install SpeechRecognition
#A biblioteca speech recognition possui a dependencia com a biblioteca PyAudio,
#por isso também precisamos instalá-la, com o comando.
#pip install pyaudio


import speech_recognition as sr
import pygame
#converso de texto para audio
import pyttsx3


def converVOZ(texto):
	engine = pyttsx3.init()
	engine.say(texto)
	engine.runAndWait()


converVOZ('BEM-VINDO EVERTON-SAMA, COMO POSSO AJUDAR')


def ouvir_microfone():
		# Habilita o microfone para ouvir o usuario
		microfone = sr.Recognizer()
		with sr.Microphone() as source:
			# Chama a funcao de reducao de ruido disponivel na speech_recognition
			microfone.adjust_for_ambient_noise(source)
			# Avisa ao usuario que esta pronto para ouvir
			print("Estou on...")
			# Armazena a informacao de audio na variavel
			audio = microfone.listen(source)

		try:
			# Passa o audio para o reconhecedor de padroes do speech_recognition
			frase = microfone.recognize_google(audio, language='pt-BR')

		# Caso nao tenha reconhecido o padrao de fala, exibe esta mensagem
		except sr.UnkownValueError:
			print("Não entendi")

		return frase


frase = ouvir_microfone()

while True:
	if frase.lower() == 'oi':
		converVOZ('Oi, chefe')
		frase = ouvir_microfone()
	elif frase.lower() == 'toca a boa':
		pygame.init()
		pygame.mixer.music.load('tchuco.mp3')
		pygame.mixer.music.play()
		frase = ouvir_microfone()
		if frase.lower() == 'pare' or 'stop':
			converVOZ('Tá maluco? Porque parou!')
		pygame.event.wait()
		input()

	else:
		converVOZ('Não entendi Everton-sama')
		converVOZ('Fale novamente')
		frase = ouvir_microfone()
