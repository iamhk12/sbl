import pandas as pd
series1 = pd.Series([10, 20, 30, 40], name="Series 1")
series2 = pd.Series([1, 2, 3, 4], name="Series 2")
data_frame = pd.concat([series1, series2], axis=1)
print("Data Frame:")
print(data_frame)
print("\nAccessing Specific Columns:")
column_1 = data_frame["Series 1"]
column_2 = data_frame["Series 2"]
print("Series 1:")
print(column_1)
print("Series 2:")
print(column_2)
print("\nBasic Operations:")
data_frame["Sum"] = data_frame["Series 1"] + data_frame["Series 2"]
data_frame["Product"] = data_frame["Series 1"] * data_frame["Series 2"]
data_frame["Mean"] = data_frame[["Series 1", "Series 2"]].mean(axis=1)
print(data_frame)
print("\nFiltering Data:")
filtered_data = data_frame[data_frame["Series 1"] > 20]
print(filtered_data)