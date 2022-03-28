"""
Welcome to Week 1

This week we will practice:
    - Reading and writing data from files we have stored locally and from the internet
    - Cleaning data to match our criteia
    - Graphing everything on a map

I will go through examples for each as a code along, then I will give you a dataset to practice by yourself.


Steps:

1. Complete this survey: https://forms.gle/kSVgnrEqubVARVPt7


2. Download 
    - pandas
    - plotly

        How to Download:
            -For windows go to command prompt and type in "pip install [library name]"  and don't include the brackets or quotations
            -For mac go to terminal and type in "pip3 install [library name]"  and don't include the brackets or quotations


        More info about the libraries:
            pandas: https://pandas.pydata.org/docs/user_guide/index.html#user-guide
            plotly: https://plotly.com/python/
            

3. Follow the code along
    - Stop me anytime for explanations
    - Ask questions!!!!!!


4. Work on the survey data solo or in groups

    a) Graph a point map of everyone's favorite restaurant
        -Title of restaurant as title 
        -Include the food type when you hover (look at plotly docs to find how to do this)
        -Include recommender's name when you hover
        -Make it a dark map

    b) Graph everyone's hometown location as a line map connected to bloomington
        -Clean the data to put it in your desired format
            -Feel free to use your own way or the method I used 
        -Add the person's name as the title
        -Include peron's funny oneliner when you hover
        -Make it an outdoors map

"""


import pandas as pd
import plotly.express as px
import plotly.graph_objects as go




link = "https://raw.githubusercontent.com/plotly/datasets/master/us-cities-top-1k.csv"



def points():
    """ 
    Graphing the points in bloomington location csv
    """

    bloom_loc = pd.read_csv("Week1-PullingData/Bloomington_Location.csv")

    fig  = px.scatter_mapbox(bloom_loc, lat = "lat", lon = "lon",

    hover_name = "name",color_discrete_sequence= ["blue"], height = 800)

    bloomington_lat_center = 39.16822839598016


    fig.update_layout(mapbox_style = "stamen-terrain", mapbox_zoom = 10, mapbox_center_lat = bloomington_lat_center,
     margin={"t":0,"b":0,"l":0,"r":0,} )

    fig.show()




def line():

    file = pd.read_csv(link)
    us_cities = file.query("State in ['Colorado', 'New York', 'Indiana']")


    fig = px.line_mapbox( us_cities, lat = "lat", lon = "lon", color = "State", 
                            zoom =1, height=800)

    fig.update_layout(mapbox_style = "stamen-terrain", mapbox_zoom = 3,
     mapbox_center_lat = 41)

    fig.show()



def cleaned_vacation():
    file =  pd.read_csv("Week1-PullingData/Vacation.csv")


    thelist = []
    numOfRows = len(file)
    columns = ["name", "lat", "lon"]

    thelist.append(columns)
    for i in range(numOfRows):

        thelist.append([ file.iloc[i]["name"], file.iloc[i]["hlat"],file.iloc[i]["hlon"]   ])
        thelist.append([ file.iloc[i]["name"], file.iloc[i]["blat"],file.iloc[i]["blon"]   ])

    folder_path = "Week1-PullingData/"
    ldf = pd.DataFrame(thelist)

    # ldf.to_csv( "Week1-PullingData/cleanedVacation")
    ldf.to_csv( f"{folder_path}cleanedVacation.csv",index = False, header = False )

    
def vacation():

    file = pd.read_csv("Week1-PullingData/cleanedVacation.csv")

    hometown = file.query(f"name in { [x for x in file.name ]}")


    fig = px.line_mapbox(hometown,lat = "lat", lon = "lon", color = "name", 
                        zoom = 3, height = 900)

    fig.update_layout(mapbox_style="stamen-terrain", mapbox_zoom=  1, mapbox_center_lat = 41,
            margin={"r":0,"t":0,"l":0,"b":0})

    fig.show()



points() #single point on a graph

line() #line between 2 points

cleaned_vacation() #cleans up points from Vacation.csv
vacation() #Lines between 2 points from cleanedVacation.csv

