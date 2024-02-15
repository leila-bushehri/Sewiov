#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from datetime import datetime


# In[1]:


import seaborn as sns
get_ipython().system('pip install scikit-learn')
import matplotlib.pyplot as plt


# In[210]:


import pandas as pd
import datetime
import time
import collections

df = pd.read_csv('probe.txt',names=['feed_id', 'zone_id','status','Time'], header=None)



#df
#sorted_df = df.sort_values(by=['feed_id'] , ascending=True)
#pd.set_option('display.max_rows', 1762)
#sorted_df

#gp=df.groupby(["feed_id",'zone_id'])
#for name, group in df.groupby(["feed_id",'zone_id']):
    #print(name)
    #print(group)

#grouped_index = df.apply(lambda x: x.reset_index(drop = True)).reset_index()
#grouped_index

#for name, group in df.groupby(["feed_id","zone_id"]):
#    print(df)

grouped_df = df.groupby(["feed_id","zone_id"])

for key,item in grouped_df:
    a_group = grouped_df.get_group(key)
    a_group.reset_index(drop=True, inplace=True)
    print(key)
    print(a_group)
    

#type(a_group)
#gp.first()
#gp
#type(gp)
#x=[gp.get_group(x) for x in gp.groups]
#type(x)


# In[224]:


a_group = a_group.sort_values('Time')
assert(a_group.loc[0, 'status'] == 'in')
for i, row in a_group.iterrows():
    if row['status'] == 'in':
        j = i
    else:
        assert(row['status'] == 'out')
        assert(i == j+1)
        a_group.loc[j, 'Time out'] = row['Time']


# In[233]:


in_time = a_group[a_group['status'] == 'in'].reset_index()
out_time = a_group[a_group['status'] == 'out'].reset_index()
assert(in_time.shape == out_time.shape)
in_time.rename(columns = {'Time': 'In Time'}, inplace = True)
out_time.rename(columns = {'Time': 'Out Time'}, inplace = True)


# In[234]:


pd.concat([in_time['In Time'], out_time['Out Time']], axis = 1)


# In[168]:


from datetime import datetime

total_diff = 0
date_format_str = '%Y-%m-%d %H:%M:%S.%f'


# In[241]:


time_in_out = pd.DataFrame([])
for key, item in grouped_df:
    a_group = grouped_df.get_group(key)
    a_group = a_group.sort_values('Time')
    a_group.reset_index(drop=True, inplace=True)
    j = None
#    assert(a_group.loc[0, 'status'] == 'in')
    for i, row in a_group.iterrows():
        if row['status'] == 'in':
            j = i
        else:
            assert(row['status'] == 'out')
            if j is None:
                continue
            assert(i == j+1)
            a_group.loc[j, 'Time out'] = row['Time']      
    time_in_out = time_in_out.append(a_group[a_group['status'] == 'in'])


# In[244]:


time_in_out['Time out'] = pd.to_datetime(time_in_out['Time out'])
time_in_out['Time'] = pd.to_datetime(time_in_out['Time'])


# In[245]:


time_in_out['diff'] = time_in_out['Time out'] - time_in_out['Time']


# In[254]:


time_in_out


# In[207]:


for i in range(1,len(a_group)):
    if df['status'].iloc[i] == 'in':
        continue
    else:        
        date_1 = a_group['Time'].iloc[i-1]
        date_2 = a_group['Time'].iloc[i]

        start = datetime.strptime(date_1, date_format_str)
        end =   datetime.strptime(date_2, date_format_str)
        # Get interval between two datetimes as timedelta object
        diff = (end - start)
        total_diff += diff.total_seconds()
        

# Get the interval in minutes
diff_in_minutes = diff.total_seconds() / 60
print('Difference between two datetimes in second:')
print(total_diff)
print('Difference between two datetimes in minutes:')
print(diff_in_minutes)
print (diff)


print (date_1)
print (date_2)
print (a_group.shape)


# In[ ]:





# In[172]:


x=df.groupby(["feed_id",'zone_id']).get_group((22, 8))
x


# In[188]:


a = []         
a

#result=pd.DataFrame(columns=['time_diff'])
#result["time_diff"] = pd.to_datetime(result)
#result


# In[209]:


from datetime import datetime
for i in range(1,len(x)):
    if df['status'].iloc[i] == 'in':
        continue
    else:        
        date_1 = df['Time'].iloc[i-1]
        date_2 = df['Time'].iloc[i]

        start = datetime.strptime(date_1, date_format_str)
        end =   datetime.strptime(date_2, date_format_str)
        # Get interval between two datetimes as timedelta object
        diff = (end - start)
        #result=result.append(diff)
        total_diff += diff.total_seconds()
        print(str(diff))



        

# Get the interval in minutes
diff_in_minutes = diff.total_seconds() / 60
print('Difference between two datetimes in second:')
print(total_diff)
print('Difference between two datetimes in minutes:')
print(diff_in_minutes)

print(date_1)
print(date_2)
type(total_diff)

