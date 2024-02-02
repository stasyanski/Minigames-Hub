"""
Attempting to make a script which acts as a 
listener on left mouse press, testing it
"""

from pynput import mouse
from pygame import mixer

def on_click(x, y, button, pressed): # The on_click listener func takes x,y,button, and pressed, but for our app we only require button and pressed data
    if pressed: print('pressed', button)
    button = str(button)
    if button[-2] == 'f': # This is such a joke of a code but its funny
        mixer.init() # Initialise the mixer
        mixer.music.load('Resources\onclick_effect.mp3') # Dir to the sound effect
        mixer.music.play()
        
with mouse.Listener(on_click=on_click) as listener: # The listener esentially listens for mouse presses

    # RUN TK WINDOW example root.mainloop() SHOULD GO HERE!

    listener.join() # The join() method takes all items in an iterable and joins them into one string.A string must be specified as the separator.

