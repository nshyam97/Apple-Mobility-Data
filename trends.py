import pandas
import matplotlib.pyplot as plt

mobility_data = pandas.read_csv("applemobilitytrends-2020-04-13.csv")


# Function to transpose the data. Currently the date values are columns and so we need to make these rows
# to make plotting the data easier
def transpose_df(region_name, transportation):
    # First choose the region and transportation type to create the usable dataframe
    df = mobility_data[(mobility_data['region'] == region_name) &
                       (mobility_data['transportation_type'] == transportation)]
    # Drop the geo_type column as it isn't useful anymore
    df = df.drop(['geo_type'], axis=1)
    # Pivots the dataframe from a wide to a tall format. Move the Date and Values as separate rows and corresponding
    # columns.
    df_t = df.melt(['region', 'transportation_type'], var_name='Date', value_name='Value')
    # Convert date column to datetime column
    df_t.Date = pandas.to_datetime(df_t.Date, format='%Y-%m-%d')
    # Make date column the index column to allow for easier plotting
    df_t.set_index('Date', inplace=True)
    # Values are currently percentages with the first value being the baseline. To make it a change in
    # baseline mobility, minus all values by the first value.
    df_t.Value = df_t.Value - df_t.Value.iloc[0]
    # Round all the values to 2 decimal places
    df_t.Value = df_t.Value.round(2)
    # Return the finished dataframe, ready to plot
    return df_t


# Function to create line graphs
def create_graph(data):
    # Iterate through every dataframe passed through this function
    for frame in data:
        # Plot the date against the corresponding value
        plt.plot(frame.index, frame['Value'], label=frame['region'][0])

    plt.legend()
    plt.xlabel('Date')
    plt.xticks(rotation=45)
    plt.ylabel('Percentage change in mobility (%)')
    plt.title('Mobility Trend Data for ' + data[0]['transportation_type'][0])
    # Plot vertical line for when the UK went into lockdown
    plt.axvline(pandas.Timestamp('2020-03-23'), color='red')
    plt.show()


london_walking = transpose_df('London', 'walking')
# manc_walking = transpose_df('Manchester', 'walking')
# birm_walking = transpose_df('Birmingham - UK', 'walking')
# leeds_walking = transpose_df('Leeds', 'walking')

# create_graph([london_walking, manc_walking, birm_walking, leeds_walking])

# UK_transit = transpose_df('UK', 'transit')
# US_transit = transpose_df('United States', 'transit')
#
# create_graph([UK_transit, US_transit])

print(london_walking[(london_walking.index >= pandas.Timestamp('2020-03-13')) &
                     (london_walking.index <= pandas.Timestamp('2020-03-15'))])
