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
#data_url = 'https://sheehan-carto.carto.com/api/v2/sql?q=SELECT * FROM yellow_tripdata_2015_04_verysmall&format=csv'
print data_url

url=data_url
s=requests.get(url).content
df=pd.read_csv(io.StringIO(s.decode('utf-8')))

#df = pd.read_csv(data_url)

print df.head(10)

for i in df.columns:
	print i

data_url = "https://%s.carto.com/api/v2/sql?q=SELECT * FROM %s tract_2010_acs_2014_5yr_vars   &format=csv" % (username1 , tablename)
#tract_2010_acs_2014_5yr_vars

data_url = "https://sheehan-carto.carto.com/api/v2/sql?q=SELECT vendorid, tpep_pickup_datetime,tpep_dropoff_datetime, passenger_count, trip_distance, pickup_longitude, pickup_latitude, ratecodeid, store_and_fwd_flag, dropoff_longitude, dropoff_latitude, payment_type, fare_amount, extra, mta_tax, tip_amount, tolls_amount, improvement_surcharge, total_amount, geoid FROM yellow_tripdata_2015_04_verysmall, tl_2014_census_tracts  WHERE ST_INTERSECTS(ST_SetSRID(ST_Point(yellow_tripdata_2015_04_verysmall.pickup_longitude, yellow_tripdata_2015_04_verysmall.pickup_latitude),4326), tl_2014_census_tracts.the_geom)&format=csv" #% (username1)

url=data_url
s=requests.get(url).content
df=pd.read_csv(io.StringIO(s.decode('utf-8')))

#df = pd.read_csv(data_url)

print df.head(10)

