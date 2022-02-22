import pandas as pd
import plotly.express as px

pd.options.mode.chained_assignment = None

raw_df = pd.read_excel(
    '../data/timmar.xlsx',
    sheet_name='timmar',
    header=0)

# Filter rows
df = raw_df.query("Projektnummer == 2097")

df['YYMM'] = df['Datum'].dt.strftime('%Y-%m')

df['hours'] = df['Timmar'][:-3].astype(float)

# print(df.head())

# for i in range(0, len(df)):
#    df.iloc[i].Timmar = df.iloc[i].Timmar[:-3]

df1 = df.groupby(['YYMM', 'Person'])['hours'].sum().reset_index()

fig = px.bar(df1, x="YYMM", y="hours", color="Person", barmode='stack')

fig.show()

df["hourssum"] = df.groupby(["Person"])["hours"].transform(sum)

df2 = df.groupby(['Person'])['hours'].sum().reset_index()

fig2 = px.bar(df2, x="Person", y="hours")

fig2.show()