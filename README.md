# sqlalchemy-challenge
## Description
Climate Analysis of Hawaii Honalulu
We will analyse and Explore the Climate Data and also Design a Climate App 

### Part1 - Analyse and Explore Climate Data

#### Precipitation Analysis

Exploratory Precipitation Analysis :

Precipitation Analysis for the last 12 months

![image](https://github.com/supvadakkeveetil/sqlalchemy-challenge/assets/144635564/bd68bec1-d888-4746-9e27-cd81d95cde02)

Summary Statistics:
	
precipitation

-------------------------
 
count	2021.000000
 
mean	0.177279

std	0.461190

min	0.000000

25%	0.000000

50%	0.020000

75%	0.130000

max	6.700000

#### Station Analysis

- List the stations in the descending order

[('USC00519281', 2772),

 ('USC00519397', 2724),
 
 ('USC00513117', 2709),
 
 ('USC00519523', 2669),
 
 ('USC00516128', 2612),
 
 ('USC00514830', 2202),
 
 ('USC00511918', 1979),
 
 ('USC00517948', 1372),
 
 ('USC00518838', 511)]
 
 - Station "USC00519281" has the greatest number of observations (2772)


#### TOBS Data

Histogram with the previous 12 months of Temperature Observations

![image](https://github.com/supvadakkeveetil/sqlalchemy-challenge/assets/144635564/38a3e9a9-0c42-4650-97cb-e72cf3c67080)

### Part2 - Design Climate App
Design a Flask API
[
](https://github.com/supvadakkeveetil/sqlalchemy-challenge/blob/main/SurfsUp/app.py)https://github.com/supvadakkeveetil/sqlalchemy-challenge/blob/main/SurfsUp/app.py

## References
Data Source: Menne, M.J., I. Durre, R.S. Vose, B.E. Gleason, and T.G. Houston, 2012: An overview of the Global Historical Climatology Network-Daily Database. Journal of Atmospheric and Oceanic Technology, 29, 897-910, https://journals.ametsoc.org/view/journals/atot/29/7/jtech-d-11-00103_1.xml

As provided by Edx
