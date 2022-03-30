"""

Using what you learned from the previous weeks, 
you will graphing solo or in small groups, your choice!


For your reference I added a completed file in pulling_graphing_cleaning.py


Tasks:
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



Goals:

- Getting comfortable writing code solo by completting Tasks(shown above)
- Pulling Data from a csv 
- Learning to graph via code
- Reading API documentation
- Transforming and cleaning data


"""

import pandas as pd
import plotly.express as px
import plotly.graph_objects as go


#Always good to look at survey to be familiar w the data before doing anything
survey = "PullingData_Cleaning_Graphing/SurveyData.csv"


def fav_rest():
    bloom_loc = pd.read_csv(survey)

    fig = px.scatter_mapbox(bloom_loc, lat="RLatitude", lon="RLongitude", 
    hover_name= "Fav_Restaurant", hover_data= ["RestaurantType","Name"] ,color_discrete_sequence= ["blue"],height = 800)

    bloomington_lat_center = 39.16822839598016

#please note that map style is "carto-darkmatter" not "dark" 
#   because cartodarkmatter works for plotly.js(which is what we are using)
#   while dark works only for builtinmapbox styles. Thier documentation is confusing, but this is why using dark caused for some people to get white screens.
    
    fig.update_layout(mapbox_style= "carto-darkmatter", mapbox_zoom=10, mapbox_center_lat = bloomington_lat_center,
        margin={"t":0,"b":0,"l":0,"r":0,})

    fig.show()



def clean_hometown():
    file =  pd.read_csv(survey)

    blat = 39.17268960349786
    blon = -86.52326466929847

    thelist = []
    numOfRows = len(file)
    columns = ["name", "lat", "lon","oneliner"]
    thelist.append(columns)
    for i in range(numOfRows):

        thelist.append([ file.iloc[i]["Name"], file.iloc[i]["CLatitude"],file.iloc[i]["CLongitude"], file.iloc[i]["One_Liner"] ])
        thelist.append([ file.iloc[i]["Name"], blat,blon,file.iloc[i]["One_Liner"]   ])

    folder_path = "PullingData_Cleaning_Graphing"
    ldf = pd.DataFrame(thelist)

    ldf.to_csv( f"{folder_path}/cleanedHometownSurveyData.csv",index = False, header = False )


  
def hometown_line():

    file = pd.read_csv("PullingData_Cleaning_Graphing/cleanedHometownSurveyData.csv")

    hometown = file.query(f"name in { [x for x in file.name ]}")


    fig = px.line_mapbox(hometown,lat = "lat", lon = "lon", color = "name", 
                        zoom = 3, height = 900, hover_data=["oneliner"])

    fig.update_layout(mapbox_style="open-street-map", mapbox_zoom=  1, mapbox_center_lat = 41,
            margin={"r":0,"t":0,"l":0,"b":0})

    fig.show()



clean_hometown()
hometown_line()
fav_rest()
