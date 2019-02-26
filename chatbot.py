# -*- coding: utf-8 -*-
from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot
from gtts import gTTS
import pygame
import time
import speech_recognition as sr

pygame.init()	

chatbot = ChatBot('Charlie')

texto = open('chat.txt','r')
cumprimento = texto.readlines()

chatbot.set_trainer(ListTrainer)
chatbot.train(cumprimento)

while True:

	rec = sr.Recognizer()
	with sr.Microphone() as fala:
		frase = rec.listen(fala)
	usuario = rec.recognize_google(frase)

	quest = usuario
	response = chatbot.get_response(quest)

	voz = gTTS(str(response), lang="pt")
	voz.save('voz.mp3')

	print(response)

	pygame.mixer.music.load("voz.mp3")
	pygame.mixer.music.play()
	time.sleep(2)
