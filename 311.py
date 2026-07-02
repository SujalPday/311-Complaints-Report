import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv(r"(Paste Location Here)")

# Monthly volume trend
monthly = df.groupby('year_month').size().reset_index(name='count')

# Complaints by borough
by_borough = df.groupby('borough').size().reset_index(name='count')

# Top complaint types
top_complaints = df['complaint_type'].value_counts().head(15)

# Borough × Year heatmap data
bor_year = df.groupby(['borough', 'year']).size().unstack(fill_value=0)

# Avg resolution time by agency
res_time = df.groupby('agency')['resolution_hours'].median().sort_values()

# 1. Line chart — monthly trend
monthly['year_month_dt'] = pd.to_datetime(monthly['year_month'])
plt.figure(figsize=(12, 4))
plt.plot(monthly['year_month_dt'], monthly['count'])
plt.title('Monthly 311 complaint volume')
plt.tight_layout()
plt.savefig("Line.jpg")
plt.show()

# 2. Bar chart — by borough
by_borough.sort_values('count').plot.barh(x='borough', y='count', figsize=(12,4))
plt.title('Total complaints by borough')
plt.savefig("Bar.jpg")
plt.show()

# 3. Heatmap — borough × year
plt.figure(figsize=(18, 5))
sns.heatmap(bor_year, annot=True, fmt='d', cmap='Blues')
plt.title('Complaints by borough and year')
plt.savefig("Heatmap.jpg")
plt.show()

# 4. Horizontal bar — top complaint types
top_complaints.sort_values().plot.barh(figsize=(18, 6))
plt.title('Top 15 complaint types')
plt.savefig("HBar.jpg")
plt.show()

print("Saved!")
