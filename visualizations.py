import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


df = pd.read_csv("email_data.csv")

# ----- Chart 1: Open Rate Pie Chart -----
labels = ['Opened', 'Not Opened']
sizes = [df['email_opened'].sum(), len(df) - df['email_opened'].sum()]
colors = ['#66b3ff', '#ff9999']

plt.figure(figsize=(6, 6))
plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)
plt.title('Email Open Rate')
plt.savefig('open_rate_pie_chart.png')
plt.close()

# ----- Chart 2: Click Rate by Email Type -----
clicks_by_type = df.groupby(['email_text', 'email_version'])['link_clicked'].mean().reset_index()
clicks_by_type['click_rate'] = clicks_by_type['link_clicked'] * 100

plt.figure(figsize=(8, 5))
sns.barplot(x='email_text', y='click_rate', hue='email_version', data=clicks_by_type)
plt.title('Click Rate by Email Type & Version')
plt.ylabel('Click Rate (%)')
plt.savefig('click_rate_by_email_type.png')
plt.close()