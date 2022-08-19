# -*- coding: utf-8 -*-
"""
Created on Fri Aug 19 13:42:26 2022

@author: Dell
"""


from tkinter import*
from PIL import Image , ImageTk
from datetime import datetime
# to implement the date and time concepts
import pytz
# to extract the correct time from different timezones
import time
# to run app continuosly from begining of time , in seconds.

root = Tk()
root.geometry("1000x1000")
map_india = ImageTk.PhotoImage(Image.open("india.jpg"))
map_usa = ImageTk.PhotoImage(Image.open("usa.jpg"))
map_australia = ImageTk.PhotoImage(Image.open("australia.jpg"))
map_japan = ImageTk.PhotoImage(Image.open("japan.jpg"))

# India 
# Label for the country name
india_label = Label(root , text = "India")
india_label.place(relx = 0.2 , rely = 0.05 , anchor = CENTER)
# label for the image of clock
india_img = Label(root  , image = map_india)
india_img.place(relx = 0.2 , rely = 0.3 , anchor = CENTER)
# label to display the clock timing
india_time = Label(root )
india_time.place(relx = 0.2 , rely = 0.5 , anchor  = CENTER)

# USA 
# Label for the country name
usa_label = Label(root , text = "USA")
usa_label.place(relx = 0.7, rely = 0.05 , anchor = CENTER)
# label for the image of clock
us_img = Label(root  , image = map_usa)
us_img.place(relx = 0.7 , rely = 0.3 , anchor = CENTER)
# label to display the clock timing
usa_time = Label(root )
usa_time.place(relx = 0.7 , rely = 0.5 , anchor  = CENTER)
australia_label = Label(root , text = "Australia")
australia_label.place(relx = 0.2 , rely = 0.55 , anchor = CENTER)
# label for the image of clock
australia_img = Label(root  , image = map_australia)
australia_img.place(relx = 0.2 , rely = 0.75 , anchor = CENTER)
# label to display the clock timing
australia_time = Label(root )
australia_time.place(relx = 0.2 , rely = 0.90 , anchor  = CENTER)
japan_label = Label(root , text = "Japan")
japan_label.place(relx = 0.7 , rely = 0.55, anchor = CENTER)
# label for the image of clock
japan_img = Label(root  , image = map_japan)
japan_img.place(relx = 0.7 , rely = 0.75 , anchor = CENTER)
# label to display the clock timing
japan_time = Label(root )
japan_time.place(relx = 0.7 , rely = 0.90 , anchor  = CENTER)
# two classes for india and usa
class India():
    # to access this function using the object of the class in which the function is created
    # we will pass the parameter self to this function
    def times(self):
        home = pytz.timezone("Asia/Kolkata")
        # to extract the current time of the countries 
        # pytz is the module which extracts the timezone of various countries
        # timezone() accepts the parameter timezone
        # we save this timezone in a variable(home)
        local_time = datetime.now(home)
        # after extracting the timezone we will extract the current time from this timezone
        # datetime() will return the current time for that country
        # we pass the parameter(home) which hold the timezone
        current_time = local_time.strftime("%H:%M:%S")
        # strftime() - "string from time" converts tme into proper format
        india_time["text"] = "Time : " + current_time
        india_time.after(200 , self.times)
        # as we want the function to be called again and again we use the after function  
        # this helps in keeping the time continuously changing
        # Syntax - <variable_name>.after(delay  , function_name)
        # Delay  - in how many seconds do you want to repeat calling the function
        # function_name - which has to be called again and agian
        # Here , after every 200 miliseconds it is calling the self.times()
        
class USA():
    # to access this function using the object of the class in which the function is created
    # we will pass the parameter self to this function
    def times(self):
        home = pytz.timezone("US/Central")
        # to extract the current time of the countries 
        # pytz is the module which extracts the timezone of various countries
        # timezone() accepts the parameter timezone
        # we save this timezone in a variable(home)
        local_time = datetime.now(home)
        # after extracting the timezone we will extract the current time from this timezone
        # datetime() will return the current time for that country
        # we pass the parameter(home) which hold the timezone
        current_time = local_time.strftime("%H:%M:%S")
        # strftime() - "string from time" converts tme into proper format
        usa_time["text"] = "Time : " + current_time
        usa_time.after(200 , self.times)
        # as we want the function to be called again and again we use the after function  
        # this helps in keeping the time continuously changing
        # Syntax - <variable_name>.after(delay  , function_name)
        # Delay  - in how many seconds do you want to repeat calling the function
        # function_name - which has to be called again and agian
        # Here , after every 200 miliseconds it is calling the self.times()
        
class Australia():
    # to access this function using the object of the class in which the function is created
    # we will pass the parameter self to this function
    def times(self):
        home = pytz.timezone("Australia/ACT")
        # to extract the current time of the countries 
        # pytz is the module which extracts the timezone of various countries
        # timezone() accepts the parameter timezone
        # we save this timezone in a variable(home)
        local_time = datetime.now(home)
        # after extracting the timezone we will extract the current time from this timezone
        # datetime() will return the current time for that country
        # we pass the parameter(home) which hold the timezone
        current_time = local_time.strftime("%H:%M:%S")
        # strftime() - "string from time" converts tme into proper format
        australia_time["text"] = "Time : " + current_time
        australia_time.after(200 , self.times)
        # as we want the function to be called again and again we use the after function  
        # this helps in keeping the time continuously changing
        # Syntax - <variable_name>.after(delay  , function_name)
        # Delay  - in how many seconds do you want to repeat calling the function
        # function_name - which has to be called again and agian
        # Here , after every 200 miliseconds it is calling the self.times() 
        
class Japan():
    # to access this function using the object of the class in which the function is created
    # we will pass the parameter self to this function
    def times(self):
        home = pytz.timezone("Japan")
        # to extract the current time of the countries 
        # pytz is the module which extracts the timezone of various countries
        # timezone() accepts the parameter timezone
        # we save this timezone in a variable(home)
        local_time = datetime.now(home)
        # after extracting the timezone we will extract the current time from this timezone
        # datetime() will return the current time for that country
        # we pass the parameter(home) which hold the timezone
        current_time = local_time.strftime("%H:%M:%S")
        # strftime() - "string from time" converts tme into proper format
        japan_time["text"] = "Time : " + current_time
        japan_time.after(200 , self.times)
        # as we want the function to be called again and again we use the after function  
        # this helps in keeping the time continuously changing
        # Syntax - <variable_name>.after(delay  , function_name)
        # Delay  - in how many seconds do you want to repeat calling the function
        # function_name - which has to be called again and agian
        # Here , after every 200 miliseconds it is calling the self.times()        
        

obj_india = India()
obj_usa = USA()
obj_australia = Australia()
obj_japan = Japan()

btn_india_time = Button(root , text = "Show time" , command = obj_india.times) 
btn_india_time.place(relx = 0.2 , rely = 0.45 , anchor = CENTER)       
btn_us_time = Button(root , text = "Show time" , command = obj_usa.times) 
btn_us_time.place(relx = 0.7 , rely = 0.45 , anchor = CENTER)
btn_australia_time = Button(root , text = "Show time" , command = obj_australia.times) 
btn_australia_time.place(relx = 0.2 , rely = 0.95 , anchor = CENTER)       
btn_japan_time = Button(root , text = "Show time" , command = obj_japan.times) 
btn_japan_time.place(relx = 0.7 , rely = 0.95 , anchor = CENTER)    
        
root.mainloop()

