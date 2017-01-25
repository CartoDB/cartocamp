import json
import pandas as pd 
import requests
import io
# modify credentials.json.sample
cred = json.load(open('credentials.json'))

username = cred['username']
api_key  = cred['api_key']

#input_data_url = 'https://team.carto.com/u/sheehan-carto/dataset/yellow_tripdata_2015_04_verysmall'

username1  = 'sheehan-carto'
tablename = 'yellow_tripdata_2015_04_verysmall'

#url = "http://"+cartodb_domain+".cartodb.com/api/v2/sql?q=SELECT%20*%20FROM%20"+tablename+"&format=csv&api_key="+API_KEY

data_url = "https://%s.carto.com/api/v2/sql?q=SELECT * FROM %s&format=csv" % (username1 , tablename)
data_url = 'https://sheehan-carto.carto.com/api/v2/sql?q=SELECT * FROM yellow_tripdata_2015_04_verysmall&format=csv'
print data_url

url=data_url
s=requests.get(url).content
df=pd.read_csv(io.StringIO(s.decode('utf-8')))

#df = pd.read_csv(data_url)

print df.head(10)

# 2:30 - 3 pm - Getting setup (CARTO accounts, API keys, programming environment, etc.)
# HOWTO
# Fill in credentials

# 3:00 pm - Introduction to maps with data science
# Spatial data
# Cool things we've seen
# Tools?
# 3:10 pm - Getting setup
# See 2:30 pm above
# 3:15 pm - Basics on workflows?
# Generate SQL query to get the data that you want, stressing that they should only pick a 24 hour period of time OR Import API to directly get custom queried data into their accounts (via URL)
# Read from Carto (pandas.read_csv and SQL API, format csv)
# Intersect Taxi Points w/ Admin Geographies, read to DataFrame, Groupby, join to Admin Geog Boundaries
# Write to disk
# request.post() to send to CARTO OR Python Client create_vis='True' to create their first map
# Gain intuition of the data in pandas
# 3:30 pm - Static and Interactive Maps
# Python template code for generating Maps with the Maps API
# Start with generic Carto maps and styles
# Then show them how to tune the map;
# Styles
# TurboCarto
# Zoom and Center Map
# 3:40 - Spatial Statistics?
# Getis-Ord's G*? Moran's I? K-means, etc.
# Data Observatory to contextualize information

# 3:45 - 4:00 pm - Discussion