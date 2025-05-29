#  ML Intern Case Study – Email Campaign Analysis

This project analyzes the effectiveness of different email campaign strategies by examining open and click-through rates across versions, timings, and weekdays. It was developed as part of a machine learning internship case study.

---

##  Objective

To evaluate the performance of various email versions based on:
- Open rates
- Click-through rates (CTR)
- Time of day and day of week trends

---

##  Files Included

| File Name               | Description                                      |
|------------------------|--------------------------------------------------|
| `analysis.py`          | Main Python script for loading and analyzing the data |
| `email_table.csv`      | Contains details of all emails sent              |
| `email_opened_table.csv` | Email IDs of opened emails                     |
| `link_clicked_table.csv` | Email IDs of clicked links                     |
| `README.md`            | This documentation                              |

---

##  Analysis Performed

-  Merged email, opened, and clicked datasets
-  Calculated total emails sent, open counts, click counts
-  Grouped performance by email text and version
-  Identified best-performing email variation based on click rate
-  Analyzed hourly click trends
-  Analyzed weekday click trends

---

##  Key Insights

- **Best Performing Email**:
  - Text: `short email`
  - Version: `Personalised version`
  - Click Rate: `3.12%`

- **Best Time to Send Emails**: Between **9 AM to 11 AM**
- **Best Day to Send Emails**: **Wednesday**, followed by **Tuesday** and **Thursday**

---

##  Technologies Used

- Python 
- Pandas 
- Jupyter/VSCode Terminal
- Git & GitHub

---

