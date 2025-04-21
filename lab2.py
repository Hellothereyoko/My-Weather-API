#! /usr/bin/env python3
"""
This program takes a domain passed into the terminal and plots
the weather forecast by the hour.

*** For More Detailed Info Refer to README.md *** 

Author: Yoko Parks
Class:  CSCD 330 EWU Tony Espinoza
Date:   16 April 2025

"""


from json import loads  # steps 3, 4
from requests import get  # steps 3, 4
from socket import gethostbyname  # step 1
from subprocess import getstatusoutput  # step 2
from sys import argv  # command line arguments
import matplotlib.pyplot as plt #for temp plotting function
import numpy as np #for temp plotting function



# Takes an array of temps
# and plots them.
def plot_temps(temps):
    xs = [x for x in range(len(temps))]
    plt.plot(xs, temps, label="Hourly Temperatures")

    # Label the x and y:
    plt.xlabel("Hour")
    plt.ylabel("Temperature F.")

    # Make sure we show the legend:
    plt.legend()

    # Show the plot:
    plt.show()


# Step 1:
# Lookup Domain & Resolve to IP
def resolve_domain(domain):
   
   # Executed Function:
   try:
      # Pass Domain to Bash & Fetch IP:
      ip= gethostbyname(domain)
      return ip
   
   # Error for Domain Resolution:
   except:
      print("Sorry, I Couldn't Resolve the Domain :(")
      quit() 


# Step 2a:
# Resolve IP to physical address
def get_whois(ip):
   
   # Executed Function:
   try:
      # Pass CMD to Bash & fetch WhoIS:
      status, out= getstatusoutput(f"whois {ip}")
      return out

   # Error for IP Resolution:
   except:
      print("whois resolution failed")   
      quit()


# Step 2b:
# Parse Whois
def parse_whois(whois_out):

   # Executed Function:
   try:	
      # Object to Store Address:
      fields = {
         'OrgName': None,
         'Address': None,
         'City': None,
         'State': None,
         'Postal Code': None,
         'Country': None,
      }

      # Mapping to Query Fields:
      mapping = {
         'OrgName': 'OrgName',
         'Address': 'Address',
         'City': 'City',
         'State': 'State',
         'StateProv': 'StateProv',
         'Province': 'State',
         'PostalCode': 'Postal Code',
         'Zip': 'Postal Code',
         'Country': 'Country',
      }

      # Traverse Output For Matching Fields:
      for line in whois_out.splitlines():
         line = line.strip()
         for whois_key, field_name in mapping.items():
            if line.startswith(f"{whois_key}:"):
               fields[field_name] = line.split(":", 1)[1].strip()

               break
      
      # Returns Stored Address:
      return fields

   # Error for Phys Address Resolution:
   except:
      print("I Wasn't Able To Return A Physical Address")
      quit()

 
#Step 3:
#Resolve to Lat & Long Coord  (Long is inversed) via API
def lat_lon(whois_info):
   
   # Executed Function:
   try:
      # Address in API Format Variables:
      street= whois_info.get("Address")
      city= whois_info.get("City")
      state= whois_info.get("StateProv")
      zip= whois_info.get("PostalCode")
   
      # Sanitize inputs for URL formatting:
      address = f"{street}, {city}, {state}, {zip}".replace(" ", "%20")
   
      # The API URL:
      api_call = f"https://geocoding.geo.census.gov/geocoder/locations/address?street={street}&city={city}&state={state}&zip={zip}&benchmark=Public_AR_Current&format=json"
    
      # Execute API Call:
      response=get(api_call)
   
      # !!! DEBUG PRINT STATEMENT !!!
      print("")
      print("[+] Geocoding URL:")
      print(api_call)
      print("")

      # Output Data Becomes JS:
      coord_js= loads(response.text)
   
      # Extract Coordinates:
      coords = coord_js['result']['addressMatches'][0]['coordinates']
      lon = coords['x']
      lat = coords['y']
      
      # !!! DEBUG PRINT STATEMENT !!!
      print(f"[+] Coordinates: {lat}, {lon}")
      print("")

      return lat, lon
    
   # Error for Coordinate Resolution:
   except:
      print("I Couldn't Find The Coordinates :0")
      quit()

#Step 4: 
#Pull Weather for Location (Hourly)
#https://weather-gov.github.io/api/general-faqs
def get_weather( lat, lon):
   
   # Executed Function:   
   try:
      # Get API_URL:
      forecast_api_call= f"https://api.weather.gov/points/{lat},{lon}"    
      weather_response= get(forecast_api_call)
      weather_js=loads(weather_response.text)

      # Execute Hourly Forecast Fetch:
      try:
         # Fetch Hourly Forecast URL:
         hourly_url= weather_js['properties']['forecastHourly']

         # !!! DEBUG STATEMENT !!!
         print(f"[+] Weather URL: {hourly_url}")
         print("")

         # Fetch Forecast Data:
         hourly_weather= get(hourly_url)
         hourly_js= loads(hourly_weather.text)

         # !!! DEBUG STATEMENT !!!
         # API Response Raw:
         # print("[DEBUG] hourly_js keys:", hourly_js.keys())
         # print("[DEBUG] Full hourly_js response:")
         # print(hourly_js)

         temps = [period['temperature'] for period in hourly_js['properties']['periods'][:160]]
         print(f"[+] Temperatures: {temps}")
	 

         return temps
      
      # Error for Fetch Weather Forecast:
      except:
         print("I Couldn't Find Weather Data For That Location. >:(")
         quit()

   # Error for API Call:
   except:
      print("I Couldn't Get a Valid Response From The API")
      quit()



def main():
   
   # Pass Shell 'argv[1]' as Domain (Step 1):
   domain = argv[1]
   ip = resolve_domain(domain)

   # Assign 'whois_data' To 'get_whois' Function Passing ip (Step 2a):
   whois_data = get_whois(ip)

   # Make 'whois_info' object via 'parse_whois' (Step 2b):
   whois_info = parse_whois(whois_data)

   # Use 'whois_info' to resolve lat/lon (Step 3):
   lat, lon = lat_lon(whois_info)

   # Use Coords To Get Weather Data (Step 4):
   temps = get_weather(lat, lon)

   # Plot The Temps (Step 5):
   plot_temps(temps)

   

if __name__ == "__main__":
    main()
