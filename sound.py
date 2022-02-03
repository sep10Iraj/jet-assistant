# -*- coding: utf-8 -*-
"""
Created on Sun Nov  7 11:39:47 2021

@author: digi max
"""
 
import pyttsx3
for i in range(10):
    text=input('write=>')
    se=pyttsx3.init("sapi5")
    
    se.setProperty('rate', 100)
    se.say(text)
    se.runAndWait()
