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
    from PIL import Image

    #-------------------Import from other files-------------------
    import mainMenu # used as parent window for CTkToplevel

    #-------------------CTk appearance-------------------
    ctk.set_appearance_mode("Dark")
    ctk.set_default_color_theme("green")

    #-------------------Hangman window-------------------
    hang = ctk.CTkToplevel() # Reference to hangman window as hang, NEEDS TO BE TOPLEVEL AS PIL CAN ONLY RENDER ONE WINDOW AT A TIME!
    window_height = 550; window_width = 850
    screen_width = hang.winfo_screenwidth()
    screen_height = hang.winfo_screenheight()
    center_x = int(screen_width/2 - window_width / 2)
    center_y = int(screen_height/2 - window_height / 2)
    hang.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
    hang.resizable(width=False, height=False)
    hang.title('Hangman')
    hang.iconbitmap('Resources/iconbitmap.ico')

    #-------------------All functions go in below-------------------

    def progressHangman():
        hangmanList = ('Resources\hang0.png','Resources\hang1.png',
                       'Resources\hang2.png','Resources\hang3.png',
                       'Resources\hang4.png','Resources\hang5.png',
                       'Resources\hang6.png','Resources\hang7.png',
                       'Resources\hang8.png','Resources\hang9.png',
                       'Resources\hang10.png')


    #-------------------All functions go in above-------------------

    
    #-------------------Left frame and right frame-------------------
    hangmanFrame = ctk.CTkFrame(master=hang, height=526, width=407, fg_color='#EEEEEE')
    hangmanFrame.grid_propagate(False); hangmanFrame.grid(padx=12,pady=12, column=0,row=0, sticky='w')

    wordFrame = ctk.CTkFrame(master=hang, height=526, width=407, fg_color='#EEEEEE')
    wordFrame.grid_propagate(False); wordFrame.grid(padx=(0,12),pady=12, column=1,row=0, sticky='e')

    #-------------------Hangman-------------------
    hangmanImage = ctk.CTkImage(light_image=Image.open('Resources/hang0.png'),
                                dark_image=Image.open('Resources/hang0.png'),
                                size=(407, 526))
    
    hangmanImageLabel = ctk.CTkLabel(master=hangmanFrame, image=hangmanImage,text='')
    hangmanImageLabel.pack()

    #-------------------Creating buttons using for loop-------------------
    alphabet = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','SPACE']
    iteration = 0; columnNum = -1
    for current in alphabet:
        iteration += 1; columnNum +=1
        if iteration <= 8: rowNum = 0
        elif iteration <= 16: rowNum = 1
        elif iteration <= 24: rowNum = 2 
        else: rowNum = 3
        if columnNum >= 8: columnNum = 0
        print (current)

        if current == 'SPACE':
            ctk.CTkButton(master=wordFrame, width=250,height=30, text=current, font=('Comic Sans MS', 27), fg_color='white',
                        text_color='gray', hover_color='#EEEEEE').grid(column=columnNum, row=rowNum, pady=1,padx=1, columnspan=6)
        else:
            ctk.CTkButton(master=wordFrame, width=48,height=30, text=current, font=('Comic Sans MS', 27), fg_color='white',
                        text_color='gray', hover_color='#EEEEEE').grid(column=columnNum, row=rowNum, pady=1,padx=1)

    #Run the app
    hang.mainloop()

