from tkinter import*
import tkinter as tk
from tkinter import ttk, messagebox
from timezonefinder import TimezoneFinder
from opencage.geocoder import OpenCageGeocode
from datetime import *
import tkinter
import requests,json
import pytz

from PIL import Image,ImageTk
from tkinter import PhotoImage

#image
def get_image(description, resize=None):
    
    image_dict = {
        'clear': 'Images/clear.png',
        'few': 'Images/few.png',
        'light': 'Images/rain.png',
        'broken': 'Images/broken.png',
        'overcast': 'Images/overcast.png',
        'scattered': 'Images/scattered.png'
        
        
    }

    
    image_path = image_dict.get(description.split()[0].lower(), image_dict['clear'])  
    
    
    image = Image.open(image_path)
    if resize:
        image = image.resize(resize, Image.LANCZOS)
    
    
    return ImageTk.PhotoImage(image)

def show_image(description, parent, x, y, resize=None):
    image = get_image(description, resize)
    label = tk.Label(parent, image=image, bg="#3C44A4")
    label.image = image  
    label.place(x=x, y=y)
    return label

root=tkinter.Tk()
root.title("Weather Forecast")
root.geometry("540x800")
root.resizable(width=False,height=False)
image_path= PhotoImage(file="Images/sky.png")
bg_image= tkinter.Label(root,image=image_path)
bg_image.place(relheight=1,relwidth=1)


font1 = ('poppins', 40, 'bold')
font2=('poppins', 11, 'bold')
font3=('poppins',20,'bold')
font4 = ('poppins', 27, 'bold')



def get_weather():
    city= searchfield.get()
    key = ''
    geocoder = OpenCageGeocode(key)
    query = city
    results = geocoder.geocode(query)

    if results:
        location = results[0]
        latitude = location['geometry']['lat']
        longitude = location['geometry']['lng']

        obj = TimezoneFinder()
        result = obj.timezone_at(lng=longitude, lat=latitude)

        time_zone.config(text=result)
        long_lat.config(text=f"{round(latitude, 4)}°N {round(longitude, 4)}°E")

        home = pytz.timezone(result)
        local_time = datetime.now(home)
        current_time = local_time.strftime("%I:%M %p")
        clock.config(text=current_time)


    
    #weather
    apikey="3eb9436e80e85d6cb059e60a7bbda030"
    baseurl= f"https://api.openweathermap.org/data/2.5/forecast?q="
    completeurl= baseurl+city+"&appid="+apikey
    res = requests.get(completeurl)
    data= res.json()
    data_dict = json.loads(json.dumps(data))
    # print(data)


    current_temp= data_dict["list"][0]["main"]["temp"]- 273.15
    # print(current_temp)
    formatted_temp = "{:.1f}°C".format(current_temp)
    # print(formatted_temp)
    humidity=data_dict["list"][0]["main"]["humidity"]
    # print(humidity)
    wind=data_dict["list"][0]["wind"]["speed"]
    # print(wind)
    weather_main = data_dict["list"][0]["weather"][0]["main"]
    description=data_dict["list"][0]["weather"][0]["description"]
    # print(description)
    lable1_1.config(text=formatted_temp)
    lable1_2.config(text=(humidity, "%"))
    lable1_3.config(text=(wind, "m/s"))
    lable1_4.config(text=description)






    #days
    one=datetime.now()
    day1.config(text=one.strftime("%A"))

    two=one+timedelta(days=1)
    day2.config(text=two.strftime("%A"))

    three=one+timedelta(days=2)
    day3.config(text=three.strftime("%A"))

    four=one+timedelta(days=3)
    day4.config(text=four.strftime("%A"))

    five=one+timedelta(days=4)
    day5.config(text=five.strftime("%A"))

    
    six=one+timedelta(days=5)
    day6.config(text=six.strftime("%A"))

    
    seven=one+timedelta(days=6)
    day7.config(text=seven.strftime("%A"))
    

    #1cell
    firtemp.config(text=formatted_temp)
    firstdes.config(text=description)
    firhum.config(text=(humidity,"%"))
    label1 = show_image(description, first, 15, 125, resize=(75, 75))


    #2cell
    d1=data_dict["list"][1]["main"]["temp"]- 273.15
    box1temp="{:.1f}°C".format(d1)
    des1=data_dict["list"][1]["weather"][0]["description"]


    sectemp.config(text=box1temp)
    secdes.config(text=des1)
   
    label2 = show_image(des1, second, 20, 80, resize=(50, 50))


    #3cell
    d2=data_dict["list"][2]["main"]["temp"]- 273.15
    box2temp="{:.1f}°C".format(d1)
    des2=data_dict["list"][2]["weather"][0]["description"]


    thitemp.config(text=box2temp)
    thides.config(text=des2)

    label3 = show_image(des2, third, 20,80, resize=(50, 50))

    #4cell
    d3=data_dict["list"][3]["main"]["temp"]- 273.15
    box3temp="{:.1f}°C".format(d1)
    des3=data_dict["list"][3]["weather"][0]["description"]


    foutemp.config(text=box2temp)
    foudes.config(text=des3)

    label4 = show_image(des3, fourth, 20, 80, resize=(50, 50))

    #5cell
    d4=data_dict["list"][4]["main"]["temp"]- 273.15
    box4temp="{:.1f}°C".format(d1)
    des4=data_dict["list"][4]["weather"][0]["description"]


    fiftemp.config(text=box4temp)
    fifdes.config(text=des4)

    label5 = show_image(des4, fifth, 20, 80, resize=(50, 50))

    #6cell
    d5=data_dict["list"][5]["main"]["temp"]- 273.15
    box5temp="{:.1f}°C".format(d1)
    des5=data_dict["list"][5]["weather"][0]["description"]


    sixtemp.config(text=box5temp)
    sixdes.config(text=des5)
    label6 = show_image(des5, sixth, 20, 80, resize=(50, 50))

    #7cell
    d6=data_dict["list"][6]["main"]["temp"]- 273.15
    box6temp="{:.1f}°C".format(d1)
    des6=data_dict["list"][6]["weather"][0]["description"]


    sevtemp.config(text=box6temp)
    sevdes.config(text=des6)
    label7 = show_image(des6, seventh, 20, 80, resize=(50, 50))
   







    



#label
label1=Label(root,text="TEMPERATURE:", font=font2,fg="#3C44A4", bg="#F5F5DC")
label1.place(x=40,y=193)
lable1_1=Label(root,text="", font=font2,fg="#000", bg="#F5F5DC")
lable1_1.place(x=170,y=193)

label2=Label(root,text="HUMIDITY:", font=font2,fg="#3C44A4", bg="#F5F5DC")
label2.place(x=40,y=228)
lable1_2=Label(root,text="", font=font2,fg="#000", bg="#F5F5DC")
lable1_2.place(x=170,y=228)

label3=Label(root,text="WINDSPEED:", font=font2,fg="#3C44A4", bg="#F5F5DC")
label3.place(x=40,y=263)
lable1_3=Label(root,text="", font=font2,fg="#000", bg="#F5F5DC")
lable1_3.place(x=170,y=263)

label4=Label(root,text="DESCRIPTION:", font=font2,fg="#3C44A4", bg="#F5F5DC")
label4.place(x=72,y=298)
lable1_4=Label(root,text="",justify='center',font=font2,fg="#000", bg="#F5F5DC",width=17)
lable1_4.place(x=50,y=315)


#search
searchfield= tk.Entry(root,justify='center',font=font3, width=13 ,bg='#FFEDA2', border=0, fg='#ED9455')
searchfield.place(x=168,y=125)
searchfield.focus()

search_icon=PhotoImage(file="Images/search.png")
myimage_icon=Button(image=search_icon,borderwidth=0,cursor="hand2", bg='#FFEDA2', command=get_weather)
myimage_icon.place(x=380,y=123)

#clock
clock=Label(root,text='',font=font1, fg='#3C44A4', bg='#A5DAFF')
clock.place(x=260,y=248)

#timezone
time_zone=Label(root,font=font4, fg='#3C44A4',bg='#A5DAFF')
time_zone.place(x=240,y=170)

long_lat=Label(root,font=font2, fg='#3C44A4',bg='#A5DAFF')
long_lat.place(x=270,y=220)


#first cell
first= Frame(root, width=105.5, height=275, bg="#3C44A4",)
first.place(x=31,y=407)

day1=Label(first,justify="center",text="",font=("poppins",17),fg="#fff", bg="#3C44A4")
day1.place(x=5,y=10)

firlab=Label(first,text="TEMPERATURE:", font=("poppins",10,"bold"),fg="#fff", bg="#3C44A4")
firlab.place(x=3,y=40)
firtemp=Label(first,justify="center",text="", font=font2,fg="#fff", bg="#3C44A4")
firtemp.place(x=23,y=60)

firlab2=Label(first,text="HUMIDITY:", font=("poppins",10,"bold"),fg="#fff", bg="#3C44A4")
firlab2.place(x=3,y=90)
firhum=Label(first,justify="center",text="", font=font2,fg="#fff", bg="#3C44A4")
firhum.place(x=72,y=89)

firlab3=Label(first,text="DESCRIPTION:", font=("poppins",10,"bold"),fg="#fff", bg="#3C44A4")
firlab3.place(x=3,y=208)
firstdes=Label(first,justify="center",text="",font=("poppins",9,"bold"), fg='#fff',bg='#3C44A4', width=14)
firstdes.place(x=1,y=230)

#second cell
second= Frame(root, width=90, height=178, bg="#38B6FF")
second.place(x=173,y=358)


day2=Label(second,justify="center",text="",font=("poppins",11, "bold"),fg="#fff", bg="#38B6FF")
day2.place(x=2,y=5)

seclab=Label(second,text="TEMPERATURE:", font=("poppins",9,"bold"),fg="#000", bg="#38B6FF")
seclab.place(x=0,y=35)
sectemp=Label(second,justify="center",text="", font=("poppins",10,"bold"),fg="#000", bg="#38B6FF")
sectemp.place(x=23,y=55)



seclab2=Label(second,text="DESCRIPTION:", font=("poppins",9,"bold"),fg="#000", bg="#38B6FF")
seclab2.place(x=5,y=135)
secdes=Label(second,justify="center",text="",font=("poppins",8,"bold"), fg='#000',bg='#38B6FF', width=13)
secdes.place(x=3,y=155)

#third cell
third= Frame(root, width=90, height=178, bg="#38B6FF")
third.place(x=296,y=358)

day3=Label(third,justify="center",text="",font=("poppins",11, "bold"),fg="#fff", bg="#38B6FF")
day3.place(x=2,y=5)

thilab=Label(third,text="TEMPERATURE:", font=("poppins",9,"bold"),fg="#000", bg="#38B6FF")
thilab.place(x=0,y=35)
thitemp=Label(third,justify="center",text="", font=("poppins",10,"bold"),fg="#000", bg="#38B6FF")
thitemp.place(x=23,y=55)



thilab2=Label(third,text="DESCRIPTION:", font=("poppins",9,"bold"),fg="#000", bg="#38B6FF")
thilab2.place(x=5,y=135)
thides=Label(third,justify="center",text="",font=("poppins",8,"bold"), fg='#000',bg='#38B6FF', width=13)
thides.place(x=1,y=155)

#fourth cell
fourth= Frame(root, width=90, height=178, bg="#38B6FF")
fourth.place(x=417,y=358)

day4=Label(fourth,justify="center",text="",font=("poppins",11, "bold"),fg="#fff", bg="#38B6FF")
day4.place(x=2,y=5)

foulab=Label(fourth,text="TEMPERATURE:", font=("poppins",9,"bold"),fg="#000", bg="#38B6FF")
foulab.place(x=0,y=35)
foutemp=Label(fourth,justify="center",text="", font=("poppins",10,"bold"),fg="#000", bg="#38B6FF")
foutemp.place(x=23,y=55)



foulab2=Label(fourth,text="DESCRIPTION:", font=("poppins",9,"bold"),fg="#000", bg="#38B6FF")
foulab2.place(x=5,y=135)
foudes=Label(fourth,justify="center",text="",font=("poppins",8,"bold"), fg='#000',bg='#38B6FF', width=13)
foudes.place(x=1,y=155)


#fifth cell
fifth= Frame(root, width=90, height=178, bg="#38B6FF")
fifth.place(x=173,y=565)

day5=Label(fifth,justify="center",text="",font=("poppins",11, "bold"),fg="#fff", bg="#38B6FF")
day5.place(x=2,y=5)

fiflab=Label(fifth,text="TEMPERATURE:", font=("poppins",9,"bold"),fg="#000", bg="#38B6FF")
fiflab.place(x=0,y=35)
fiftemp=Label(fifth,justify="center",text="", font=("poppins",10,"bold"),fg="#000", bg="#38B6FF")
fiftemp.place(x=23,y=55)



fiflab2=Label(fifth,text="DESCRIPTION:", font=("poppins",9,"bold"),fg="#000", bg="#38B6FF")
fiflab2.place(x=5,y=135)
fifdes=Label(fifth,justify="center",text="",font=("poppins",8,"bold"), fg='#000',bg='#38B6FF', width=13)
fifdes.place(x=1,y=155)

#sixth cell
sixth= Frame(root, width=90, height=178, bg="#38B6FF")
sixth.place(x=296,y=565)

day6=Label(sixth,justify="center",text="",font=("poppins",11, "bold"),fg="#fff", bg="#38B6FF")
day6.place(x=2,y=5)

sixlab=Label(sixth,text="TEMPERATURE:", font=("poppins",9,"bold"),fg="#000", bg="#38B6FF")
sixlab.place(x=0,y=35)
sixtemp=Label(sixth,justify="center",text="", font=("poppins",10,"bold"),fg="#000", bg="#38B6FF")
sixtemp.place(x=23,y=55)



sixlab2=Label(sixth,text="DESCRIPTION:", font=("poppins",9,"bold"),fg="#000", bg="#38B6FF")
sixlab2.place(x=5,y=135)
sixdes=Label(sixth,justify="center",text="",font=("poppins",8,"bold"), fg='#000',bg='#38B6FF', width=13)
sixdes.place(x=1,y=155)

# seventh cell
seventh= Frame(root, width=90, height=178, bg="#38B6FF",)
seventh.place(x=417,y=565)


day7=Label(seventh,justify="center",text="",font=("poppins",11, "bold"),fg="#fff", bg="#38B6FF")
day7.place(x=2,y=5)

sevlab=Label(seventh,text="TEMPERATURE:", font=("poppins",9,"bold"),fg="#000", bg="#38B6FF")
sevlab.place(x=0,y=35)
sevtemp=Label(seventh,justify="center",text="", font=("poppins",10,"bold"),fg="#000", bg="#38B6FF")
sevtemp.place(x=23,y=55)



sevlab2=Label(seventh,text="DESCRIPTION:", font=("poppins",9,"bold"),fg="#000", bg="#38B6FF")
sevlab2.place(x=5,y=135)
sevdes=Label(seventh,justify="center",text="",font=("poppins",8,"bold"), fg='#000',bg='#38B6FF', width=13)
sevdes.place(x=1,y=155)





root.mainloop()

