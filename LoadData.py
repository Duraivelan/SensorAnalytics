#Load, clean and resample sensor data (CORE)
import pandas as pd
df = pd.read_csv("trace.csv", parse_dates=["ts"]).set_index("ts").sort_index()
df = df[~df.index.duplicated()] # remove duplicate timestamps
df = df.resample("1s").mean() # regular 1-second grid
df = df.interpolate(limit=5) # fill short gaps only
print(df.describe()) # sanity check ranges and NaNs
