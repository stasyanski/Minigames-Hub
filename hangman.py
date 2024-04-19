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
    import random # for choosing word from wordpool
    import turtle # using t for hangman
    import tkinter as tk # using tk canvas, as ctk canvas produces unwanted behaviour
    from CTkMessagebox import CTkMessagebox

    #-------------------Global variables-------------------
    global num_attempts # this var is used accross different funcs
    num_attempts = 0 # defining as 0 for number of attempts

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
    
    def game(id, button): # get button ID (index within alphabet list) and the button pressed
        global num_attempts
        
        button_list[id].configure(state=ctk.DISABLED, fg_color='#dcdcdc') # disables a button after pressed 

        for loop in range(len(word)): # checks each letter of word
            if button in word[loop]: # if button pressed is in word
                letter_list[loop].configure(text=word[loop], text_color='black')
                    # the display letter is revealed

        if button not in word: # if the button is not in word
            num_attempts += 1 # increase attetmpts taken by 1
            wrong(num_attempts) # call the wrong func with nr of atttempts
        
        # all() returns true only if all value are NOT '_', as '_' is the default text for letter_list
        if all(value.cget("text") is not '_' for value in letter_list): 

            #if all() is true, win notif appears
            wonnotif = CTkMessagebox(title='End of game', message="You've won! Congratulations", fade_in_duration=1, justify='center', 
                          icon='check', button_color='gray', button_hover_color='white', button_text_color='black',
                          option_1='Restart', option_2='Quit')
            
            if wonnotif.get() == 'Restart':
                hang.destroy() # destroys current game
                hangman() # creates new game
            hang.destroy() # destroys current game
            
    def lost(): # gets called when nr attempts is 7
            for loop in button_list:
                loop.configure(state=ctk.DISABLED) # disabled the entire keyboard

            # lost notif appears asking user if they want to restart or quit
            lostnotif = CTkMessagebox(title='End of game', message=f"You lost. The word was {word}!", fade_in_duration=1, justify='center', 
                          icon='question', button_color='gray', button_hover_color='white', button_text_color='black',
                          option_1='Restart', option_2='Quit')
            if lostnotif.get() == 'Restart':
                hang.destroy() # destroys current game
                hangman() # creates new game
            hang.destroy() # destroys current game
                
    def wrong(num_attempts):

        # special thanks to: turtle code taken from https://github.com/john-u/hangman/blob/main/hangman.py
        # adapted code to this projects needs
    
        t = turtle.RawTurtle(hangCanvas)
        t.speed(0)
        t.width(3)
        t.hideturtle()

        if num_attempts == 1:
            # draw gallow bottom
            t.penup()
            t.goto(40, -200)
            t.pendown()
            t.forward(45)
            t.left(180)
            t.forward(90)
            t.right(180)
            t.forward(45)
            # draw gallow top
            t.left(90)
            t.forward(175)
            t.left(90)
            t.forward(75)
            t.left(90)
            t.forward(35)
            t.penup()

        elif num_attempts == 2:
            # draw head
            t.penup()
            t.goto(-49.5, -75)
            t.pendown()
            t.right(90)
            t.circle(15,None,100)
            t.penup()

        elif num_attempts == 3:
            # draw torso
            t.penup()
            t.goto(-35.5, -160)
            t.pendown()
            t.left(90)
            t.penup()
            t.forward(30)
            t.pendown()
            t.forward(40)
            t.right(180)
            t.forward(30)
            t.penup()

        elif num_attempts == 4:
            # draw first arm
            t.penup()
            t.goto(-62, -140)
            t.pendown()
            t.left(55)
            t.forward(45)
            t.right(180)
            t.forward(45)
            t.penup()

        elif num_attempts == 5:
            # draw second arm
            t.penup()
            t.goto(-8, -140)
            t.pendown()
            t.left(125)
            t.forward(45)
            t.right(180)
            t.forward(45)
            t.penup()

        elif num_attempts == 6:
            # draw first leg
            t.penup()
            t.goto(-35, -130)
            t.pendown()
            t.right(120)
            t.forward(45)
            t.penup()

        elif num_attempts == 7:
            # draw second leg
            t.penup()
            t.goto(-35, -130)
            t.pendown()
            t.right(60)
            t.forward(45)
            t.penup()
            
            # at the last try, triggest the lost func
            lost() # triggest lost func to display CTkMessageBox 

    #-------------------All functions go in above-------------------



    #-------------------Left frame and right frame-------------------
    hangCanvas = tk.Canvas(master=hang) # custom tkinter seems to be broken when using ctk.CTkCanvas, tkinter naturally goes with t canvas
    hangCanvas.grid_propagate(False); hangCanvas.pack(side="left", fill="both", expand=True)
    # for side, fill and expand visual guide check https://stackoverflow.com/questions/28089942/difference-between-fill-and-expand-options-for-tkinter-pack-method

    wordFrame = ctk.CTkFrame(master=hang, width=400, fg_color='#dcdcdc') 
    # height here (in wordFrame and keyboardFrame) is 4 more pixels as CTkFrame and CTkCanvas respects height value differently
    wordFrame.grid_propagate(False); wordFrame.pack(side="top", fill="both", padx=5, pady=(5,0), expand=True)

    keyboardFrame = ctk.CTkFrame(master=hang, width=400, height=185, fg_color='#dcdcdc') 
    # height here (in wordFrame and keyboardFrame) is 4 more pixels as CTkFrame and CTkCanvas respects height value differently.
    keyboardFrame.grid_propagate(False); keyboardFrame.pack(side="bottom", fill="both", padx=5, pady=5)



    #-------------------Display word-------------------
    wordPool = ['BLIZZARD', 'OXYGEN', 'HYPERTROPHY', 'VOODOO', 'ZODIAC', 'XYLOPHONE', 'TRANSCRIPT', 'UNBEKNOWN', 'AFOREMENTIONED', 'VISION',
                'PNEUMONIA', 'SCISSORS', 'MISCHIEVOUS', 'PENGUIN', 'EPITOME', 'STOICISM', 'NIHILISM', 'ALGEBRA', 'DOCTRINE', 'SHENANIGANS', 'HANGMAN', 
                'CAR WASH', 'FATHER IN LAW', 'OVER THE COUNTER', 'UNDER THE SEA', 'OUTER SPACE', 'POST CARD', 'NOSE BLEED', 'KICK BOXING', 'FRENCH FRIES',
                'CHOCOLATE CHIP', 'BODY GUARD', 'BANTAM WEIGHT', 'BUSINESS MAN', 'CHECK MATE', 'DOWN STREAM', 'FINGER PRINT', 'FRAME WORK', 'GENTLE MAN']
                    # feel free to add words, both compound words and normal words
                    # ! words must be 6 or more letters !

    word = random.choice(wordPool) # chooses random word from wordPool
    print(word)



    #-------------------Creating empty label based on current word-------------------
    relxval = 0.0; relyval = 0.3
    letter_list=[]

    for loop in range(0, len(word)):
            relxval += 0.143575 # adjust spacing between buttons, .14375 is perfect spacing
            if loop % 6 == 0 : # if divisible by 6 (6,12,18,etc.) create a new row
                relyval += 0.12 # increase y spacing
                relxval = 0.14375 # reset x position
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
                ' ': (6, 2)}
    # dict maps each letter of the alphabet and the space to its row and column

    button_list=[]
    for current, (rowNum, columnNum) in alphabet.items():
        if current == ' ': 
            # space is treated differently with bigger column day, representing common physical and virtual keyboard space buttons
            button = ctk.CTkButton(master=keyboardFrame, width=250, height=30, text='SPACE', font=('Comic Sans MS', 27),
                                   fg_color='whitesmoke', text_color='gray', hover_color='#EEEEEE')
            button.grid(column=columnNum, row=rowNum, pady=1, padx=1, columnspan=6)
        else:
            button = ctk.CTkButton(master=keyboardFrame, width=48, height=30, text=current, font=('Comic Sans MS', 27),
                                   fg_color='whitesmoke', text_color='gray', hover_color='#EEEEEE')
            button.grid(column=columnNum, row=rowNum, pady=1, padx=1)
        button_list.append(button)
    
    # alphabet list to assign each button to the respective letter
    # having an alphabet dict and an alphabet list seems reduntant, think of an alternative, for example, ordered dict from collections
    alphabet_list = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',' ']
    for loop in range(len(button_list)):
        button_list[loop].configure(command=lambda y=loop, x=alphabet_list[loop]: game(y,x))
    
    """
    rather complex for loop and not easy to read, it iterates over everything in button_list, 
    in this case, the letter buttons and the lambda function captures current value of alphabet_list, 
    and uses loop as index and assigns to x, esentially referencing each button with an the respective letter 
    in the list between 0 to 26, including space.

    we pass loop to x first, if we dont, all buttons would end up assigning to index 26, passing it to
    lambda as x ensures capturing current value of loop at the time the lambda function is created

    not sure if this explanation is great...
    """ 

    # Run the app
    hang.mainloop()