import tradingeconomics as te

te.login()
df = te.getRatings(country=['United states','United Kingdom','India','Japan','Russia'], output_type='df')
print(df)
print(df.columns)
print(df[['Country','SP','Moodys','Fitch']])
