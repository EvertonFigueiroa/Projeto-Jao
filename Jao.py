import speech_recognition as sr
import pygame
import pyttsx3


def converVOZ(texto):
	engine = pyttsx3.init()
	engine.say(texto)
	engine.runAndWait()


print('-=-'*20)
print(f'{"PROJETO JÃO":.^60}')
print('-=-'*20)

converVOZ('BEM-VINDO MEU PATRÃO, COMO POSSO AJUDAR')


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
		converVOZ('É pra já')
		pygame.init()
		pygame.mixer.music.load('tchuco.mp3')
		pygame.mixer.music.set_volume(0.1)
		pygame.mixer.music.play()
		pygame.event.wait()

		resposta = str(input('Deseja para a música? [S/N]: ')).strip()
		if resposta in 'Ss':
			frase = ouvir_microfone()
			pygame.mixer.music.stop()
			converVOZ('POXA TAVA TÃO BOM')
		frase = ouvir_microfone()

	elif frase.lower() == 'vou dormir' or 'vou dormi':
		converVOZ('Bom descanso chefe!')
		break
	else:
		converVOZ('Fala pra fora que eu Não entendi')
		frase = ouvir_microfone()
