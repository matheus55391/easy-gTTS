# -- coding: utf-8 --
# Autor: Meguinha  ( Matheus Felipe Vieira Santiago )
# PYTHON 3.7.6
# gtts, os
from gtts import gTTS as mytts

def tts_convert(text:str, file_name: str="default", play:bool =False):
    #creates an mp3 file using a string 
    file = mytts(text)
    file.save(f"{file_name}.mp3")