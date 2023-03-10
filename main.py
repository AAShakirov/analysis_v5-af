import pandas as pd

all_matchs = pd.read_excel('statistics.xlsx')
df = all_matchs[['date', 'result']]
df.insert(2, 'count_win', [1 if df.loc[i]['result'] == 'win' else 0 for i in range(len(df))])
df.insert(3, 'count_lose', [1 if df.loc[i]['result'] == 'lose' else 0 for i in range(len(df))])

pd.options.mode.chained_assignment = None
for i in range(1, len(df)):
    if df.loc[i, 'date'] == df.loc[i-1, 'date']:
    # df.loc[df.loc[i]['count_win']] = df.loc[df.loc[i-1]['count_win']].values
        if df.loc[i, 'result'] == 'win':
            df.loc[i, 'count_win'] = df.loc[i-1, 'count_win'] + 1
            df.loc[i, 'count_lose'] = df.loc[i-1, 'count_lose']
        else:
            df.loc[i, 'count_win'] = df.loc[i-1, 'count_win']
            df.loc[i, 'count_lose'] = df.loc[i-1, 'count_lose'] + 1
df = df.drop_duplicates(subset='date', keep='last')
print(df)
print(df.mean(numeric_only=True))
print(df.median(numeric_only=True))
