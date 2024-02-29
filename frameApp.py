#using customtkinter because give more set for the appearance 
import customtkinter
from tkinter import *
from customtkinter import *
import tkinter as tk

class frameApp(customtkinter.CTk):
    def __init__(self):
        
        #main setup build my frame
        super().__init__()   
        self.title('Book app')
        self.geometry('600x600')
        self._set_appearance_mode('dark')
        self.minsize(600,600)

        textBoxes.text_boxes(self,"First Name",0,0,5,5)
        textBoxes.text_boxes(self,"Last Name",1,0,5,5)
        textBoxes.text_boxes(self,"Phone",2,0,5,5)
        textBoxes.text_boxes(self,"Address",3,0,5,5)
        textBoxes.text_boxes(self,"Email",4,0,5,5)
        self.mainloop()
        
class textBoxes():
    def text_boxes(self, text, row, column, padx, pady):     
        textBox = CTkLabel(self ,text=(text),padx=padx,pady=pady, width=70,height=5)
        textBox.grid(row=row,column=column,padx=padx,pady=pady)  
     
        
    

