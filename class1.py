from unittest import result
import pandas as pd
import statistics
import csv

df = pd.read_csv("data.csv")

height_list = df["Height"].tolist()
weight_list = df["Weight"].tolist()

height_mean = statistics.mean(height_list)
weight_mean = statistics.mean(weight_list)

height_median = statistics.median(height_list)
weight_median = statistics.median(weight_list)

height_mode = statistics.mode(height_list)
weight_mode = statistics.mode(weight_list)

print("mean,median,mode of height is {},{},{}".format(height_mean,height_median,height_mode))
print("mean,median,mode of weight is {},{},{}".format(weight_mean,weight_median,weight_mode))

height_stDev = statistics.stdev(height_list)
weight_stDev = statistics.stdev(weight_list)

heightFirstStdevStart,heightFirstStdevend = height_mean-height_stDev, height_mean+height_stDev
heightSecondStdevStart,heightSecondStdevend = height_mean-(2*height_stDev), height_mean+(2*height_stDev)
heightThirdStdevStart,heightThirdStdevend = height_mean-(3*height_stDev), height_mean+(3*height_stDev)

weightFirstStdevStart,weightFirstStdevend = weight_mean-weight_stDev, weight_mean+weight_stDev
weightSecondStdevStart,weightSecondStdevend = weight_mean-(2*weight_stDev), weight_mean+(2*weight_stDev)
weightThirdStdevStart,weightThirdStdevend = weight_mean-(3*weight_stDev), weight_mean+(3*weight_stDev)

heightListOfDataWithinFirstStdev = [result for result in height_list if result > heightFirstStdevStart and result < heightFirstStdevend]
heightListOfDataWithinSecondStdev = [result for result in height_list if result > heightSecondStdevStart and result < heightSecondStdevend]
heightListOfDataWithinThirdStdev = [result for result in height_list if result > heightThirdStdevStart and result < heightThirdStdevend]

weightListOfDataWithinFirstStdev = [result for result in weight_list if result > weightFirstStdevStart and result < weightFirstStdevend]
weightListOfDataWithinSecondStdev = [result for result in weight_list if result > weightSecondStdevStart and result < weightSecondStdevend]
weightListOfDataWithinThirdStdev = [result for result in weight_list if result > weightThirdStdevStart and result < weightThirdStdevend]

print("{}% Of data for height lies within first standard deviation".format(len(heightListOfDataWithinFirstStdev)*100.0/len(height_list)))
print("{}% Of data for height lies within second standard deviation".format(len(heightListOfDataWithinSecondStdev)*100.0/len(height_list)))
print("{}% Of data for height lies within third standard deviation".format(len(heightListOfDataWithinThirdStdev)*100.0/len(height_list)))

print("{}% Of data for weight lies within first standard deviation".format(len(weightListOfDataWithinFirstStdev)*100.0/len(weight_list)))
print("{}% Of data for weight lies within second standard deviation".format(len(weightListOfDataWithinSecondStdev)*100.0/len(weight_list)))
print("{}% Of data for weight lies within third standard deviation".format(len(weightListOfDataWithinThirdStdev)*100.0/len(weight_list)))