counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}
#for county in counties_dict.keys():
 #   print(county)

#for voters in counties_dict:
 #   print(counties_dict[voters])    

#for key, value in counties_dict.items():
 #   print (key, value)

for county, voters in counties_dict.items():
    print(f"{county} county has {voters} registered voters.")