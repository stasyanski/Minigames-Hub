"""
program: hangman.py
author: Stanislav Birca, Kameron Bains

this python file acts as the interface
for the hangman minigame for our
python minigame hub.
"""
def hangman():
    #-------------------Libraries-------------------
    import customtkinter as ctk
    import random
    import time

    #-------------------CTk appearance-------------------
    ctk.set_appearance_mode("Dark")
    ctk.set_default_color_theme("green")

    #-------------------Hangman window-------------------
    hang = ctk.CTk() # Reference to hangman window as hang
    hang.configure(fg_color = 'whitesmoke')
    window_height = 550; window_width = 836
    screen_width = hang.winfo_screenwidth() # get user screenwidth
    screen_height = hang.winfo_screenheight() # get user screenheight
    center_x = int(screen_width / 2 - window_width / 2) # center app based on user screenwidth
    center_y = int(screen_height / 2 - window_height / 2) # center app based on user screenheight
    hang.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}') # set window geometry and centering it on x and y axis
    hang.resizable(width=False, height=False)
    hang.title('Hangman') 
    hang.iconbitmap('Resources/iconbitmap.ico')

    #-------------------All functions go in below-------------------
    


       

    #-------------------All functions go in above-------------------

    
    #-------------------Left frame and right frame-------------------
    hangCanvas = ctk.CTkCanvas(master=hang)
    hangCanvas.grid_propagate(False); hangCanvas.pack(side="left", fill="both", expand=True)
    # for side, fill and expand visual guide check https://stackoverflow.com/questions/28089942/difference-between-fill-and-expand-options-for-tkinter-pack-method

    wordFrame = ctk.CTkFrame(master=hang, width=400, fg_color='#dcdcdc') 
    # height here (in wordFrame and keyboardFrame) is 4 more pixels as CTkFrame and CTkCanvas respects height value differently
    wordFrame.grid_propagate(False); wordFrame.pack(side="top", fill="both", padx=5, pady=(5,0), expand=True)

    keyboardFrame = ctk.CTkFrame(master=hang, width=400, height=185, fg_color='#dcdcdc') 
    # height here (in wordFrame and keyboardFrame) is 4 more pixels as CTkFrame and CTkCanvas respects height value differently.
    keyboardFrame.grid_propagate(False); keyboardFrame.pack(side="bottom", fill="both", padx=5, pady=5)

    #-------------------Hangman-------------------

    def highlighted():
        letter_list[0].configure(fg_color='#CFFDBC', text_color='black')

    
    #-------------------Display word-------------------
    wordPool = ['BLIZZARD', 'OXYGEN', 'HYPERTROPHY', 'VOODOO', 'ZODIAC', 'XYLOPHONE', 'KAYAK', 'TRANSCRIPT', 'UNBEKNOWN', 'AFOREMENTIONED',
                'PNEUMONIA', 'SCISSORS', 'MISCHIEVOUS', 'PENGUIN', 'EPITOME', 'STOICISM', 'NIHILISM', 'ALGEBRA', 'DOCTRINE', 'SHENANIGANS', 'HANGMAN', 
                'CAR WASH', 'FATHER IN LAW', 'OVER THE COUNTER', 'UNDER THE SEA', 'OUTER SPACE', 'POST CARD', 'NOSE BLEED', 'KICK BOXING', 'FRENCH FRIES',
                'CHOCOLATE CHIP', 'BODY GUARD', 'BANTAM WEIGHT', 'BUSINESS MAN', 'CHECK MATE', 'DOWN STREAM', 'FINGER PRINT', 'FRAME WORK', 'GENTLE MAN']
                    # feel free to add words, both compound words and normal words

    word = random.choice(wordPool) # chooses random word from wordPool
    
    #-------------------Creating empty label based on current word-------------------
    relxval = 0.0; relyval = 0.3
    letter_list=[]

    for loop in range(0, len(word)+1):
            relxval += 0.143 # adjust spacing between buttons, .143 is perfect spacing
            if loop % 6 == 0 : # if divisible by 6 (6,12,18,etc.) create a new row
                relyval += 0.12 # increase y spacing
                relxval = 0.143 # reset x position
            # creating label for each letter of the word
            letter = ctk.CTkLabel(master=wordFrame, height=30, width=48, text='_', text_color='gray', font=('Comic Sans MS', 27), fg_color='lightgray')
            letter.place(relx=relxval, rely=relyval, anchor="c")
            # append the list of buttons with the currently created one
            letter_list.append(letter)

    #-------------------Creating buttons using for loop-------------------
    alphabet = {'A': (3, 0), 'B': (3, 1), 'C': (3, 2), 'D': (3, 3), 'E': (3, 4), 'F': (3, 5), 'G': (3, 6), 'H': (3, 7),
                'I': (4, 0), 'J': (4, 1), 'K': (4, 2), 'L': (4, 3), 'M': (4, 4), 'N': (4, 5), 'O': (4, 6), 'P': (4, 7),
                'Q': (5, 0), 'R': (5, 1), 'S': (5, 2), 'T': (5, 3), 'U': (5, 4), 'V': (5, 5), 'W': (5, 6), 'X': (5, 7),
                'Y': (6, 0), 'Z': (6, 1), 
                'SPACE': (6, 2)}
    # dict maps each letter of the alphabet and the space to its row and column

    button_list=[]
    for current, (rowNum, columnNum) in alphabet.items():
        if current == 'SPACE': 
            # space is treated differently with bigger column day, representing common physical and virtual keyboard space buttons
            button = ctk.CTkButton(master=keyboardFrame, width=250, height=30, text=current, font=('Comic Sans MS', 27),
                                   fg_color='whitesmoke', text_color='gray', hover_color='#EEEEEE')
            button.grid(column=columnNum, row=rowNum, pady=1, padx=1, columnspan=6)
        else:
            button = ctk.CTkButton(master=keyboardFrame, width=48, height=30, text=current, font=('Comic Sans MS', 27),
                                   fg_color='whitesmoke', text_color='gray', hover_color='#EEEEEE')
            button.grid(column=columnNum, row=rowNum, pady=1, padx=1)
        button_list.append(button)

    highlighted()
    # Run the app
    hang.mainloop()