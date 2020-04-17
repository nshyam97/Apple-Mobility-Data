import pandas
import numpy as np
import matplotlib.pyplot as plt

mobility_data = pandas.read_csv("applemobilitytrends-2020-04-13.csv")

mobility_city_data = mobility_data[mobility_data['geo_type'] == 'city']
mobility_country_data = mobility_data[~mobility_data.index.isin(mobility_city_data.index)]

mobility_city_data = mobility_city_data.drop(['geo_type'], axis=1)
mobility_country_data = mobility_country_data.drop(['geo_type'], axis=1)

london_walking = mobility_city_data[(mobility_city_data['region'] == 'London') &
                                    (mobility_city_data['transportation_type'] == "walking")]

london_t = london_walking.melt(['region', 'transportation_type'], var_name='Date', value_name='Value')
london_t.Value = london_t.Value - london_t.Value.iloc[0]

manc_walking = mobility_city_data[(mobility_city_data['region'] == 'Manchester') &
                                    (mobility_city_data['transportation_type'] == "walking")]

manc_t = manc_walking.melt(['region', 'transportation_type'], var_name='Date', value_name='Value')
manc_t.Value = manc_t.Value - manc_t.Value.iloc[0]

for frame in [london_t, manc_t]:
    plt.plot(frame["Date"], frame["Value"])
    plt.xticks(np.arange(0,92,step=15))
plt.axvline(70, color='red')
plt.show()
