# -- coding: utf-8 --
# Autor: Meguinha  ( Matheus Felipe Vieira Santiago )
# PYTHON 3.7.6
# gtts, os
from gtts import gTTS
import os

def tts_config(text:str, file_name: str="default", set_lang: str = "en"):
    #creates an mp3 file using a string 
    #return filename.mp3
    file_name = f'{file_name}.mp3'
    file = gTTS(text, lang= set_lang)
    file.save(file_name)
    return file_name


#test
#tts("Isso é apenas um teste :) ", file_name="bruninhars", set_lang= "pt")
