import pandas as pd
import numpy as np
import seaborn as sns


def getMeanValue(data, columnName):
  return data[['stationId', columnName]].groupby(['stationId'], as_index=False).mean()


def getData(dataPath, isBeijing=False):
  train_df = pd.read_csv(dataPath)
  pm_two = getMeanValue(train_df, 'PM2.5')
  pm_ten = getMeanValue(train_df, 'PM10')
  data = [pm_two, pm_ten]

  if (isBeijing):
    o_three = getMeanValue(train_df, 'O3')
    data.append(o_three)

  return data

def writeFile(output, data):
  for id, station in enumerate(data[0]['stationId']):
    for hour in range(48):
      output.write(data[0]['stationId'][id])
      output.write('#' + str(hour))
      output.write(',')
      output.write(str(data[0]['PM2.5'][id]))
      if (str(data[1]['PM10'][id]) != 'nan'):
        output.write(',')
        output.write(str(data[1]['PM10'][id]))
      if(len(data) > 2):
        output.write(',')
        output.write(str(data[2]['O3'][id]))
      output.write('\n')

dataBeijing = getData('./data/beijing/beijing_17_18_aq.csv', isBeijing=True)
dataLondon_1 = getData('./data/london/London_historical_aqi_forecast_stations_20180331.csv')

with open('submission.csv', 'w') as output:
  output.write('test_id,PM2.5,PM10,O3\n')
  writeFile(output, dataBeijing)
  writeFile(output, dataLondon_1)
  
