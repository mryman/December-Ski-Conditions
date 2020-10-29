# How is the skiing in December?

## Description
The month of December in Washington State can often be a fickle time with respect to accumulating enough snow for commercial ski operations to get into full swing, and be able to capitalize on the peak holiday season to generate revenue.  Seasoned veterans of the Pacific Northwest skiing community may even be heard grumbling that *"it's hardly worth buying lift tickets in advance during the month of December because the conditions are so variable that sometimes it feels like it rains as much as it snows"*, or *"some years it doesn't snow enough to open a reasonable amount of terrain before the big storms arrive in January or later"*.  This project explores archived weather data recorded from a weather instrument station at one of the most popular ski areas in close proximity to Seattle and Western Washington, Alpental at Snoqualmie Pass. Analyzing this data allows us to get a better picture of how the winter weather shaped ski conditions for that specific venue over a five year period.

## Data Source
The data for this project was downloaded from the archives provided to the public by The Northwest Avalanche Center on their data portal found here:   
<https://www.nwac.us/data-portal/>    

The datasets drawn from this particular location (Alpental Base 3100') include data for:  
 
 - Battery Voltage  
 - Temperature  
 - Relative Humidity  
 - Precipitation  
 - Total Snow Depth  
 - 24hr Snow accumulation  
 Each point is recorded every hour on the hour.


 It is important to note that precipitation data is standardized to water equivalent.  That is to say, regardless of whether it falls to the ground as rain or snow, the gauges are heated and record quantities using water equivalent.  Similarly, the data recorded for 24 Hour Snow are expressed using a term called SWE (Snow Water Equivalent).  This is how much water content is in a cubic inch of space.  

In general, we can think of 0.1 inches of SWE producing roughly 1 inch to 1.5 inches of actual snow on the ground.  Similarly, a storm cycle that delivers 1.0 inch of SWE may result in a foot of fresh snowfall on the ground.  These are only general rules of thumb for estimating.  The type of snow particles, moisture content, and density will all play a role in what total accululation amounts to.

The Total Snow Depth field in our data refers to actual inches of snow on the surface of the ground.

## Usage
As the data fields from each location may differ slightly or include more fields, and instrumentation failures or gitches often present outlier data points, using CSV files from locations other than Alpental Base may require reformatting and additional cleaning.  Providing the columns do not change in the future, subsequent year CSV files from this location should produce consistent results in the code and visualizations as they become available.




### Example of weather instrument stations:
![Weather Station](img/weather_instruments.jpg)


## Exploratory Data Analysis

After importing and cleaning my data using pandas, my first goal was to investigate where daily average temperatures lie with relation to the transition point value of 32 degrees Fahrenheit, below which precipitation falls as some form of snow rather than rain. The graphs below show that daily temperature means often straddle that critical transition line much of the time for the month of December each year.

![Mean Temps](img/meantemps.jpg)

While this provides insights as to how often the temperatue was conducive to producing snow, it does not address the factor of whether or not meausurable precipitation was happening when the temperature was favorable for snowfall.  This could be further assessed by determining which hourly periods had measurable precipitation for temperatures above and below the transition point, as well as the actual quantities of precipitation measured during those periods. 

![Mean Temps](img/precip_totals.jpg)

To explore the potential accuracy/inaccuracy of the claim *"It rains as much as it snows at Alpental in December"*, I used Bayesian analysis to apply the five years of data we have to see what the probability is of that hypothesis holding true as time goes on.






While we now have a better idea of rainy periods versus snowy periods, our second inquiry pertains more to the question of *"is there enough snow 'coverage' to provide a reasonable base and allow the ski area to open to the public for the busy holiday season?"*

The graphs below illustrate some important points in this query.  Based on feedback from a former professional ski patrol staff member, it is reasonable to consider a minumum depth of 36" of snow being one factor that influences the decision of when to open.  The critical date for the busy holiday season may be defined by the start date of school breaks, which varies annually but is typically the Friday which falls before Christmas.  As we can see, snow depth in some of our years of interest was robust enough in the first half of the month to allow early opening.  In 2018 the actual opening date coincided with the target deadline.  In 2019, conditions were so weak that the area was not able to open until January 5, completely missing the holiday break period.


![Snow Depth](img/snowdepths.jpg)