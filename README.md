# Surfs_Up_Challenge

## Overview
The purpose of this analysis is to assist W. Avy to analyze temperature trends for June and December in Oahu, Hawaii to determine if his surf and ice cream business would be sustainable year-round.
## Resources

- Jupyter notebook 6.4.8
- SQL Alchemy 1.4.32

## Results

We added a histogram to show a visual representation of some of the data in our summary statistics.

### June Summary Statistics and Histogram(2010 - 2017)
![image](https://user-images.githubusercontent.com/110706169/196061922-4b404c4a-e2f8-4927-ab64-88fb55b3c4d2.png)
![image](https://user-images.githubusercontent.com/110706169/196062549-5b5d8515-6063-469f-ad78-63eb3d37e7ee.png)

### December Summary Statistics and Histogram(2010 - 2017)
![image](https://user-images.githubusercontent.com/110706169/196061929-94ceee20-e006-46e7-b2e5-26c95de59407.png)
![image](https://user-images.githubusercontent.com/110706169/196062585-22d2ae32-2cad-49e5-83d8-9f368fae2cca.png)

- June has 1700 recorded data points and December has 1517.
- The average temperature for June is about 75&deg;F, 4&deg;F higher than in December(71&deg;F).
- The median for June is 75&deg;F and 71&deg;F for December.

## Summary
**Looking at our statistics and histograms:** 
- for June we can observe that from 2010 to 2017 temperatures between 72&deg;F and 78&deg;F represent the majority of the data.
- for December we can observe that from 2010 to 2017 temperatues between 68&deg;F and 76&deg;F represent the majority of the data.

Knowing this and the average temperatures for the 7 year duration we consider that setting up the surf and ice cream business would be a lucrative endeavor. To provide further data we created an additional query and a regression plot for the months of June and December to demonstrate the relationship between temperature and precipitation.

![image](https://user-images.githubusercontent.com/110706169/196075730-1e9247c7-a719-4e7b-a77a-e15998e3d4c5.png)
![image](https://user-images.githubusercontent.com/110706169/196074921-b0e30032-bac1-4a76-91a4-95bab63b4b08.png)

From the graph above we can see that between 67&deg;F and 70&deg;F is when the highest chance of precipitation exists for the month of June.

![image](https://user-images.githubusercontent.com/110706169/196075794-99eb1842-abd3-47ee-b8d6-a86025defbe1.png)
![image](https://user-images.githubusercontent.com/110706169/196074964-8b4f0a9b-c6d2-4ec8-bcec-c56cc5909d18.png)

From the graph above we can see that between 65&deg;F and 71&deg;F is when the highest chance of precipitation exists for the month of December.

Although it is relatively colder in December than in June. A tropical island like Hawaii seems to maintain warm temperatures all year round and we believe that opening the business is the right choice.


