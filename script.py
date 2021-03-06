# names of hurricanes
names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 'Labor Day', 'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille', 'Edith', 'Anita', 'David', 'Allen', 'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix', 'Matthew', 'Irma', 'Maria', 'Michael']

# months of hurricanes
months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 'September', 'September', 'September', 'September', 'October', 'September', 'August', 'September', 'September', 'August', 'August', 'September', 'September', 'August', 'October', 'September', 'September', 'July', 'August', 'September', 'October', 'August', 'September', 'October', 'September', 'September', 'October']

# years of hurricanes
years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977, 1979, 1980, 1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018]

# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160, 175, 175, 190, 185, 160, 175, 180, 165, 165, 160, 175, 180, 185, 175, 175, 165, 180, 175, 160]

# areas affected by each hurricane
areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'], ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'], ['The Bahamas', 'Northeastern United States'], ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'], ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], ['Jamaica', 'Yucatn Peninsula'], ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'], ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'], ['Bermuda', 'New England', 'Atlantic Canada'], ['Lesser Antilles', 'Central America'], ['Texas', 'Louisiana', 'Midwestern United States'], ['Central America'], ['The Caribbean', 'Mexico', 'Texas'], ['Cuba', 'United States Gulf Coast'], ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], ['Mexico'], ['The Caribbean', 'United States East coast'], ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'], ['Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'], ['The Caribbean', 'United States East Coast'], ['The Bahamas', 'Florida', 'United States Gulf Coast'], ['Central America', 'Yucatn Peninsula', 'South Florida'], ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'], ['The Caribbean', 'Venezuela', 'United States Gulf Coast'], ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], ['Bahamas', 'United States Gulf Coast'], ['Cuba', 'United States Gulf Coast'], ['Greater Antilles', 'Central America', 'Florida'], ['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'], ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'], ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'], ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic', 'Turks and Caicos Islands'], ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]

# damages (USD($)) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', '306M', '2M', '65.8M', '326M', '60.3M', '208M', '1.42B', '25.4M', 'Damages not recorded', '1.54B', '1.24B', '7.1B', '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B', '91.6B', '25.1B']

# deaths for each hurricane
deaths = [90,4000,16,3103,179,184,408,682,5,1023,43,319,688,259,37,11,2068,269,318,107,65,19325,51,124,17,1836,125,87,45,133,603,138,3057,74]

# write your update damages function here:
def updated_damages(list_damages):
  damages_not_recorded = []
  for i in list_damages:
    if i[-1] == "M":
      i = float(i[0:(len(i)-1)])*1000000
      damages_not_recorded.append(i)
    elif i[-1] == "B":
      i = float(i[0:(len(i)-1)])*1000000000
      damages_not_recorded.append(i)
    else: damages_not_recorded.append('Damages not recorded')
  return damages_not_recorded
damages = updated_damages(damages)
#print(damages)
# write your construct hurricane dictionary function here:
#function
def hurricanes_list(names, months, years, max_sustained_winds, areas_affected, damages, deaths):
  new_dictionary = {}  
  index = 0
  for items in names:
    new_dictionary[items] = ({"Name": names[index], "Month": months[index], "Year": years[index], "Max Sustained Wind": max_sustained_winds[index], "Areas Affected": areas_affected[index], "Damage": damages[index], "Deaths": deaths[index] })
    index = index + 1
  return new_dictionary
#print(hurricane(names, months, years, max_sustained_winds, areas_affected, damages, deaths))
hurricanes = hurricanes_list(names, months, years, max_sustained_winds, areas_affected, damages, deaths)
#loop + .update()

i = 0
new_dictionary2 = {}
for items in names:
  new_dictionary2.update({names[i]:{"Name": names[i], "Month": months[i], "Year": years[i], "Max Sustained Wind": max_sustained_winds[i], "Areas Affected": areas_affected[i], "Damage": damages[i], "Deaths": deaths[i] }})
  i = i + 1

#print(new_dictionary2)

# write your construct hurricane by year dictionary function here:
#function
def hurricanes_year(names, months, years, max_sustained_winds, areas_affected, damages, deaths):
  current_year = {}  
  index = 0
  for items in years:
    current_year[items] = ({"Name": names[index], "Month": months[index], "Year": years[index], "Max Sustained Wind": max_sustained_winds[index], "Areas Affected": areas_affected[index], "Damage": damages[index], "Deaths": deaths[index] })
    index = index + 1
  return current_year

#print(hurricanes_year(names, months, years, max_sustained_winds, areas_affected, damages, deaths))

#loop + .update()
i = 0
new_dictionary_year = {}
for items in names:
  new_dictionary_year.update({years[i]:{"Name": names[i], "Month": months[i], "Year": years[i], "Max Sustained Wind": max_sustained_winds[i], "Areas Affected": areas_affected[i], "Damage": damages[i], "Deaths": deaths[i] }})
  i = i + 1

#print(new_dictionary_year)

# write your count affected areas function here:
def count_affected_areas():
  affected_areas_list = {}
  for hurricane in hurricanes.values():
    for area in hurricane["Areas Affected"]:
      if area in affected_areas_list.keys():
        affected_areas_list[area] += 1 
      else:
        affected_areas_list[area]=1
        
  return affected_areas_list
#print(count_affected_areas())
affected_areas_dictionary = count_affected_areas()

# write your find most affected area function here:
#option 1
def max_hurricane_count():
    return max(affected_areas_dictionary,key=affected_areas_dictionary.get) 
max_hurricane_count_key = max_hurricane_count()
    
def max_hurricane_count1():    
    all_values = affected_areas_dictionary.values()
    return max(all_values)
max_hurricane_count_value = max_hurricane_count1()

affected_areas_count = {}
affected_areas_count[max_hurricane_count_key] = max_hurricane_count_value

#print(affected_areas_count)

#option2
def max_affected_area():
  most_affected_area = {}
  max_hit = 0
  max_area = ""
  for key, value in affected_areas_dictionary.items():
    if value > max_hit:
      max_hit = value
      max_area = key
      most_affected_area[max_area] = max_hit
  return most_affected_area

most_affected_area_dict = max_affected_area()

#print(max_affected_area())
#print(most_affected_area_dict)

# write your greatest number of deaths function here:
hurricane_mortality = {key:value for key, value in zip(names, deaths)}
print(hurricane_mortality)
def max_mortality_count():
  max_mortality = {}
  max_mortality_key = max(hurricane_mortality,key=hurricane_mortality.get) 
  max_mortality_value = max(hurricane_mortality.values())
  max_mortality[max_mortality_key] = max_mortality_value
  return max_mortality

print(max_mortality_count())







# write your catgeorize by mortality function here:







# write your greatest damage function here:







# write your catgeorize by damage function here:
