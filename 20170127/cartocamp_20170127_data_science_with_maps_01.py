import json

# modify credentials.json.sample
cred = json.load(open('credentials.json'))

username = cred['username']
api_key  = cred['api_key']


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