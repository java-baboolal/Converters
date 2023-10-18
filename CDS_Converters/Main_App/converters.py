import json

# Reading JSON data is stored in a file named 'input.cdsEngine.json'
with open('input.cdsEngine.json', 'r') as json_file:
    data = json.load(json_file)

city_id = data["city_id"]
print('CityId : ', city_id)
areas = data["areas"]

area_list = []
zone_list = []
curb_list = []

for area in areas:
    area_list.append(area)
    for zone in area['zones']:
        zone_list.append(zone)
        for curb in zone['curb_spaces']:
            curb_list.append(curb)

print('###############################CURB LIST######################################')
print(curb_list)

print('###############################ZONE LIST######################################')
print(zone_list)

print('###############################AREA LIST######################################')
print(area_list)

for area in area_list:
    if "zones" in area:
        del area["zones"]
    print('############################### UPDATED AREA LIST######################################')
    print(area)

# with open('modified_data.json', 'w') as json_file:
#     json.dump(data, json_file, indent=4)


"""
For later use
import sqlite3

# Open a connection to the database
conn = sqlite3.connect('mydatabase.db')

# Read the file
with open('file.pdf', 'rb') as file:
    file_data = file.read()

# Insert the file data into the database
conn.execute('INSERT INTO files (data) VALUES (?)', [sqlite3.Binary(file_data)])

# Commit the transaction
conn.commit()

# Close the connection
conn.close()


"""