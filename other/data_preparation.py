import pandas as pd
import biogeme.database as db
import biogeme.biogeme as bio
from IPython.core.display_functions import display
from biogeme.expressions import Beta, Variable
from biogeme.models import loglogit
from biogeme.segmentation import DiscreteSegmentationTuple, segmented_beta

# Load the data
df = pd.read_csv("lpmc01.dat", sep = '\t')
df['age_scaled'] = (df['age'] - df['age'].mean()) / df['age'].std()
df['cost_driving'] = df['cost_driving_ccharge'] + df['cost_driving_fuel']
df['dur_pt'] = df['dur_pt_access'] + df['dur_pt_rail'] + df['dur_pt_int'] + df['dur_pt_bus']

database1 = db.Database('lpmc01', df)


# Define the given veriables 
dur_pt = Variable('dur_pt')
cost_driving = Variable('cost_driving')
age_scaled = Variable('age_scaled')
trip_id = Variable('trip_id')
household_id = Variable('household_id')
person_n = Variable('person_n')
trip_n = Variable('trip_n')
travel_mode = Variable('travel_mode')
purpose = Variable('purpose')
fueltype = Variable('fueltype')
faretype = Variable('faretype')
bus_scale = Variable('bus_scale')
survey_year = Variable('survey_year')
travel_year = Variable('travel_year')
travel_month = Variable('travel_month')
travel_date = Variable('travel_date')
day_of_week = Variable('day_of_week')
start_time = Variable('start_time')
age = Variable('age')
female = Variable('female')
driving_license = Variable('driving_license')
car_ownership = Variable('car_ownership')
distance = Variable('distance')
dur_walking = Variable('dur_walking')
dur_cycling = Variable('dur_cycling')
dur_pt_access = Variable('dur_pt_access') # Predicted total access and egress time for public transport route in hours
dur_pt_rail = Variable('dur_pt_rail')
dur_pt_bus = Variable('dur_pt_bus')
dur_pt_int = Variable('dur_pt_int') # Time taken (hrs) at each interchange point
pt_interchanges = Variable('pt_interchanges')   # Number of interchange points in public transport route
dur_driving = Variable('dur_driving')
cost_transit = Variable('cost_transit')
cost_driving_fuel = Variable('cost_driving_fuel')   # Estimated fuel cost of driving route in GBP
cost_driving_ccharge = Variable('cost_driving_ccharge')  # Estimated congestion charge cost of driving route in GBP
driving_traffic_percent = Variable('driving_traffic_percent')


# Define new variables:
# # Define driving cost 
# df['cost_driving'] = df['cost_driving_ccharge'] + df['cost_driving_fuel']
# cost_driving = Variable(cost_driving_ccharge + cost_driving_fuel)

# # Define time taken by each mode of transport
# df['dur_pt'] = df['dur_pt_access'] + df['dur_pt_rail'] + df['dur_pt_int'] + df['dur_pt_bus']
# dur_pt = Variable(dur_pt_access + dur_pt_rail + dur_pt_int + dur_pt_bus)


# Define transport availability
# Assume pt, walking, cycle always available, with car availability depending on number of cars per household. From the data, 
# people without driving licenses choose driving as their mode of transport (eg. row 28). 
av_drive =  (car_ownership > 0)
av_pt =1
av_walk = 1
av_cycle = 1

variable_names = ['dur_pt', 'cost_driving', 'age_scaled']  # Replace with your variable name
for variable_name in variable_names:
    if variable_name in database1.data.columns:
        print(f"'{variable_name}' exists in the database.")
    else:
        print(f"'{variable_name}' does NOT exist in the database.")



# Define pt_cost (not needed)
# Original paper, page 31: "Public transport fares are determined for single trips using Oystercard/contactless payment."
# Therefore, cost_transit should already consider faretype and bus_scale

database = db.Database('lpmc01', df)
variable_names = ['dur_pt', 'cost_driving', 'age_scaled']  # Replace with your variable name
for variable_name in variable_names:
    if variable_name in database1.data.columns:
        print(f"'{variable_name}' exists in the database.")
    else:
        print(f"'{variable_name}' does NOT exist in the database.")