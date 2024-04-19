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
    from CTkMessagebox import CTkMessagebox

    #-------------------CTk appearance-------------------
    ctk.set_appearance_mode("Dark")
    ctk.set_default_color_theme("green") 

    #-------------------Global variables-------------------
    global current; current='❌'

    #-------------------Menu window-------------------
    tic = ctk.CTk() # Reference to ticTacToe window as tic 
    window_height = 510; window_width = 400
    screen_width = tic.winfo_screenwidth()
    screen_height = tic.winfo_screenheight()
    center_x = int(screen_width/2 - window_width / 2)
    center_y = int(screen_height/2 - window_height / 2)
    tic.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
    tic.resizable(width=False, height=False)
    tic.title('TicTacToe')
    tic.iconbitmap('Resources/iconbitmap.ico')

    #-------------------All functions go in below-------------------


    # start game
    def startGame():
        for current in buttons:
            start.configure(state=ctk.DISABLED)
            current.configure(state=ctk.DISABLED)
        count(3) # starts timer countdown

    # end game
    def end_game():
        for i in buttons:
            i.configure(state=ctk.DISABLED)
        timer.configure(text="--------------------------------  Game Over  -------------------------------------")
        CTkMessagebox(tic, title='Game Over', message='Game Over!')
    
    # Function to check win conditions
    def check_winner():
        # Check rows
        for i in range(3):
            if buttons[i*3].cget('text') == buttons[i*3+1].cget('text') == buttons[i*3+2].cget('text') != ' ':
                return end_game()

        # Check columns
        for i in range(3):
            if buttons[i].cget('text') == buttons[i+3].cget('text') == buttons[i+6].cget('text') != ' ':
                return end_game()

        # Check diagonals
        if buttons[0].cget('text') == buttons[4].cget('text') == buttons[8].cget('text') != ' ':
            return end_game()
        if buttons[2].cget('text') == buttons[4].cget('text') == buttons[6].cget('text') != ' ':
            return end_game()

        return None

    # Function to process click
    def on_click(button_id):
        global turn,current,end

        print(f"! Button {button_id} pressed !")
        buttons[button_id].configure(state=ctk.DISABLED, text=current,text_color_disabled='white',fg_color ='#539f7e')
        check_winner()

        if current == '❌':
            current = '⭕'
            timer.configure(text="-------------------------------  Player 2 Move  ------------------------------------")
        else:
            current = '❌'
            timer.configure(text="-------------------------------  Player 1 Move  ------------------------------------")
                

    # Uses a recursive function to display the time and the after method allows you to wait a certain amouont of time for it to update 
    def count(sec):
        if sec>0:
            timer.configure(text=f"-----------------------------  Starting in {sec} seconds  -----------------------------")
            timer.after(1000,count,sec-1)
        else :
            timer.configure(text="-------------------------------  Player 1 Move  ------------------------------------")
            for current in buttons:
                current.configure(state=ctk.NORMAL, hover_color='#106a43') # sets buttons to active after timer

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
    
    for i,(row,column) in enumerate(positions):
        
        button =ctk.CTkButton(master=frameButtons, text=' ', height=116, width=116)
        button.grid(padx=(10, 2) if column == 0 else (2, 2) if 0 < column < 2 else (2, 10), pady=(10, 2) if row == 0 else (2, 2) if 0 < row < 2 else (2, 10), row=row, column=column)
        buttons.append(button)
        buttons[i].configure(state=ctk.DISABLED)
    
    # Function to assign signals to buttons
    for j,(x,y) in enumerate(positions):
        buttons[j].configure(command=lambda i=j:on_click(i))
    
    #-------------------Timer label-------------------
    timer = ctk.CTkLabel(master=tic, text="---------------------------------------   Timer   ---------------------------------------")
    timer.pack()
    
    #-------------------Frame 2-------------------
    frameOther = ctk.CTkFrame(master=tic, width=400, height=400)
    frameOther.pack(padx=12, pady=0)

    # start button
    start = ctk.CTkButton(master=frameOther, font=('Agency FB', 27), text="Start Game",command=startGame)
    start.pack(padx=25, pady=(20,20), side='right')

    # Run the app
    tic.mainloop()