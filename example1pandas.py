import pandas as pd
calories={"day1":1000,"day2":2000,"day3":3000,"day4":4000,"day5":5000,"day6":6000,"day7":7000}
series=pd.Series(calories)
print(series)
print(series.loc["day1"])
series.loc["day2"]+=1000
print(series.loc["day2"])
series.loc["day3"]+=5000
print(series.loc["day3"])

print(series[series<2000])