# Importing necessary modules

import pygame
import tkinter as tkr
from tkinter.filedialog import askdirectory
import os

# Creating application window
musicplayer = tkr.Tk()

# Setting the title name
musicplayer.title("Music Player")

# Setting the dimension
musicplayer.geometry("450x350")

# Asking for music directory
directory = askdirectory()

# Setting music directory to the current working directory
os.chdir(directory)

# Creating our songlist
# os.listdir() returns a list containing the names of the entries in the directory given by the path
songlist = os.listdir()

# Creating the playlist
playlist = tkr.Listbox(musicplayer, font = "Cambria 14 bold", bg = "cyan2", selectmode = tkr.SINGLE)

# Adding songs from songlist to playlist
for item in songlist:
    pos=0
    playlist.insert(pos, item)
    pos = pos+1

# Initialising our modules
pygame.init()
pygame.mixer.init()

# Function for Play button
def play():
    pygame.mixer.music.load(playlist.get(tkr.ACTIVE))
    var.set(playlist.get(tkr.ACTIVE))
    pygame.mixer.music.play()

# Function fo Stop button
def exitmusicplayer():
    pygame.mixer.music.stop()

# Function for Pause button
def pause():
    pygame.mixer.music.pause()

# Function for Resume/Unpause button
def resume():
    pygame.mixer.music.unpause()

# Creating Buttons
Button_Play = tkr.Button(musicplayer, height=3, width=5, text="Play Music", font="Cambria 14 bold", command=play, bg="lime green", fg="black")
Button_Stop = tkr.Button(musicplayer, height=3, width=5, text="Stop Music", font="Cambria 14 bold", command=exitmusicplayer, bg="red", fg="black")
Button_Pause = tkr.Button(musicplayer, height=3, width=5, text="Pause Music", font="Cambria 14 bold", command=pause, bg="yellow", fg="black")
Button_Resume = tkr.Button(musicplayer, height=3, width=5, text="Resume Music", font="Cambria 14 bold", command=resume, bg="purple", fg="black")
Button_Play.pack(fill="x")
Button_Stop.pack(fill="x")
Button_Pause.pack(fill="x")
Button_Resume.pack(fill="x")

playlist.pack(fill="both", expand="yes")

var = tkr.StringVar()
songtitle = tkr.Label(musicplayer, font="Cambria 12 bold", textvariable=var)
songtitle.pack()
musicplayer.mainloop()