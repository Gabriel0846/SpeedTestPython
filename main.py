from tkinter import*

co0 = "#f0f3f5"  # Preta
co1 = "#feffff"  # branca
co2 = "#3fb5a3"  # verde
co3 = "#fc766d"  # vermelha / red
co4 = "#403d3d"   # preta / black
co5 = "#4a88e8"  # Azul / Bblue

janela = Tk ()
janela.title ("")
janela.geometry('350x200')
janela.configure(background=co1)
janela.resizable(width=FALSE, height=FALSE)

frame_logo = Frame(janela, width=350, height=60, bg=co2)
frame_logo.grid(row=0, column=0, pady=1, padx=0, sticky=NSEW)

frame_corpo = Frame(janela, width=350, height=140, bg=co2)
frame_corpo.grid(row=1, column=0, pady=1, padx=0, sticky=NSEW)

janela.mainloop()