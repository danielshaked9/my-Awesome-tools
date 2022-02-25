import math
import numpy as np
from numpy.core.fromnumeric import shape
import pandas as pd

import tkinter as tk


class particle():
    def __init__(self,charge,x,y):
        self.charge=charge
        self.x=x
        self.y=y
        


    



class Application(tk.Frame):
    def __init__(self,master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.mouseX=None
        self.mouseY=None
        self.first_coord=None
        self.second_coord=None
        self.create_canvas()
        self.canvas.bind('<Button-1>',self.on_click)
        
        
    
    def on_click(self, event):
        if self.first_coord is None:  
            if self.first_coord is None:
                self.first_coord=[event.x,event.y]

                print("first click")
                print(self.first_coord)
                
                


            else: 
                self.first_coord=None

        else:
            #self.second_coord = self.click_to_center(event)
            self.second_coord=[event.x,event.y]

            print("second click")
            print(self.second_coord)
            self.first_coord=None
                  
   
    def create_canvas(self):
        self.canvas=tk.Canvas(self,width=450,height=450)         
        self.canvas.create_polygon(10,10,20,20,30,30,40,40)
                        
        
            
        
        
        
        
        
            
        
        self.canvas.pack(side="top")
        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=root.destroy)
        self.quit.pack(side="bottom")



        

root = tk.Tk()
app = Application(master=root)
app.mainloop()