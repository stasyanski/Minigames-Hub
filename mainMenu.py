"""
program: mainMenu.py
author: Stanislav Birca, Kameron Bains

this python file acts as the main menu
of our Minigames Hub project, where the user
can select their preferred minigame to play.
"""

# Libraries
import customtkinter as ctk
from PIL import Image # For putting CTk Images

# Import functions from other files
from ticTacToe import ticTacToe

# CTk appearance: check the docs for more info
ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("green")  

# Menu window
menu = ctk.CTk() # Reference to menu window as 'menu' 
window_height = 600; window_width = 800
screen_width = menu.winfo_screenwidth()
screen_height = menu.winfo_screenheight()
center_x = int(screen_width/2 - window_width / 2)
center_y = int(screen_height/2 - window_height / 2)
menu.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}') # Center the menu window, so it opens in middle of user screen
menu.resizable(width=False, height=False)
menu.title('Minigames Hub')
menu.iconbitmap('Resources/iconbitmap.ico')

# Frame
frameButtons = ctk.CTkFrame(master=menu)
frameButtons.pack(padx=12, pady=12) # Putting a frame on master window which is menu

# Button images
ticTacToe_image = ctk.CTkImage(light_image=Image.open('Resources/ticTacToe.png'),
                                  dark_image=Image.open('Resources/ticTacToe.png'),
                                  size=(250,250))

# Buttons for games
game1 = ctk.CTkButton(master=frameButtons, text=' ', image=ticTacToe_image, width=367, height=268, command=ticTacToe)
game1.grid(padx=10, pady=10, row=0, column=0)

# game1 button has already been used. when linking a button, import the function (from tictactoe import tictactoe)
# link it using command = , change the text = , and remove the state =  and fg_color options.

game2 = ctk.CTkButton(master=frameButtons, text='To be added', width=367, height=268, state='disabled', fg_color='#5A5A5A')
game2.grid(padx=10, pady=10, row=0, column=1)

game3 = ctk.CTkButton(master=frameButtons, text='To be added', width=367, height=268, state='disabled', fg_color='#5A5A5A')
game3.grid(padx=10, pady=10, row=1, column=0)

game4 = ctk.CTkButton(master=frameButtons, text='To be added', width=367, height=268, state='disabled', fg_color='#5A5A5A')
game4.grid(padx=10, pady=10, row=1, column=1)

# Run the app
menu.mainloop()