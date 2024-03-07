#using customtkinter because give more set for the appearance 
import customtkinter
from tkinter import ttk
from customtkinter import *
import tkinter as tk
from dataBase_sqlite import Database





class frameApp(customtkinter.CTk):
    def __init__(self):

        #main setup build my frame
        super().__init__()   
        self.title('Book app')
        self._set_appearance_mode('dark')
        
        #using ctkframe to create a new frame inside the main frame to be more easy to manipulate 
        frame = tk.Frame(self)
        frame.pack()
        
        # change to tk.labelframe because with the ctklabel its not inserting text 
        widget_frame = tk.LabelFrame(frame, text= "Insert Data",padx=7,pady=7)
        widget_frame.grid(row=0,column=0,sticky='ew')


        #calling class textBoxes to create them
        textBoxes.text_boxes(widget_frame,"First Name",0,0,5,5)
        textBoxes.text_boxes(widget_frame,"Last Name",1,0,5,5)
        textBoxes.text_boxes(widget_frame,"Phone",2,0,5,5)
        textBoxes.text_boxes(widget_frame,"Address",3,0,5,5)
        textBoxes.text_boxes(widget_frame,"Email",4,0,5,5)
        
       #calling class textField to create them
        textField.text_field(widget_frame,0,1,5,5,'Only accept words')
        textField.text_field(widget_frame,1,1,5,5,'Only accept words')
        textField.text_field(widget_frame,2,1,5,5,'Only accept numbers')
        textField.text_field(widget_frame,3,1,5,5,'Accept any number or words')
        textField.text_field(widget_frame,4,1,5,5,'Accept any number or words and need @')
        
        #calling our database frame
        frameDatabase.frame_database(self)
        
        
        self.mainloop()
        
class textBoxes():
    #using class to make this function more easy to use in another code parts 
    def text_boxes(self, text, row, column, padx, pady):
        #using CTkLabel from customtkinter do design your text box were we pass there arguments, and i am anchor my text to northwest and expand my text box to right and left (sticky)    
        textBox = tk.Label(self ,text=text,padx=padx,pady=pady,anchor= 'nw')
        textBox.grid(row=row,column=column,padx=padx,pady=pady,sticky='ew')  
     
class textField():
    def text_field(frame,row,column,padx,pady,textfield):
        # sourcery skip: instance-method-first-arg-name
        #using tk.Entry from tkinter to design our text box were we pass this arguments ,and expand my text box to right and left (sticky) and with my bind i am erasing all inside the textfield      
       
       
       
        field = tk.Entry(frame, width=70,fg='grey') 
        field.insert(0, textfield)
    
        field.bind("<FocusIn>", lambda e: field.delete('0','end'))
        field.grid(row=row,column=column,padx=padx,pady=pady,sticky='ew')
                
    
class frameDatabase():
      
    def frame_database(self):

        # change to tk.labelframe because with the ctklabel its not inserting text 
        frame = tk.Frame(self)
        frame.pack()
        self.dataBase1 = Database()
        
    
        
        self.data_widget_frame = tk.LabelFrame(frame, text= "Insert Data")
        self.data_widget_frame.grid(row=0,column=0,sticky='ew')

        treeScroll = ttk.Scrollbar(self.data_widget_frame)
        treeScroll.pack(side= 'right',fill='y')
        
        cols = ("First Name","Last Name", "Phone", "Address", "Email")
        self.treeview = ttk.Treeview(self.data_widget_frame, show='headings', yscrollcommand=treeScroll.set, columns=cols ,height=13,padding=5)
        self.treeview.column('First Name',width=100)
        self.treeview.column('Last Name',width=100)
        self.treeview.column('Phone',width=100)
        self.treeview.column('Address',width=100)
        self.treeview.column('Email',width=100)
        
        self.treeview.heading('First Name',text='First Name')
        self.treeview.heading('Last Name',text='Last Name')
        self.treeview.heading('Phone',text='Phone')
        self.treeview.heading('Address',text='Address')
        self.treeview.heading('Email',text='Email')
        
        
        frameDatabase.insertData(self)
        
        self.treeview.pack()
        
        treeScroll.config(command=self.treeview.yview)
     
   
    def insertData(self):
       #self.treeview.delete(*self.treeview.get_children())
       new=self.dataBase1.populateTable()
       i = -1
       for data in new:
           i=i+1
           self.treeview.insert('',i, text = new[i][1:2], values=new[i][2:7])
        
        
            
             
             
        
        

        

           
