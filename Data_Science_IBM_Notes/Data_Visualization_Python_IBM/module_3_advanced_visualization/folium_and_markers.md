## Welcome to an introduction to Folium. 

Folium is a powerful data visualization library in Python that was built primarily to help people visualize geospatial data. With Folium, you can create a map of any location in the world using latitude and longitude values. 

You can also create a map and superimpose markers and clusters on top of the map for interesting visualizations, you can also create maps of different styles, such as street level maps, stamen maps, and a couple of others, which we will look into in just a moment. 

Creating a world map with Folium is straightforward. First, you need to import Folium and then you call the map function. That is all.

What's interesting about the maps created by Folium is that they are interactive, so you can zoom in and out after the map is rendered, which is a helpful feature. 

   ![word cloud](https://github.com/shweta27407/data-science-projects/blob/main/Data_Science_IBM_Notes/Data_Visualization_Python_IBM/module_2_specialized_visualization_tools/images/folium.png)

In this video, you learned that Folium is a data visualization library in Python that helps people visualize geospatial data.
With Folium, you can create maps of different styles, such as street level maps, stamen maps, and more. 
A feature of Folium is that you can create different map styles using the tiles parameter.


## Markers 

1. First, import Folium, then create the map object. Remember that the location parameter specifies the latitude and longitude coordinates of the center point of the map. The zoom_start sets the initial zoom level of the map.

2. Markers play a vital role in enhancing interactivity and adding context to maps. They represent specific locations or points of interest, providing additional information when clicked. 

Markers are like signposts that guide us through the map, highlighting important elements. Ontario is a Canadian province that contains about 40% of the Canadian population. It is considered Canada's most populous province.


Let's add a marker for Ontario province, one of the largest provinces in Canada to our map. 

Using the folium.Marker function, we specify the location parameter as 51.2538, -85.3232, representing the approximate coordinates for Ontario. 
Additionally, we set the pop-up parameter as Ontario to provide a label when the marker is clicked. 
The add_to (canada_map) method is called on the folium.Marker object to add the marker for Ontario to the canada_map. This ensures that the marker is included as part of the map’s layers and will be displayed when the canada_map is rendered or saved.

   ![word cloud](https://github.com/shweta27407/data-science-projects/blob/main/Data_Science_IBM_Notes/Data_Visualization_Python_IBM/module_2_specialized_visualization_tools/images/foliummarkers.png)


Markers can be created using feature group.