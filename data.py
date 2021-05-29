import pandas as pd 
import statistics 
import csv 

df = pd.read_csv("height-weight.csv") 

height_list = df["Height(Inches)"].to_list() 
weight_list = df["Weight(Pounds)"].to_list()

height_mean = statistics.mean(height_list) 
weight_mean = statistics.mean(weight_list) 

height_median = statistics.median(height_list) 
weight_median = statistics.median(weight_list)

height_mode = statistics.mode(height_list) 
weight_mode = statistics.mode(weight_list) 

print(" the mean of height is " + str(height_mean))
print(weight_mean)
print("mean, mode and median of weight is " +str(height_mean)+ " , " +str(height_mode)+ " , " +str(height_median)+ " respectively")