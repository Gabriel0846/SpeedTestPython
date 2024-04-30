from tkinter import *
from PIL import Image, ImageTk
import speedtest

co0 = "#f0f3f5"  # Preto
co1 = "#feffff"  # Branco
co2 = "#3fb5a3"  # Verde
co3 = "#fc766d"  # Vermelho
co4 = "#403d3d"  # Preto
co5 = "#4a88e8"  # Azul

janela = Tk()
janela.title("")
janela.geometry('350x200')
janela.configure(background=co1)
janela.resizable(width=False, height=False)

frame_logo = Frame(janela, width=350, height=60, bg=co1)
frame_logo.grid(row=0, column=0, pady=1, padx=0, sticky=NSEW)

frame_corpo = Frame(janela, width=350, height=140, bg=co1)
frame_corpo.grid(row=1, column=0, pady=1, padx=0, sticky=NSEW)

imagem = Image.open('speed.png')
imagem_resized = imagem.resize((55, 60))
imagem_tk = ImageTk.PhotoImage(imagem_resized)

l_logo_imagem = Label(frame_logo, height=60, image=imagem_tk, compound=LEFT, padx=10, anchor='nw', font=('Ivy 16 bold'), bg=co1, fg=co3)
l_logo_imagem.place(x=18, y=0)
l_logo_nome = Label(frame_logo, text='Internet Speed Test', height=60, padx=10, anchor=NE, font=('Ivy 20'), bg=co1, fg=co4)
l_logo_nome.place(x=75, y=10)

l_logo_linha = Label(frame_logo, width=350, anchor=NW, font=('Ivy 1'), bg=co2)
l_logo_linha.place(x=0, y=57)

def main():
    speed = speedtest.Speedtest()
    download = f"{'{:.2f}'.format(speed.download()/1024/1024)}"
    upload = f"{'{:.2f}'.format(speed.upload()/1024/1024)}"

    l_download['text'] = download
    l_upload['text'] = upload

    botao_testar['text'] = 'Testar Novamente'
    botao_testar.place(x=115, y=100)

l_download = Label(frame_corpo, text='', anchor=NW, font=('arial 28'), bg=co1, fg=co4)
l_download.place(x=30, y=25)
l_download_mb = Label(frame_corpo, text='Mbps Download', anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
l_download_mb.place(x=30, y=70)

imagem_setas = Image.open('setas.png')
imagem_setas = imagem_setas.resize((70, 80))
imagem_setas = ImageTk.PhotoImage(imagem_setas)
l_logo_imagem = Label(frame_corpo, height=85, image=imagem_setas, compound=LEFT, padx=10, anchor='nw', font=('Ivy 16 bold'), bg=co1, fg=co3)
l_logo_imagem.place(x=142.5, y=20)

l_upload = Label(frame_corpo, text='', anchor=NW, font=('arial 28'), bg=co1, fg=co4)
l_upload.place(x=230, y=25)
l_upload_mb = Label(frame_corpo, text='Mbps Upload', anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
l_upload_mb.place(x=230, y=70)

botao_testar = Button(frame_corpo, command=main, text='Iniciar Teste', font=('Ivy 10 bold'), relief=RAISED, overrelief=RIDGE, bg=co5, fg=co1)
botao_testar.place(x=134, y=100)

janela.mainloop()
