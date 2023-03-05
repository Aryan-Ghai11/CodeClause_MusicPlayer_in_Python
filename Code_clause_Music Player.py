import tkinter as tk
from tkinter import filedialog
import pygame

# initialize pygame
pygame.init()

# create the main window
root = tk.Tk()
root.title("Music Player")

# create a label to display the status
status_label = tk.Label(root, text="Music Player")
status_label.pack()

# create a button to load the music file
def load_music():
    music_file = tk.filedialog.askopenfilename()
    pygame.mixer.music.load(music_file)
    status_label.config(text="Loaded: " + music_file)

load_button = tk.Button(root, text="Load Music", command=load_music)
load_button.pack()

# create a button to play the music
def play_music():
    pygame.mixer.music.play()
    status_label.config(text="Playing")

play_button = tk.Button(root, text="Play", command=play_music)
play_button.pack()

# create a button to pause the music
def pause_music():
    pygame.mixer.music.pause()
    status_label.config(text="Paused")

pause_button = tk.Button(root, text="Pause", command=pause_music)
pause_button.pack()

# create a button to stop the music
def stop_music():
    pygame.mixer.music.stop()
    status_label.config(text="Stopped")

stop_button = tk.Button(root, text="Stop", command=stop_music)
stop_button.pack()

# run the main loop
root.mainloop()

# quit pygame
pygame.quit()
