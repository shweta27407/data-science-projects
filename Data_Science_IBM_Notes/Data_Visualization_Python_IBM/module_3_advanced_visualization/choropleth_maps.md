## Welcome to Choropleth Maps. 

These are what we call choropleth maps.

 So what is a choropleth map? A choropleth map is a thematic map in which areas are shaded or patterned in proportion to the measurement of the statistical variable displayed on the map. Such as population density or per capita income.

The higher the measurement, the darker the color. 

So the map to the left is a choropleth world map showing the infant mortality rate per 1000 births. 

The darker the color, the higher the infant mortality rate. According to the map, African countries have very high infant mortality rates, with some reporting a rate higher than 160 per 1000 births. 

Similarly, the map on the right is a choropleth map of the US showing population per square mile by state. 

   ![word cloud](https://github.com/shweta27407/data-science-projects/blob/main/Data_Science_IBM_Notes/Data_Visualization_Python_IBM/module_2_specialized_visualization_tools/images/choropleth.png)


Again, the darker the color, the higher the population. According to the map, states in the eastern part of the US tend to be more populous than states in the western part, with California being an exception.



Folium is a Python library used for creating interactive maps and visualizations. It provides a simple and intuitive way to generate maps using data from various sources, including GeoJSON, Pandas DataFrames, and NumPy arrays. 

To create a choropleth map of a region of interest, folium requires a GeoJSON file that includes geospatial data of the region. 

For a choropleth map of the world, we would need a GeoJSON file that lists each country and any geospatial data to define its borders and boundaries.

Here's an example of what a GeoJSON file would include about each country.

   ![word cloud](https://github.com/shweta27407/data-science-projects/blob/main/Data_Science_IBM_Notes/Data_Visualization_Python_IBM/module_2_specialized_visualization_tools/images/geoJson.png)


The example here pertains to the country Brunei. As you can see, the file consists of its name, ID, geometry, shape, and coordinates that define its borders and boundaries.


So let's see how we can create a choropleth map of the world showing immigration to Canada.

But this time, let's use the Mapbox Bright Tileset. 

   ![word cloud](https://github.com/shweta27407/data-science-projects/blob/main/Data_Science_IBM_Notes/Data_Visualization_Python_IBM/module_2_specialized_visualization_tools/images/createmap.png)


The result is a nice world map displaying the name of every country. 
Now, let's convert this map into a choropleth map. 

We first define a variable that points to our JSON file. Then we apply the choropleth function to our world map. We tell it to use the country total columns in our df_canada data frame and the country names to look up the geospatial information about each country in the GeoJSON file. The result will be a choropleth map of Canada showing the intensity of immigration from different countries worldwide.



The Mapbox Bright Tileset displays the name of every country when used on a map.