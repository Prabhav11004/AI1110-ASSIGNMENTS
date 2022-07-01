#Name: Prabhav Singh
#Roll no. BT21BTECH11004

import numpy as np
import pandas as pd

#read raw data from excel sheet
df = pd.read_excel(r'raw_data.xlsx')
raw_data = np.array(df)

#creating the grouped frequency table
bin = [0.04*i for i in range(7)] 
h = np.histogram(raw_data,bins = bin)

#creating class intervals 
class_intervals = ["{}-{}".format(bin[i],bin[i+1]) for i in range(6)]
class_intervals.append("Total")

#adding the total at the end of frequency column
new = np.append(h[0],raw_data.size)

#creating dataframe of the grouped frequency table and writing to excel
dict = {"Conc. of sulphur dioxide (ppm)":class_intervals,"Frequency":new}
gtable = pd.DataFrame(dict) 
gtable.to_excel('Q14_Table.xlsx',index = False)

