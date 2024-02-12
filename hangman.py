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
    import turtle
    import random

    #-------------------CTk appearance-------------------
    ctk.set_appearance_mode("Dark")
    ctk.set_default_color_theme("green")

    #-------------------Hangman window-------------------
    hang = ctk.CTk() # Reference to hangman window as hang
    hang.configure(fg_color = 'whitesmoke')
    window_height = 550; window_width = 836
    screen_width = hang.winfo_screenwidth()
    screen_height = hang.winfo_screenheight()
    center_x = int(screen_width/2 - window_width / 2)
    center_y = int(screen_height/2 - window_height / 2)
    hang.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
    hang.resizable(width=False, height=False)
    hang.title('Hangman')
    hang.iconbitmap('Resources/iconbitmap.ico')

    #-------------------All functions go in below-------------------
    


       

    #-------------------All functions go in above-------------------

    
    #-------------------Left frame and right frame-------------------
    hangCanvas = ctk.CTkCanvas(master=hang)
    hangCanvas.grid_propagate(False); hangCanvas.pack(side="left", fill="both", expand=True)
    # for side, fill and expand visual guide check https://stackoverflow.com/questions/28089942/difference-between-fill-and-expand-options-for-tkinter-pack-method

    wordFrame = ctk.CTkFrame(master=hang, width=400, fg_color='#dcdcdc') #height here (in wordFrame and keyboardFrame) is 4 more pixels as CTkFrame and CTkCanvas respects height value differently.
    wordFrame.grid_propagate(False); wordFrame.pack(side="top", fill="both", padx=5, pady=(5,0), expand=True)

    keyboardFrame = ctk.CTkFrame(master=hang, width=400, height=185, fg_color='#dcdcdc') #height here (in wordFrame and keyboardFrame) is 4 more pixels as CTkFrame and CTkCanvas respects height value differently.
    keyboardFrame.grid_propagate(False); keyboardFrame.pack(side="bottom", fill="both", padx=5, pady=5)

    #-------------------Hangman-------------------

        #code here
    
    #-------------------Display word-------------------
    wordPool = ['BLIZZARD', 'OXYGEN', 'HYPERTROPHY', 'VOODOO', 'ZODIAC', 'XYLOPHONE', 'KAYAK', 'TRANSCRIPT', 'UNBEKNOWN', 'AFOREMENTIONED',
                'PNEUMONIA', 'SCISSORS', 'MISCHIEVOUS', 'PENGUIN', 'EPITOME', 'STOICISM', 'NIHILISM', 'ALGEBRA', 'DOCTRINE', 'SHENANIGANS', 'HANGMAN', 
                'CAR WASH', 'FATHER IN LAW', 'OVER THE COUNTER', 'UNDER THE SEA', 'OUTER SPACE', 'POST CARD', 'NOSE BLEED', 'KICK BOXING', 'FRENCH FRIES',
                'CHOCOLATE CHIP', 'BODY GUARD', 'BANTAM WEIGHT', 'BUSINESS MAN', 'CHECK MATE', 'DOWN STREAM', 'FINGER PRINT', 'FRAME WORK', 'GENTLE MAN']
                    #feel free to add words, both compound words and normal words

    word = wordPool[random.randint(0, len(wordPool))] # chooses random word from wordPool
    print(word)
    
    # ----WORK IN PROGRESS ----- NEEDS CENTERING -------
    columnCount = 0; rowCount = 2
    for loop in range(0, len(word)+1):
            if columnCount == 8: columnCount = 0
            if columnCount % 8==0: rowCount+=1
            ctk.CTkLabel(master=wordFrame, height=30, width=48, text='_', font=('Comic Sans MS', 27), fg_color='gray').grid(row=rowCount, column=columnCount, padx=1, pady=1) 
            columnCount += 1 # for iteration

    #-------------------Creating buttons using for loop-------------------
    alphabet = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','SPACE']
    iteration = 0; columnNum = -1
    for current in alphabet:
        iteration += 1; columnNum +=1
        if iteration <= 8: rowNum = 2
        elif iteration <= 16: rowNum = 4
        elif iteration <= 24: rowNum = 5
        else: rowNum = 6
        if columnNum >= 8: columnNum = 0
        if current == 'SPACE':
            ctk.CTkButton(master=keyboardFrame, width=250,height=30, text=current, font=('Comic Sans MS', 27), fg_color='whitesmoke',
                        text_color='gray', hover_color='#EEEEEE').grid(column=columnNum, row=rowNum, pady=1,padx=1, columnspan=6)
        else:
            ctk.CTkButton(master=keyboardFrame, width=48,height=30, text=current, font=('Comic Sans MS', 27), fg_color='whitesmoke',
                        text_color='gray', hover_color='#EEEEEE').grid(column=columnNum, row=rowNum, pady=1,padx=1)

    #Run the app
    hang.mainloop()

