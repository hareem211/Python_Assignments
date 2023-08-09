import csv

def read_weather_data(file_path):
    weather_data = []
    with open( r"weatherAUS.csv") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            weather_data.append(row)
        return weather_data
def calculate_avg_temperatures(file-path):
    avg_min_temp = {}
    avg_max_temp = {}
    for entry in weather_data:
     date = entry['Date']
     month = date.split('-')[1]
     month = input("enter month to check temp")
     if entry['MinTemp'] == 'NA':
         min_temp == 0.0
     else:    
      min_temp = float(entry['MinTemp'])
    if entry['MaxTemp'] == 'NA':
        max_temp =0.0
    else:     
      max_temp = float(entry['MaxTemp'])
    
    if month not in avg_min_temp:
            avg_min_temp[month] = [min_temp]
            avg_max_temp[month] = [max_temp]
    else:
            avg_min_temp[month].append(min_temp)
            avg_max_temp[month].append(max_temp)

    for month in avg_min_temp:
        avg_min_temp[month] = sum(avg_min_temp[month]) / len(avg_min_temp[month])
        avg_max_temp[month] = sum(avg_max_temp[month]) / len(avg_max_temp[month])
        return avg_min_temp, avg_max_temp
def find_highest_rainfall_each_year(file_path):
    highest_rainfall = {}
    for entry in weather_data:
        date = entry['Date']
        year = date.split('-')[0]
        if entry['Rainfall'] == 'NA':
         rainfall = 0.0
        else:
         rainfall = float(entry['Rainfall'])

        if year not in highest_rainfall:
            highest_rainfall[year] = rainfall
        else:
            if rainfall > highest_rainfall[year]:
                highest_rainfall[year] = rainfall

    return highest_rainfall
def find_min_pressure_at_9am(file_path):
    min_pressure_9am = float('inf')
    for entry in weather_data:
        if entry['Pressure9am'] == 'NA':
            Pressure9am = 0.0
        else:
         pressure_9am = float(entry['Pressure9am'])
        if pressure_9am < min_pressure_9am:
            min_pressure_9am = pressure_9am

    return min_pressure_9am
path = input("input_file_path")
weather_data = read_weather_data(path)

avg_min_temp, avg_max_temp = calculate_avg_temperatures(weather_data)
highest_rainfall_each_year = find_highest_rainfall_each_year(weather_data)
min_pressure_9am = find_min_pressure_at_9am(weather_data)

print("Average Minimum Temperatures by Month:")
print(avg_min_temp)

print("\nAverage Maximum Temperatures by Month:")
print(avg_max_temp)

print("\nHighest Rainfall of Each Year:")
print(highest_rainfall_each_year)

print("\nMinimum Pressure at 9 AM:")
print(min_pressure_9am)
