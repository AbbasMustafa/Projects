import json

f = open('data.json')
data = json.load(f)

################# 
# Question No 1 #
################# 
def min_max_mean(first, second):
  values = [x[second] for x in data[first]]
  minimum = min(values)
  maximum = max(values)
  mean_value = sum(values)/len(values)
  return (minimum, maximum, mean_value)

# 'social_D' -> '90day_bull_prop_rollingz_60'
minimum, maximum, mean_value = min_max_mean('social_D',
												 '90day_bull_prop_rollingz_60')
print(f"min of social_D' -> '90day_bull_prop_rollingz_60: {minimum}")
print(f"max of social_D' -> '90day_bull_prop_rollingz_60: {maximum}")
print(f"avg of social_D' -> '90day_bull_prop_rollingz_60: {mean_value}")

# 'social_D' -> 'cumulative_abs'
minimum, maximum, mean_value = min_max_mean('social_D',
												 'cumulative_abs')
print(f"min of social_D' -> 'cumulative_abs: {minimum}")
print(f"max of social_D' -> 'cumulative_abs: {maximum}")
print(f"avg of social_D' -> 'cumulative_abs: {mean_value}")

# 'price_D' -> 'vloume'
minimum, maximum, mean_value = min_max_mean('price_D',
												 'volume')
print(f"min of price_D' -> 'volume: {minimum}")
print(f"max of price_D' -> 'volume: {maximum}")
print(f"avg of price_D' -> 'volume: {mean_value}")

# 'price_D' -> 'last'
minimum, maximum, mean_value = min_max_mean('price_D',
												 'last')
print(f"min of price_D' -> 'last': {minimum}")
print(f"max of price_D' -> 'last': {maximum}")
print(f"avg of price_D' -> 'last': {mean_value}")

############ End Question 1 ##########################

#################
# Question No 2 #
#################

# Top three highest closing days for the stock
closing = {}
for i in data['price_D']:
  closing[i['date']] = i['last']

for key in sorted(closing, key=closing.get, reverse=True)[:3]:
  print(f"{key}")

###########  End Question 2 ####################

#################
# Question No 3 #
#################

list_date = {}
with open('data.csv','w') as f:
  f.write('date,90day_bull_prop_rollingz_60,cumulative_z,last\n')
  for i in data['social_D']:
    for j in data['price_D']:
      if i['date'] == j['date']:
        f.write("{},{},{},{}\n".format(j['date'],
          i['90day_bull_prop_rollingz_60'],
          i['cumulative_z'],
          j['last']))

        list_date[i['date']] = 0

with open('data.csv','a') as f:
  for i, j in zip(data['social_D'],data['price_D']):
    if i['date'] not in list_date:
      f.write("{},{},{},{}\n".format(i['date'],
        i['90day_bull_prop_rollingz_60'],
        i['cumulative_z'],
        ""))
    if  j['date'] not in list_date:
      f.write("{},{},{},{}\n".format(j['date'],
        "",
        "",
        j['last']))



######### End Question 3 #################

