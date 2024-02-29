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

        textBox = CTkLabel(self,text=("First Name"))
        textBox.grid(row=0,column=0,padx=5,pady=5)
        textField = CTkTextbox(self)
        textField.grid(row=0,column=2,padx=5,pady=5)
        
        
        
        
        
        
        
        #add_button = CTkButton(master=self,text=("Update"))
        #add_button.grid(row=2,column=60)
        

        self.mainloop()
        
    

