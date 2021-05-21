import pandas as pd
from io import StringIO

data = 'Airline Code;DelayTimes;FlightCodes;To_From\nAir Canada (!);[21, 40];20015.0;WAterLoo_NEWYork\n<Air France> (12);[];;Montreal_TORONTO\n(Porter Airways. );[60, 22, 87];20035.0;CALgary_Ottawa\n12. Air France;[78, 66];;Ottawa_VANcouvER\n""".\\.Lufthansa.\\.""";[12, 33];20055.0;london_MONTreal\n'

StringData = StringIO("""{}""".format(data))

df = pd.read_csv(StringData, sep=";")
print(df)

# 1 FlightCodes column: Some values are null. Flight Codes are supposed to increase by 10
