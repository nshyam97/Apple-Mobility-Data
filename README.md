# Apple-Mobility-Data

This repository includes my Apple Mobility Trends analysis in the trend_analysis.ipynb file. The trends.py file served as an initial starting point for this notebook.

The update.sh file is a shell file I have written to be used for a cron job on my computer that will automatically update the notebook every 24 hours. The data contains 2 data sources, one from the Johns Hopkins Github found [here](https://github.com/CSSEGISandData/COVID-19) and the other is from the Apple Mobility Trends Dataset found [here](https://www.apple.com/covid19/mobility). The Apple Mobility dataset that the notebook uses is found in another repository of mine, found [here](https://github.com/nshyam97/Apple-Mobility-Trends-Data). Due to Apple requiring the user to download a new csv file everyday to get the daily stats, I have created a python script found [here](https://github.com/nshyam97/Scraping-with-Selenium) which will pull this data every 24 hours and update my Apple Mobility dataset repository referenced above.

More information about the accompanying repos can be found in their respective repos.

This repo serves as a personal project pulling in multiple data sources and visualisation as well as some general EDA to observe and understand trends in the data.
