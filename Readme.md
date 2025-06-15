# Email Campaign Optimization

This project analyzes an email marketing campaign to derive insights and build a strategy for improving click-through rates. It includes exploratory data analysis and discusses how a predictive model could help send optimized emails to users.

---

##  Files in the Repository

- `analysis.py`: Python script that performs data loading, merging, and analysis.
- `email_table.csv`: Original list of all users who were sent the emails.
- `email_opened_table.csv`: Subset of users who opened the emails.
- `link_clicked_table.csv`: Subset of users who clicked the link in the email.
- `README.md`: This file – documentation of the project.
- `train_model.py` : Python script that performs model training of the data.
- `visualizations.py` : Python script that plots the graph for Open and Click Rates.
- `open_rate_pie_chart.png` : Pie chart of Open rate.
- `email_data.csv` : Sample Data for the generation of charts.
- `click_rate_by_email_type.png` : Graph for click rate.

---

##  Key Questions & Insights

###  What percentage of users opened the email and clicked the link?

- **Total Emails Sent:** 100,000  
- **Emails Opened:** 56,154 →  **56.15% opened**
- **Links Clicked:** 11,898 → 🔗 **11.90% clicked**

---

###  Can we build a model to improve email targeting?

Yes (as mentioned below). Although emails were sent randomly in this campaign, we can build a **classification model** (e.g., Logistic Regression or Decision Tree) using:

- `email_version` (A or B)
- `email_text` (Short or Long)

These can help **predict the probability of a user clicking**. Once trained, the model can optimize which type of email to send, increasing overall effectiveness.

---

## Model Training

A Random Forest classifier was trained to predict whether a user opens an email based on the dataset. The current accuracy is 98%, but due to data imbalance, precision and recall for the minority class are low. Further improvements are in progress. This all happened due to only 2% data being true and others being false.

###  By how much could a model improve click-through rate?
Current (Random Assignment) CTR: ~11.90%

Simulated CTR with Trained Model: ~15.8%

Uplift: ✅ ~32.8% improvement

This means if the campaign used the model to predict the best email type for each user instead of sending them randomly, the overall click-through rate could increase by nearly one-third — a major impact in marketing performance.

###  Did we find any interesting patterns in the campaign?

Yes. Even with limited data, some patterns were observed:

- **Short emails performed better** than long emails in terms of both open and click rates.
- **Email version A** had a slight edge over B in engagement.
- The combination of **Short text + Version A** yielded the highest click-through rate.

---
### Visualizations

We added few charts and graphs for visualizations and better understanding.

##  Technologies Used

- Python 
- Pandas 
- VSCode Terminal
- Git & GitHub
