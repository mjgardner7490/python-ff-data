import pandas as pd


df = pd.read_csv('https://raw.githubusercontent.com/fantasydatapros/LearnPythonWithFantasyFootball/master/2023/06-Data%20Munging/01-FDP%20Projections%20-%20(2023.03.30).csv')

# First 5 rows
# print(df.head())

# First 10 rows
# print(df.head(10))

# First 3 rows
# print(df[:3])

# Print rows 10 to 14 and first 10 columns
# print(df.iloc[10:15, 0:10])

# Print columns
# print(df.columns)
# print(', '.join(df.columns))


# Calculate new column FantasyPoints
scoring_weights = {
    'receptions': 0.5,
    'receiving_yds': 0.1,
    'receiving_td': 6,
    'rushing_yds': 0.1,
    'rushing_td': 6,
    'passing_yds': 0.04,
    'passing_td': 4,
    'int': -2
}

df['FantasyPoints'] = (
    df['Receptions']*scoring_weights['receptions'] + df['ReceivingYds']*scoring_weights['receiving_yds'] + \
    df['ReceivingTD']*scoring_weights['receiving_td'] + \
    df['RushingYds']*scoring_weights['rushing_yds'] + df['RushingTD']*scoring_weights['rushing_td'] + \
    df['PassingYds']*scoring_weights['passing_yds'] + df['PassingTD']*scoring_weights['passing_td'] + \
    df['Int']*scoring_weights['int'])

# print(df.head())


