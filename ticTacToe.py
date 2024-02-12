"""
program: ticTacToe.py
author: Stanislav Birca, Kameron Bains

this python file acts as the interface
for the ticTacToe minigame for our
python minigame hub.
"""

def ticTacToe():  
    #-------------------Libraries-------------------
    import customtkinter as ctk
    import random

    #-------------------CTk appearance-------------------
    ctk.set_appearance_mode("Dark")
    ctk.set_default_color_theme("green") 

    #-------------------Menu window-------------------
    tic = ctk.CTk() # Reference to ticTacToe window as tic 
    window_height = 640; window_width = 400
    screen_width = tic.winfo_screenwidth()
    screen_height = tic.winfo_screenheight()
    center_x = int(screen_width/2 - window_width / 2)
    center_y = int(screen_height/2 - window_height / 2)
    tic.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
    tic.resizable(width=False, height=False)
    tic.title('TicTacToe')
    tic.iconbitmap('Resources/iconbitmap.ico')

    #-------------------Global variables-------------------
    global current; current='❌'
    global turn; turn = True
    global end; end = False

    #-------------------All functions go in below-------------------


    # start game
    def startGame():
        print('startgame func called')
        for current in (start, difficulty, firstMove):
            current.configure(state=ctk.DISABLED)
        count(3) # starts timer countdown

        # if the user starts it will call the user function first to give them their go 
        if firstMove.get() == "Me":
            user() # calls the ai function if user chose user
            print('user func called')
        elif firstMove.get() == "The AI":
            ai() # calls the ai function if user chose the AI
            print('ai func called')
        else: 
            print('random randint func called')
            result = random.randint(1,2)
            if result == 1: user(); 
            else: ai()


    # end game
    def end_game():
        print('endgame func called')
        global end; end = True
        for i in buttons:
            i.configure(state=ctk.DISABLED)
    
    # function to check win conditions
    def check_winner():
        print('check_winner called')
        pass

    # Function to process click
    def on_click(button_id):
        print('on click func called')
        global turn,current,end

        print(f"! Button {button_id} pressed !")
        buttons[button_id].configure(state=ctk.DISABLED, text=current,text_color_disabled='white',fg_color ='#539f7e')
        
        if not end:
            # this will change current to the next turn and will check a winner 
            if current == '❌':
                current = '⭕'
            else:
                current = '❌'
            
            if check_winner():
                pass
            elif current == '⭕' :
                ai()
            elif current == '❌' :
                user()
            
            """"
            i tried implementing a better solution for changing turns, dont get rid of this yet

            if firstMove.get() == 'Me':
                if current == '❌':
                    current = '⭕'
                else:
                    current = '❌'

                if current == '❌':
                    user()
                
            elif firstMove.get() == 'The AI':
                if current == '❌':
                    current = '⭕'
                else:
                    current = '❌'
                
                if current == '❌':
                    ai()
            """
                

    # uses a recursive function to display the time and the after method allows you to wait a certain amouont of time for it to update 
    def count(sec):
        print('count func called')
        if sec>0:
            timer.configure(text=f"-----------------------------  Starting in {sec} seconds  -----------------------------")
            timer.after(1000,count,sec-1)
        else :
            timer.configure(text="--------------------------------  Game started  -------------------------------------")
            for current in buttons:
                current.configure(state=ctk.NORMAL, hover_color='#106a43') # sets buttons to active after timer


    # function for the user to allow them to put their character where they want it 
    def user():
        print('user func called')
        for j,(x,y) in enumerate(positions):
            buttons[j].configure(command=lambda i=j:on_click(i))
    

    # ai function which uses a list comprehension to see the avliable spaces in the game 
    def ai():
        print('ai func called')
        available_spots = [i for i, button in enumerate(buttons) if button.cget('text') == ' ']

        #if there are any available places it uses the random choice function to select a spot 
        if available_spots:
            ai_choice = random.choice(available_spots)
            on_click(ai_choice) # feeds ai choice into on click, where button is pressed
        else:
            end_game() # ends game if no available places


    # function that will be used to assign difficulty
    def difficulty_ai():
        print('difficulty ai func called')
        pass


    #-------------------All functions go in above-------------------
        





    #-------------------Frame-------------------
    frameButtons = ctk.CTkFrame(master=tic, width=400, height=350)
    frameButtons.pack(padx=12, pady=(12,4))
    
    #-------------------Buttons-------------------
    buttons=[] 

    positions = [
        (0,0),(0,1),(0,2),
        (1,0),(1,1),(1,2),
        (2,0),(2,1),(2,2)
    ] 
    
    for i,( row ,column) in enumerate(positions):
        
        button =ctk.CTkButton(master=frameButtons, text=' ', height=116, width=116)
        button.grid(padx=(10, 2) if column == 0 else (2, 2) if 0 < column < 2 else (2, 10), pady=(10, 2) if row == 0 else (2, 2) if 0 < row < 2 else (2, 10), row=row, column=column)
        buttons.append(button)
        buttons[i].configure(state=ctk.DISABLED)

    #-------------------Timer label-------------------
    timer = ctk.CTkLabel(master=tic, text="---------------------------------------   Timer   ---------------------------------------")
    timer.pack()
    
    #-------------------Frame 2-------------------
    frameOther = ctk.CTkFrame(master=tic, width=400, height=400)
    frameOther.pack(padx=12, pady=0)

    #-------------------Choose difficulty-------------------
    ctk.CTkLabel(master=frameOther, font=('Agency FB', 42), text="Choose AI difficulty...").pack(pady=(10,1))

    difficulty_var = ctk.StringVar(value="Intermediate")
    difficulty = ctk.CTkSegmentedButton(master=frameOther, values=[" Beginner ", " Intermediate ", " Impossible "],
                                                    variable=difficulty_var,
                                                    font=('Agency FB', 27)
                                                    )
    difficulty.set(" Intermediate ")
    difficulty.pack(padx=25, pady=(0,10))

    #-------------------Who moves first-------------------
    ctk.CTkLabel(master=frameOther, font=('Agency FB', 26), text="Who moves first...              Click below to   ").pack(pady=(5,1))

    firstMove_var = ctk.StringVar(value="Random")
    firstMove = ctk.CTkComboBox(master=frameOther, values=["Me", "The AI", "Random"],
                                    variable=firstMove_var,
                                    font=('Agency FB', 27),
                                    state='readonly',
                                    dropdown_font=('Agency FB',22)
                                    )
    firstMove.set("Random")
    firstMove.pack(padx=25, pady=(0,20), side='left')

    # start button
    start = ctk.CTkButton(master=frameOther, font=('Agency FB', 27), text="Start Game",command=startGame)
    start.pack(padx=25, pady=(0,20), side='right')

    # Run the app
    tic.mainloop()