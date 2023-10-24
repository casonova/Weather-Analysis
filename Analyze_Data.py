import pandas as pd
from sklearn.impute import KNNImputer
from sklearn.impute import SimpleImputer
from load_data import import_csv_file
import matplotlib.pyplot as plt
import seaborn as sns

data1= import_csv_file("weather.csv")



def Temperatur_Operation(data, start_date, end_date):
    # Convert 'Date' column to datetime
    data.iloc[:,0]=pd.to_datetime(data.iloc[:,0])

    # Convert start_date and end_date to datetime
    start_date=pd.to_datetime(start_date)
    end_date=pd.to_datetime(end_date)

    # Filter data between start_date and end_date
    filtered_df = data[(data.iloc[:,0] >= start_date) & (data.iloc[:,0] <= end_date)]

    # Get max, avg, min temperature
    max_temp = filtered_df['Temp'].max()
    avg_temp = filtered_df['Temp'].mean()
    min_temp = filtered_df['Temp'].min()

    # Return a dictionary with max, avg, min temperature
    return {
        "Maximum Temperature": max_temp,
        "Average Temperature": avg_temp,
        "Minimum Temperature": min_temp
    }
def humidity_trend(data, start_date, end_date):
    # Convert 'Date' column to datetime
    data['Date']=pd.to_datetime(data['Date'])

    # Convert start_date and end_date to datetime
    start_date=pd.to_datetime(start_date)
    end_date=pd.to_datetime(end_date)

    # Filter data between start_date and end_date
    filtered_df = data[(data.iloc[:,0]>= start_date) & (data.iloc[:,0] <= end_date)]

    # Find max and min humidity
    max_humidty = filtered_df['Humidity'].max()
    min_humidty = filtered_df['Humidity'].min()

    # Calculate the difference between max and min humidity
    Humidty_Increase = max_humidty-min_humidty

    # Return the humidity increase
    return {"Humidty increase by": Humidty_Increase}

def Highest_Wind(data, start_date, end_date):
    # Convert 'Date' column to datetime
    data.iloc[:,0]= pd.to_datetime(data.iloc[:,0])

    # Convert start_date and end_date to datetime
    start_date = pd.to_datetime(start_date)
    end_date = pd.to_datetime(end_date)

    # Filter data between start_date and end_date
    filtered_df = data[(data.iloc[:,0] >= start_date) & (data.iloc[:,0]<= end_date)]

    if not filtered_df.empty:
        # Find the row with the maximum wind speed
        max_wind_row = filtered_df.loc[filtered_df['WindGustSpeed'].idxmax()]

        # Extract the date with the highest wind speed
        date_with_highest = max_wind_row['Date']

        # Return the date with the highest wind speed
        return {"Date with Highest Wind Speed": date_with_highest}
    else:
        return "No data within the specified date range."
def Temperature_Analytics(data, start_date, end_date, output_file):
    start_date = pd.to_datetime(start_date)
    end_date = pd.to_datetime(end_date)

    # Filter data between start_date and end_date
    filtered_df = data[(data.iloc[:,0] >= start_date) & (data.iloc[:,0]<= end_date)]

    if filtered_df.empty:
        with open(output_file, 'w') as file:
            file.write("No data within the specified date range.")
        return

    # Calculate temperature statistics
    Temp_Stats = Temperatur_Operation(filtered_df, start_date, end_date)

    
    # Generate time series plot for temperature
    plt.figure(figsize=(12, 6))
    sns.lineplot(x=filtered_df['Date'], y=filtered_df['Temp'])
    plt.xlabel('Date')
    plt.ylabel('Temperature')
    plt.title('Temperature Time Series')
    plt.savefig('temperature_time_series.png')

    with open(output_file, 'w') as file:
        file.write("Temperature Time Series Plot saved as temperature_date_series.png\n")
def Wind_Analytics(data, start_date, end_date, output_file):
    start_date = pd.to_datetime(start_date)
    end_date = pd.to_datetime(end_date)

    # Filter data between start_date and end_date
    filtered_df = data[(data.iloc[:,0]>= start_date) & (data.iloc[:,0]<= end_date)]

    if filtered_df.empty:
        with open(output_file, 'w') as file:
            file.write("No data within the specified date range.")
        return

    
    # Generate time series plot for WindSpeed
    plt.figure(figsize=(12, 6))
    sns.lineplot(x=filtered_df['Date'], y=filtered_df['WindGustSpeed'])
    plt.xlabel('Date')
    plt.ylabel('Wind_Speed')
    plt.title('Wind_Speed over Time')
    plt.savefig('Wind_speed_series.png')

    with open(output_file, 'w') as file:
 
        file.write("Wind Speed Series Plot saved as WindSpeed_date_series.png\n")

def Humidity_Analytics(data, start_date, end_date, output_file):
    start_date = pd.to_datetime(start_date)
    end_date = pd.to_datetime(end_date)

    # Filter data between start_date and end_date
    filtered_df = data[(data.iloc[:,0]>= start_date) & (data.iloc[:,0]<= end_date)]

    if filtered_df.empty:
        with open(output_file, 'w') as file:
            file.write("No data within the specified date range.")
        return

    
    # Generate time series plot for Humidity
    plt.figure(figsize=(12, 6))
    sns.lineplot(x=filtered_df['Date'], y=filtered_df['Humidity'])
    plt.xlabel('Date')
    plt.ylabel('Humidity')
    plt.title('Humidity over Time')
    plt.savefig('Humidity_series.png')

    with open(output_file, 'w') as file:
 
        file.write("Humidity Series Plot saved as Humidity_series.png\n")        

def analysis(data, start_date, end_date, output_file):
    global data1
    # Get temperature statistics
    Temp_Stats = Temperatur_Operation(data1, start_date, end_date)

    # Get humidity trend
    Humidty_Diff = humidity_trend(data1, start_date, end_date)

    # Get date with highest wind speed
    Wind_Speed = Highest_Wind(data1, start_date, end_date)

    # Generate Temperature trend over the period of time in graph
    Temperature_Analytics(data1, start_date, end_date, output_file)
    
    # Generate wind trend over the period of time in graph
    Wind_Analytics(data1, start_date, end_date, output_file)
    
    # Generate Humidity trend over the period of time in graph
    Humidity_Analytics(data1, start_date, end_date, output_file)

    # Write results to file
    with open(output_file, 'w') as file:
        file.write("Temperature Stats:\n")
        for key, value in Temp_Stats.items():
            file.write(f"{key}: {value}\n")
        file.write("\n")

        file.write(f"Humidity Difference: {Humidty_Diff}\n\n")
        file.write(f"Date with Highest Wind Speed: {Wind_Speed}\n")


