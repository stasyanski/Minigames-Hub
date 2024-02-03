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
    
    #-------------------CTk appearance-------------------
    ctk.set_appearance_mode("Dark")
    ctk.set_default_color_theme("green") 

    #-------------------Menu window-------------------
    tic = ctk.CTk() # Reference to menu window as 'menu' 
    window_height = 660; window_width = 400
    screen_width = tic.winfo_screenwidth()
    screen_height = tic.winfo_screenheight()
    center_x = int(screen_width/2 - window_width / 2)
    center_y = int(screen_height/2 - window_height / 2)
    tic.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
    tic.resizable(width=False, height=False)
    tic.title('TicTacToe')
    tic.iconbitmap('Resources/iconbitmap.ico')



    #-------------------All functions go in below-------------------


    # Function to process click
    def on_click (button_id):
        # buttons[button_id].configure(state=ctk.DISABLED)
        buttons[button_id].configure(state=ctk.DISABLED)
        print(f"button{button_id+1} pressed")
        user()
        buttons[button_id].configure(text=button_symbols[button_id])

    # uses a recursive function to display the time and the after method allows you to wait a certain amouont of time for it to update 
    def count(sec):
        if sec>0:
            timer.configure(text=f"-----------------------------  Starting in {sec} seconds  -----------------------------")
            timer.after(1000,count,sec-1)
        else :
            timer.configure(text="--------------------------------  Game started  -------------------------------------")
    
    # needs to make this function only run when the user has selected a difficultity 
    def startGame():
        start.configure(state=ctk.DISABLED)
        sec = 3
        
        count(sec)
        for i in buttons:
            i.configure(state=ctk.ACTIVE)
        return True
          #need to fix why it is crashing the program  and make it so the buttons become active again
    
    # this function will be what decides whos turn it is and what their value is x or o
    def user():
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
    
    button_symbols = ['❌', '⭕', '❌', '⭕', '❌', '⭕', '❌', '⭕', '❌']
  
    for i,( row ,column) in enumerate(positions):
        button =ctk.CTkButton(master=frameButtons, text=' ', height=116, width=116, command=lambda i=i:on_click(i))
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
    difficulty.pack(padx=25, pady=(0,10))

    #-------------------Who moves first-------------------
    ctk.CTkLabel(master=frameOther, font=('Agency FB', 42), text="Who moves first...").pack(pady=(5,1))
    # ! this button needs aligning to left side and maybe font made smaller.

    firstMove_var = ctk.StringVar(value="Random")
    firstMove = ctk.CTkComboBox(master=frameOther, values=["Me", "The AI", "Random"],
                                    variable=firstMove_var,
                                    font=('Agency FB', 27)
                                    )
    firstMove.set("Random")
    firstMove.pack(padx=25, pady=(0,20), side='left')

    # start button
    start = ctk.CTkButton(master=frameOther, font=('Agency FB', 27), text="Start Game",command=startGame)
    start.pack(padx=25, pady=(0,20), side='right')

    # Run the app
    tic.mainloop()