from tkinter import *  # tkinter is a module that helps in reating GUI windows
import tkinter as tk
from geopy.geocoders import Nominatim  # geopy module has a submodule called geocoders that involves the process of converting address into its geographical subcordinates(latitude and longitude), Nominatim is class of geocoders submodule that helps in defining the web services to be used
from tkinter import ttk,messagebox   
from timezonefinder import TimezoneFinder # Timezonefinder module contains TimezoneFinder class which helps in finding the timezone of a particular place or address
from datetime import datetime # datetime class of datetime module gives the current time at a particular timezone and allows to set the format in which current time is displayed
import requests # requests modules allows us to establish a connection with the web service, facilitating exchange of information
import pytz # pytz module helps in retrieving the current time of another place with respect to the current time of the place in which the user is based

t = Tk() # creating an object of the Tk class of the tkinter module
t.title("Weather App") # using title method of the Tk class to set the title of the gui window
t.geometry("900x500+300+200") # using geometry method of Tk class to set the width,height and x cordinates and y cordinates 
t.resizable(False,False) # using resizable method of Tk class to restrict the user from resizing the window size, this way the the geometry of window cannot be changed by the user



def getWeather():
    try:
        
        city = textfield.get() # the get method of Tk class is used to get the input from the user eith the help of the object textfield , the city variable stores the input provided by the user.

        geolocator = Nominatim(user_agent = "geoapiExercises") # geolocator is an object of the class Nominatum of the submodule geocoders, geoapiExercises is the web service that the user wants to use as data source.
        location = geolocator.geocode(city) # geocode is a method of the Nominatim class which is used to return the longitude and latitude of the city provided.
        obj = TimezoneFinder() # TimezoneFinder class is used to return the timezone of that particular longitutde and latitude
        result = obj.timezone_at(lng=location.longitude,lat=location.latitude) # timezone_at method of the TimezoneFinder class is used to return the timezone at that prticular longitutde and latitude

        home = pytz.timezone(result) # timezone class of the pytz module returns the current time at that particular timezone
        local_time = datetime.now(home) # now class of the datetime module returns the current time of the person who is using the gui and converts the home time with respect to the local time
        current_time=local_time.strftime("%I:%M %p") # the format for representing this time is set by using the srftime method of the datetime now class
        clock.config(text=current_time) # clock is a widget created using Label class of the tkinter module which is configered with text , in this case the current time
        name.config(text="CURRENT WEATHER") # name is a widget created using Label class of the tkinter module which is configered with text

        #weather
        api = "https://api.openweathermap.org/data/2.5/weather?lat=" + str(location.latitude) + "&lon=" + str(location.longitude) + "&appid=8ef680ce2e870a66872617106fd84fae" # this line constructs an api for retrieving data from this website by creating an url.


        json_data = requests.get(api).json()  # this line requests for data from the web service using the get function of requests using the api url module and stores ad parses it in json format 
        condition = json_data['weather'][0]['main'] # this line retireves the condition data from the web service using the api url that was created
        description = json_data['weather'][0]['description'] # this line retireves the description of weather from the web service using the api url that was created 
        temp = int(json_data['main']['temp']-273.15) # this line retrieves the temp data
        pressure = json_data['main']['pressure'] # retireving pressure data
        humidity = json_data['main']['humidity'] # retrieving humidity at that loaction which was specified in the api url above
        wind = json_data['wind']['speed'] # retiriveing wind data


        y.config(text=(temp,"°")) # text configuration to the widget
        c.config(text=(condition,"|","FEELS","LIKE",temp,"°")) # text congfiguration to the widget

        w.config(text=wind) # text congfiguration to the widget
        h.config(text=humidity) # text congfiguration to the widget
        d.config(text=description) # text congfiguration to the widget
        p.config(text=pressure) # text congfiguration to the widget

    except Exception as e:
        messagebox.showerror("Weather App","Invalid Entry!") 
    
    



#search box
search_image = PhotoImage(file="C:\\Users\\birad\\OneDrive\\Documents\\weather_app\\search_box.png") # creating an object of the PhotoImage class of the tkinter module to load the image to be used in the gui window 
myimage = Label(image = search_image) # this object is used as input to the image parameter of the Label class, as Label class cannot load images.This creates a widget of image and myimage is assigned the object of Label class
myimage.place(x=20,y=20) # using the object, place method of Label class is used to adjust the position of image widget created by the Label class

textfield = tk.Entry(t,justify="center", width=17,font=("Comic Sans MS",25,"bold"),bg="#404040",border=0,fg="white") # creating an object of the Entry class of the tkinter module.This is used to create a text field which takes input from the user, thus creating a text widget
textfield.place(x=50,y=40) # text widget is placed by default in the previously created widget , in this case, the image widget and with x and y parameters it is positioned accordingly over the image widget
textfield.focus() # this method of Entry class is used to prompt the user to enter something into the text field as soon as the gui window is opened without the need for the user having to click on the text field to enter text


search_icon = PhotoImage(file = "C:\\Users\\birad\\OneDrive\\Documents\\weather_app\\search_icon.png" ) # loading another image 
mysearch_icon = Button(image=search_icon,borderwidth=0,cursor="hand2",bg="#404040",command=getWeather) # creating an object of the Button class which creates an image widget acting like a button, expecting the user to click on it.When the user clicks on the button the command parameter is used to run the getWeather function.
mysearch_icon.place(x=400,y=34) # this button widget is positioned using place method of Button class of the tkinter module


#logo
logo_image = PhotoImage(file="C:\\Users\\birad\\OneDrive\\Documents\\weather_app\\logo.png") # loading another image
mylogo = Label(image=logo_image)
mylogo.place(x=150,y=100) 


#Bottom box
box_image = PhotoImage(file = "C:\\Users\\birad\\OneDrive\\Documents\\weather_app\\box.png") # loading another image
mybox = Label(image=box_image)
mybox.pack(padx=5, pady=5, side=BOTTOM) # using the pack method of Label class to pack the image widget and automatically adjusting the widget at the bottom of the window taking the space available to place the widget in the window,padx and pady allow users to customize the position if they are not satisfied by the position decided by the pack method

#time
name=Label(t,font=("arial",15,"bold")) # creating a widget which will be configered with text 
name.place(x=30,y=100)
clock=Label(t,font=("Helvetica",20)) # creating another widget which will be configured with text
clock.place(x=30,y=130)



#label
label1 = Label(t,text="WIND",font=("Helvetica",15,'bold'),fg="white",bg="#1ab5ef")  # creating a text widget and placing it in the recently created widget, in this case the box widget 
label1.place(x=120,y=400)

label2 = Label(t,text="HUMIDITY",font=("Helvetica",15,'bold'),fg="white",bg="#1ab5ef") # creating a text widget and placing it in the recently created widget, in this case the box widget
label2.place(x=250,y=400)

label3 = Label(t,text="DESCRIPTION",font=("Helvetica",15,'bold'),fg="white",bg="#1ab5ef") # creating a text widget and placing it in the recently created widget, in this case the box widget
label3.place(x=430,y=400)

label4 = Label(t,text="PRESSURE",font=("Helvetica",15,'bold'),fg="white",bg="#1ab5ef") # creating a text widget and placing it in the recently created widget, in this case the box widget
label4.place(x=650,y=400)

y=Label(font=("arial",70,'bold'),fg="#ee666d") # creating a widget which will be configered with text
y.place(x=400,y=150)
c=Label(font=("arial",15,'bold')) # creating a widget which will be configered with text
c.place(x=400,y=250)

w=Label(text="...",font=("arial",20,"bold"),bg="#1ab5ef") # creating another text widget which will be configered with some text 
w.place(x=120,y=430)
h=Label(text="...",font=("arial",20,'bold'),bg="#1ab5ef") # creating another text widget which will be configered with some text 
h.place(x=280,y=430)
d=Label(text="...",font=("arial",20,"bold"),bg="#1ab5ef") # creating another text widget which will be configered with some text 
d.place(x=450,y=430)
p=Label(text="...",font=("arial",20,"bold"),bg="#1ab5ef") # creating another text widget which will be configered with some text 
p.place(x=670,y=430)



t.mainloop() # using the mainloop method of tkinter class to run all the above lines upon opening the gui window, it maps the functionalities to the respect functions handling events upon user input 
