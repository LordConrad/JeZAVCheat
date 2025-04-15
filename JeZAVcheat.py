from tkinter import*
from tkinter import ttk
import threading
from PIL import Image, ImageTk, ImageSequence 
import customtkinter
import sys
import os
from pynput import keyboard
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo
import random
import pydirectinput
import cv2
import easyocr
import numpy as np
import time
import keyboard

def resource_path(relative_path):
    """ Vrátí správnou cestu k souboru (funguje v .exe i při běhu v Pythonu) """
    if hasattr(sys, '_MEIPASS'):  # Pokud běžíme z exe, hledáme v dočasné složce
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.abspath(relative_path)

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")
def main_window():
  c = Tk()
  c.title("JeZAVcheat")
  c.config(background="#000000")
  c.iconbitmap("ico.ico")
  c.state("zoomed")
  width = c.winfo_screenwidth()
  height = c.winfo_screenheight()
  
  global First_word_waiting
  First_word_waiting = False

  Writing_Textbox = customtkinter.CTkTextbox(c, width=width*0.75, height=height*0.65,font=("Courier New",13,"bold"))
  Delay_Textbox = customtkinter.CTkTextbox(c, font=("Arial",30,"bold"), width=100,height=1)
  Speed_Textbox = customtkinter.CTkTextbox(c, font=("Arial",30,"bold"), width=60,height=1)
  Character_counter = customtkinter.CTkTextbox(c, font=("Arial",30,"bold"), width=150,height=1)
  Delay_Textbox.insert("1.0","2")
  Speed_Textbox.insert("1.0",random.randint(10,25))
  
  Title_Text = customtkinter.CTkLabel(c,text="JeZAVcheat",font=("Arial",50,"bold"))

  def vybratobr():
      global filename
      global File
      filetypes = (
          ('Všechny soubory', '*.*'),
          ('PNG soubory', '*.png')
          
      )
      File_Textbox.delete(0, "End_Counter")  # Vymazání původního textu
      filename = fd.askopenfilename(
          title='Otevřít obrázek',
          filetypes=filetypes)
      File_Textbox.insert(0,filename)
      print("letsgou")
      File = filename
      image_path = filename
      img = cv2.imread(image_path)
      print("letsgou")
      # instance text detector
      reader = easyocr.Reader(['cs'], gpu=False)
      # detect text on image
      print("letsgou")
      Text_from_Image = reader.readtext(img, detail=0,paragraph=True)
      print("letsgou")
      text = " ".join(Text_from_Image)
      global Text_to_write
      Text_to_write = text
      j=0
      global Randomizer
      Text_to_be_written = str(Writing_Textbox.get("1.0",'End_Counter-1c'))
      Randomizer = int(Speed_Textbox.get("1.0","End_Counter-1c"))
      Writing_Textbox.delete("1.0","End_Counter")
      Writing_Textbox.insert("1.0",Text_to_write)
      c.update_idletasks()
      
  def potvrdit():
      global Text_to_be_written
      global Randomizer
      global Character_typing_delay
      Character_typing_delay = float(Delay_Textbox.get("1.0","end-1c"))
      Text_to_be_written = Writing_Textbox.get("1.0","end-1c")
      Randomizer = int(Speed_Textbox.get("1.0","end-1c"))
      Character_counter.delete("1.0","end")
      Character_counter.insert("1.0",len(Text_to_be_written))
  
  def exit():
      c.destroy()
    
  def vycistit():
    Writing_Textbox.delete("1.0","end")

  def mezery():
      text_content = Writing_Textbox.get("1.0","end")  # Získání textu z widgetu
      updated_text = text_content.replace(" ", "")  # Nahrazení mezer
      Writing_Textbox.delete("1.0", "end")  # Vymazání původního textu
      Writing_Textbox.insert("1.0", updated_text)
     

  def prevratit():
      Text_to_be_written_REVERSED = Writing_Textbox.get("1.0", "end").strip()  
      Text_to_be_written_REVERSED = Text_to_be_written_REVERSED[::-1]  # Otočení textu
      Writing_Textbox.delete("1.0", "end")  # Vymazání původního textu
      Writing_Textbox.insert("1.0", Text_to_be_written_REVERSED)  # Vložení otočeného text

  def auto_type():
      global Text_to_be_written_End
      global Typing_acceleration_counter_Default
      global First_word_waiting
      for Character in Text_to_be_written:
                Typing_acceleration_counter_Default= Typing_acceleration_counter_Default +1
                print("pocitadlo - ",Typing_acceleration_counter_Default)
                print("char - ",Character)
                random.seed(time.time())
                global Delay_for_writing
                if Typing_acceleration_counter_Default < Text_to_be_written_End * 0.33:
                  Delay_for_writing = random.randint(Randomizer,Randomizer+random.randint(71,120))/120*random.randint(91,99)/101
                  print("1")
                  print(Delay_for_writing)
                  time.sleep(Delay_for_writing)

                elif Typing_acceleration_counter_Default > Text_to_be_written_End * 0.33 and Typing_acceleration_counter_Default < Text_to_be_written_End  * 0.66:
                  print("2")
                  Delay_for_writing = random.randint(Randomizer,Randomizer+random.randint(30,71))/120*random.randint(87,99)/101
                  print(Delay_for_writing)
                  time.sleep(Delay_for_writing)
                  zbylytxt = len(Text_to_be_written) - len(Text_to_be_written) * 0.66
                elif Typing_acceleration_counter_Default > Text_to_be_written_End * 0.66:
                    print("3")
                    Delay_for_writing = random.randint(Randomizer,Randomizer+random.randint(8,29))/120*random.randint(87,99)/101
                    print(Delay_for_writing)
                    time.sleep(Delay_for_writing)
                    zbylytxt = len(Text_to_be_written) - len(Text_to_be_written)
          
                if Character == "A":
                  pydirectinput.keyDown("shift")
                  pydirectinput.keyDown(Character)
                  pydirectinput.keyUp(Character)
                  pydirectinput.keyUp("shift")
                elif Character == "B":
                  pydirectinput.keyDown("shift")
                  pydirectinput.keyDown(Character)
                  pydirectinput.keyUp(Character)
                  pydirectinput.keyUp("shift")
                elif Character == "C":
                  pydirectinput.keyDown("shift")
                  pydirectinput.keyDown(Character)
                  pydirectinput.keyUp(Character)
                  pydirectinput.keyUp("shift")
                elif Character == "D":
                  pydirectinput.keyDown("shift")
                  pydirectinput.keyDown(Character)
                  pydirectinput.keyUp(Character)
                  pydirectinput.keyUp("shift")
                elif Character == "E":
                  pydirectinput.keyDown("shift")
                  pydirectinput.keyDown(Character)
                  pydirectinput.keyUp(Character)
                  pydirectinput.keyUp("shift")
                elif Character == "F":
                  pydirectinput.keyDown("shift")
                  pydirectinput.keyDown(Character)
                  pydirectinput.keyUp(Character)
                  pydirectinput.keyUp("shift")
                elif Character == "G":
                  pydirectinput.keyDown("shift")
                  pydirectinput.keyDown(Character)
                  pydirectinput.keyUp(Character)
                  pydirectinput.keyUp("shift")
                elif Character == "H":
                  pydirectinput.keyDown("shift")
                  pydirectinput.keyDown(Character)
                  pydirectinput.keyUp(Character)
                  pydirectinput.keyUp("shift")
                elif Character == "I":
                  pydirectinput.keyDown("shift")
                  pydirectinput.keyDown(Character)
                  pydirectinput.keyUp(Character)
                  pydirectinput.keyUp("shift")
                elif Character == "J":
                  pydirectinput.keyDown("shift")
                  pydirectinput.keyDown(Character)
                  pydirectinput.keyUp(Character)
                  pydirectinput.keyUp("shift")
                elif Character == "L":
                  pydirectinput.keyDown("shift")
                  pydirectinput.keyDown(Character)
                  pydirectinput.keyUp(Character)
                  pydirectinput.keyUp("shift")
                elif Character == "M":
                  pydirectinput.keyDown("shift")
                  pydirectinput.keyDown(Character)
                  pydirectinput.keyUp(Character)
                  pydirectinput.keyUp("shift")
                elif Character == "N":
                  pydirectinput.keyDown("shift")
                  pydirectinput.keyDown(Character)
                  pydirectinput.keyUp(Character)
                  pydirectinput.keyUp("shift")
                elif Character == "O":
                  pydirectinput.keyDown("shift")
                  pydirectinput.keyDown(Character)
                  pydirectinput.keyUp(Character)
                  pydirectinput.keyUp("shift")
                elif Character == "P":
                  pydirectinput.keyDown("shift")
                  pydirectinput.keyDown(Character)
                  pydirectinput.keyUp(Character)
                  pydirectinput.keyUp("shift")
                elif Character == "Q":
                  pydirectinput.keyDown("shift")
                  pydirectinput.keyDown(Character)
                  pydirectinput.keyUp(Character)
                  pydirectinput.keyUp("shift")
                elif Character == "R":
                  pydirectinput.keyDown("shift")
                  pydirectinput.keyDown(Character)
                  pydirectinput.keyUp(Character)
                  pydirectinput.keyUp("shift")
                elif Character == "S":
                  pydirectinput.keyDown("shift")
                  pydirectinput.keyDown(Character)
                  pydirectinput.keyUp(Character)
                  pydirectinput.keyUp("shift")
                elif Character == "T":
                  pydirectinput.keyDown("shift")
                  pydirectinput.keyDown(Character)
                  pydirectinput.keyUp(Character)
                  pydirectinput.keyUp("shift")
                elif Character == "U":
                  pydirectinput.keyDown("shift")
                  pydirectinput.keyDown(Character)
                  pydirectinput.keyUp(Character)
                  pydirectinput.keyUp("shift")
                elif Character == "V":
                  pydirectinput.keyDown("shift")
                  pydirectinput.keyDown(Character)
                  pydirectinput.keyUp(Character)
                  pydirectinput.keyUp("shift")
                elif Character == "W":
                  pydirectinput.keyDown("shift")
                  pydirectinput.keyDown(Character)
                  pydirectinput.keyUp(Character)
                  pydirectinput.keyUp("shift")
                elif Character == "X":
                  pydirectinput.keyDown("shift")
                  pydirectinput.keyDown(Character)
                  pydirectinput.keyUp(Character)
                  pydirectinput.keyUp("shift")
                elif Character == "Y":
                  pydirectinput.keyDown("shift")
                  pydirectinput.keyDown(Character)
                  pydirectinput.keyUp(Character)
                  pydirectinput.keyUp("shift")
                elif Character == "Z":
                  pydirectinput.keyDown("shift")
                  pydirectinput.keyDown(Character)
                  pydirectinput.keyUp(Character)
                  pydirectinput.keyUp("shift")
                elif Character == "a":
                  pydirectinput.keyDown(Character)
                  pydirectinput.keyUp(Character)
                elif Character == "b":
                  pydirectinput.keyDown(Character)
                  pydirectinput.keyUp(Character)
                elif Character == "c":
                  pydirectinput.keyDown(Character)
                  pydirectinput.keyUp(Character)
                elif Character == "d":
                  pydirectinput.keyDown(Character)
                  pydirectinput.keyUp(Character)
                elif Character == "e":
                  pydirectinput.keyDown(Character)
                  pydirectinput.keyUp(Character)
                elif Character == "f":
                  pydirectinput.keyDown(Character)
                  pydirectinput.keyUp(Character)
                elif Character == "g":
                  pydirectinput.keyDown(Character)
                  pydirectinput.keyUp(Character)
                elif Character == "h":
                  pydirectinput.keyDown(Character)
                  pydirectinput.keyUp(Character)
                elif Character == "i":
                  pydirectinput.keyDown(Character)
                  pydirectinput.keyUp(Character)
                elif Character == "j":
                  pydirectinput.keyDown(Character)
                  pydirectinput.keyUp(Character)
                elif Character == "k":
                  pydirectinput.keyDown(Character)
                  pydirectinput.keyUp(Character)
                elif Character == "l":
                  pydirectinput.keyDown(Character)
                  pydirectinput.keyUp(Character)
                elif Character == "m":
                  pydirectinput.keyDown(Character)
                  pydirectinput.keyUp(Character)
                elif Character == "n":
                  pydirectinput.keyDown(Character)
                  pydirectinput.keyUp(Character)
                elif Character == "o":
                  pydirectinput.keyDown(Character)
                  pydirectinput.keyUp(Character)
                elif Character == "p":
                  pydirectinput.keyDown(Character)
                  pydirectinput.keyUp(Character)
                elif Character == "q":
                  pydirectinput.keyDown(Character)
                  pydirectinput.keyUp(Character)
                elif Character == "r":
                  pydirectinput.keyDown(Character)
                  pydirectinput.keyUp(Character)
                elif Character == "s":
                  pydirectinput.keyDown(Character)
                  pydirectinput.keyUp(Character)
                elif Character == "t":
                  pydirectinput.keyDown(Character)
                  pydirectinput.keyUp(Character)
                elif Character == "u":
                  pydirectinput.keyDown(Character)
                  pydirectinput.keyUp(Character)
                elif Character == "v":
                  pydirectinput.keyDown(Character)
                  pydirectinput.keyUp(Character)
                elif Character == "w":
                  pydirectinput.keyDown(Character)
                  pydirectinput.keyUp(Character)
                elif Character == "x":
                  pydirectinput.keyDown(Character)
                  pydirectinput.keyUp(Character)
                elif Character == "y":
                  pydirectinput.keyDown("z")
                  pydirectinput.keyUp("z")
                elif Character == "z":
                  pydirectinput.keyDown("y")
                  pydirectinput.keyUp("y")
                elif Character == "q":
                  pydirectinput.keyDown(Character)
                  pydirectinput.keyUp(Character)
                elif Character == "ě":
                    pydirectinput.press('2')
                elif Character == "š":
                    pydirectinput.press('3')
                elif Character == "č":
                    pydirectinput.press('4')
                elif Character == "ř":
                    pydirectinput.press('5')
                elif Character == "ž":
                    pydirectinput.press('6')
                elif Character == "ý":
                    pydirectinput.press('7')
                elif Character == "á":
                    pydirectinput.press('8')
                elif Character == "í":
                    pydirectinput.press('9')
                elif Character == "é":
                    pydirectinput.press('0')
                elif Character == "Ě":
                    pydirectinput.keyDown("capslock")
                    pydirectinput.keyUp("capslock")
                    pydirectinput.keyDown('2')
                    pydirectinput.keyDown("capslock")
                    pydirectinput.keyUp("capslock")
                elif Character == "Š":
                    pydirectinput.keyDown("capslock")
                    pydirectinput.keyUp("capslock")
                    pydirectinput.keyDown('3')
                    pydirectinput.keyDown("capslock")
                    pydirectinput.keyUp("capslock")
                elif Character == "Č":
                    pydirectinput.keyDown("capslock")
                    pydirectinput.keyUp("capslock")
                    pydirectinput.keyDown('4')
                    pydirectinput.keyDown("capslock")
                    pydirectinput.keyUp("capslock")
                elif Character == "Ř":
                    pydirectinput.keyDown("capslock")
                    pydirectinput.keyUp("capslock")
                    pydirectinput.keyDown('5')
                    pydirectinput.keyDown("capslock")
                    pydirectinput.keyUp("capslock")
                elif Character == "Ž":
                    pydirectinput.keyDown("capslock")
                    pydirectinput.keyUp("capslock")
                    pydirectinput.keyDown('6')
                    pydirectinput.keyDown("capslock")
                    pydirectinput.keyUp("capslock")
                elif Character == "Ý":
                    pydirectinput.keyDown("capslock")
                    pydirectinput.keyUp("capslock")
                    pydirectinput.keyDown('7')
                    pydirectinput.keyDown("capslock")
                    pydirectinput.keyUp("capslock")
                elif Character == "Á":
                    pydirectinput.keyDown("capslock")
                    pydirectinput.keyUp("capslock")
                    pydirectinput.keyDown('8')
                    pydirectinput.keyDown("capslock")
                    pydirectinput.keyUp("capslock")
                elif Character == "Í":
                    pydirectinput.keyDown("capslock")
                    pydirectinput.keyUp("capslock")
                    pydirectinput.keyDown('9')
                    pydirectinput.keyDown("capslock")
                    pydirectinput.keyUp("capslock")
                elif Character == "É":
                    pydirectinput.keyDown("capslock")
                    pydirectinput.keyUp("capslock")
                    pydirectinput.keyDown('0')
                    pydirectinput.keyDown("capslock")
                    pydirectinput.keyUp("capslock")
                elif Character == ".":
                  pydirectinput.keyDown(".")
                elif Character == ",":
                  pydirectinput.keyDown(",")
                elif Character == "$":
                  pydirectinput.keyDown("enter")
                elif Character == "-":
                  pydirectinput.keyUp("shift")
                  pydirectinput.keyDown("/")  
                elif Character == "ť":
                  pydirectinput.keyDown("shift")
                  pydirectinput.keyDown("=")
                  pydirectinput.keyUp("shift")
                  pydirectinput.keyDown("t")
                elif Character == "ď":
                  pydirectinput.keyDown("shift")
                  pydirectinput.keyDown("=")
                  pydirectinput.keyUp("shift")
                  pydirectinput.keyDown("d")
                elif Character == "ň":
                  pydirectinput.keyDown("shift")
                  pydirectinput.keyDown("=")
                  pydirectinput.keyUp("shift")
                  pydirectinput.keyDown("n")
                  pydirectinput.keyUp("n")
                elif Character == "Ň":
                  pydirectinput.keyDown("shift")
                  pydirectinput.keyDown("=")
                  pydirectinput.keyDown("n")
                  pydirectinput.keyUp("n")
                  pydirectinput.keyUp("shift")
                elif Character == "Ď":
                  pydirectinput.keyDown("shift")
                  pydirectinput.keyDown("=")
                  pydirectinput.keyDown("n")
                  pydirectinput.keyUp("shift")
                elif Character == "Ť":
                  pydirectinput.keyDown("shift")
                  pydirectinput.keyDown("=")
                  pydirectinput.keyDown("T")
                  pydirectinput.keyUp("shift")
                elif Character == "ú":
                  pydirectinput.keyDown("[")
                elif Character == "ů":
                  pydirectinput.keyDown(";")
                else:
                  pydirectinput.keyDown(Character)
                  pydirectinput.keyUp(Character)
      First_word_waiting = False

  def Write():
    global Text_to_be_written
    global Text_to_be_written_End
    global Typing_acceleration_counter_Default
    global First_word_waiting
    First_word_waiting = True

    Text_to_be_written = Text_to_be_written.split(" ")
    Text_to_be_written = " ".join(Text_to_be_written[1:])
    Text_to_be_written = Text_to_be_written[::-1]
    Text_to_be_written = Text_to_be_written.split(" ")
    Text_to_be_written = " ".join(Text_to_be_written[1:])
    Text_to_be_written = Text_to_be_written[::-1]
    
    Typing_acceleration_counter_Default = 0
    Text_to_be_written_End = len(Text_to_be_written)
    if First_word_waiting == True:
       keyboard.wait("space")
       auto_type()
  
  keyboard.add_hotkey("f2",Write)

  btnpotvrdit = customtkinter.CTkButton(c,text="Potvrdit",command=potvrdit)
  btnpsat = customtkinter.CTkButton(c,text="Psát (F2)",command=Write)
  btnexit = customtkinter.CTkButton(c,text="Ukončit",command=exit)
  btnvycistit = customtkinter.CTkButton(c,text="Vyčistit pole",command=vycistit)
  btnmez = customtkinter.CTkButton(c,text="Odstranit mezery",command=mezery)
  btnopak = customtkinter.CTkButton(c,text="Převrátit pořadí",command=prevratit)
  File_Textbox = customtkinter.CTkEntry(c, width=135,height=1,state="normal")
  delayvyber = customtkinter.CTkLabel(c,text="Začátek psaní (s)")
  znakytext = customtkinter.CTkLabel(c,text="Počet znaků")
  rychlostvyber = customtkinter.CTkLabel(c,text="Rychlost (od - do)")
  btnvyber = customtkinter.CTkButton(c,text="Vybrat obrázek",command=vybratobr)


  File_Textbox.place(x=width*0.83,y=height*0.20)
  btnvyber.place(x=width*0.83,y=height*0.25)
  btnvycistit.place(x=width*0.83,y=height*0.35)
  btnmez.place(x=width*0.83,y=height*0.40)
  btnopak.place(x=width*0.83,y=height*0.45)
  btnpsat.place(x=width*0.83,y=height*0.70)
  btnpotvrdit.place(x=width*0.83,y=height*0.65)
  btnexit.place(x=width*0.83,y=height*0.85)
  Title_Text.place(x=width/2-width/10,y=0)
  Writing_Textbox.place(x=width/100,y=height*0.2)
  Delay_Textbox.place(x=width*0.02,y=height*0.02)
  Speed_Textbox.place(x=width*0.27,y=height*0.02)
  Character_counter.place(x=width*0.65,y=height*0.02)
  znakytext.place(x=width*0.65,y=height*0.1)
  delayvyber.place(x=width*0.02,y=height*0.1)
  rychlostvyber.place(x=width*0.14,y=height*0.1)

  c.mainloop()
def typing_analyzer():
   analyzer_c = Tk()
   analyzer_c.iconbitmap("ico.ico")
   analyzer_c.title("Měření času mezi klávesami")
   analyzer_c.geometry()
   analyzer_c.resizable(False, False)
   analyzer_c.mainloop()
GIF_WIDTH = 390  # Změň na požadovanou šířku
GIF_HEIGHT = 220  # Změň na požadovanou výšku

main_window()