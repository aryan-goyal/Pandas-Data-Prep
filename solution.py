import pandas as pd
from io import StringIO

data = 'Airline Code;DelayTimes;FlightCodes;To_From\nAir Canada (!);[21, 40];20015.0;WAterLoo_NEWYork\n<Air France> (12);[];;Montreal_TORONTO\n(Porter Airways. );[60, 22, 87];20035.0;CALgary_Ottawa\n12. Air France;[78, 66];;Ottawa_VANcouvER\n""".\\.Lufthansa.\\.""";[12, 33];20055.0;london_MONTreal\n'

StringData = StringIO("""{}""".format(data))

df = pd.read_csv(StringData, sep=";")
# print("Intial Data:\n", df)

# 1 Find null rows, pandas series groupby (series.diff compares current and previous row)
nul = df.FlightCodes.isnull()
df.FlightCodes = nul.groupby(
    (nul.diff() == True).cumsum()).sum()*10 + df.FlightCodes.ffill()
df.FlightCodes = df.FlightCodes.astype('int')
# print("Cleaned FlightCodes:\n", df)

# 2
df[['To', 'From']] = df.To_From.str.split('_', expand=True)
df.To = df.To.str.upper()
df.From = df.From.str.upper()
df = df.drop(['To_From'], axis=1)
# print("Cleaned To_From:\n", df)

# 3
df['Airline Code'] = df['Airline Code'].str.replace(
    r'[^a-zA-Z]+', " ", regex=True)
df['Airline Code'] = df['Airline Code'].str.strip()
# print("Cleaned Airline Code:\n", df)

df.to_csv('cleanedData', sep=';', index=False)
print("Cleaned data:\n", df)
