# Assingment by using numpy

# import Modules
import numpy as np
import pandas as pd

# Load json file
data = pd.read_json('data.json')

# normalize json format
social_D = pd.DataFrame(data['social_D'].tolist())
price_D = pd.DataFrame(data['price_D'].tolist())

#################
# Question No 1 #
#################

print(social_D.describe().loc[['min','max','mean'],'90day_bull_prop_rollingz_60'])
print(social_D.describe().loc[['min','max','mean'],'cumulative_abs'])
print(price_D.describe().loc[['min','max','mean'],'volume'])
print(price_D.describe().loc[['min','max','mean'],'last'])

#################
# Question No 2 #
#################

sorted_last = price_D.sort_values('last', ascending=False)
print(sorted_last['date'][:3])

#################
# Question No 3 #
#################

s_D = social_D.set_index('date')
p_D = price_D.set_index('date')

final_csv = p_D.join(s_D, how='outer')
final_csv = final_csv.loc[:,['last','90day_bull_prop_rollingz_60','cumulative_z']]
final_csv.reset_index(inplace=True)
final_csv.to_csv('data.csv')

