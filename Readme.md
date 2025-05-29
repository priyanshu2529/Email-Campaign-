# Email Campaign Optimization

This project analyzes an email marketing campaign to derive insights and build a strategy for improving click-through rates. It includes exploratory data analysis and discusses how a predictive model could help send optimized emails to users.

---

##  Files in the Repository

- `analysis.py`: Python script that performs data loading, merging, and analysis.
- `email_table.csv`: Original list of all users who were sent the emails.
- `email_opened_table.csv`: Subset of users who opened the emails.
- `link_clicked_table.csv`: Subset of users who clicked the link in the email.
- `README.md`: This file – documentation of the project.

---

##  Key Questions & Insights

###  What percentage of users opened the email and clicked the link?

- **Total Emails Sent:** 100,000  
- **Emails Opened:** 56,154 →  **56.15% opened**
- **Links Clicked:** 11,898 → 🔗 **11.90% clicked**

---

###  Can we build a model to improve email targeting?

Yes. Although emails were sent randomly in this campaign, we can build a **classification model** (e.g., Logistic Regression or Decision Tree) using:

- `email_version` (A or B)
- `email_text` (Short or Long)

These can help **predict the probability of a user clicking**. Once trained, the model can optimize which type of email to send, increasing overall effectiveness.

---

###  By how much could a model improve click-through rate?

To estimate this:

1. Train a predictive model on the existing dataset.
2. Use the model to simulate a campaign where each user gets the most likely-to-be-clicked email.
3. Compare the simulated CTR to the current random assignment CTR.

> Example:  
> Current CTR = 11.90%  
> Simulated CTR = 16.00%  
> Uplift = **34.45% improvement**

---

###  Did we find any interesting patterns in the campaign?

Yes. Even with limited data, some patterns were observed:

- **Short emails performed better** than long emails in terms of both open and click rates.
- **Email version A** had a slight edge over B in engagement.
- The combination of **Short text + Version A** yielded the highest click-through rate.

---

##  Technologies Used

- Python 
- Pandas 
- Jupyter/VSCode Terminal
- Git & GitHub

---
