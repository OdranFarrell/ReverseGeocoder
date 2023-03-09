import pandas as pd
from geopy.geocoders import Nominatim
import time
from tqdm import tqdm
import os

#Find file
file = '/Users/odran/Desktop/Dissertation Data Work/Co-ordinates and Addresses.xlsx'

#transform into dataframe
df = pd.read_excel(file)

geolocator = Nominatim(user_agent="http")


Address = []
Province = []
cleaned_list = []

#Iterate through coords
for coord in tqdm(df['Coords']):
    location = geolocator.reverse(coord)
    Address.append(location.address)
    words = location.address.split(",")
    for string in words:
        if not any(char.isdigit() for char in string):
            cleaned_list.append(string)
    province = cleaned_list[-3]
    Province.append(province)
    time.sleep(0.2)

#Save new dataframe
df_new = df.head(20).assign(Address=Address, Province=Province)

df_new.to_excel("/Users/odran/Desktop/Dissertation Data Work/ReverseGeoCodedResults.xlsx")