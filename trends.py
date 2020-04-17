import pandas
import numpy as np
import matplotlib.pyplot as plt

mobility_data = pandas.read_csv("applemobilitytrends-2020-04-13.csv")


def transpose_df(city_name, transportation):
    df = mobility_data[(mobility_data['region'] == city_name) &
                       (mobility_data['transportation_type'] == transportation)]
    df = df.drop(['geo_type'], axis=1)
    df_t = df.melt(['region', 'transportation_type'], var_name='Date', value_name='Value')
    df_t.Value = df_t.Value - df_t.Value.iloc[0]

    return df_t


london_walking = transpose_df('London', 'walking')
manc_walking = transpose_df('Manchester', 'walking')
birm_walking = transpose_df('Birmingham - UK', 'walking')
leeds_walking = transpose_df('Leeds', 'walking')

for frame in [london_walking, manc_walking, birm_walking, leeds_walking]:
    plt.plot(frame["Date"], frame["Value"], label=frame['region'][0])
    plt.xticks(np.arange(0, 92, step=15))
    plt.text(92, frame['Value'][91], str(frame['Value'][91]), fontsize=8)

plt.legend()
plt.axvline(70, color='red')
plt.show()
