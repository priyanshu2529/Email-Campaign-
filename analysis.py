import pandas as pd

# STEP 1: Load CSV Files

email_df = pd.read_csv("email_table.csv")
opened_df = pd.read_csv("email_opened_table.csv")
clicked_df = pd.read_csv("link_clicked_table.csv")

# STEP 2: Merge 'opened' and 'clicked' flags

email_df["opened"] = email_df["email_id"].isin(opened_df["email_id"])
email_df["clicked"] = email_df["email_id"].isin(clicked_df["email_id"])

# STEP 3: Overview Stats
    
print("\n EMAIL TABLE with Opens & Clicks:\n")
print(email_df.head())

total = len(email_df)
opens = email_df["opened"].sum()
clicks = email_df["clicked"].sum()

print(f"\nTotal Emails Sent: {total}")
print(f"Total Opened: {opens} ({opens / total:.2%})")
print(f"Total Clicked: {clicks} ({clicks / total:.2%})")

# STEP 4: Group Performance by Email Type

performance = email_df.groupby(["email_text", "email_version"]).agg(
    emails_sent=("email_id", "count"),
    opens=("opened", "sum"),
    clicks=("clicked", "sum")
).reset_index()

# Calculate rates
performance["open_rate"] = performance["opens"] / performance["emails_sent"]
performance["click_rate"] = performance["clicks"] / performance["emails_sent"]

# Sort by click rate
performance = performance.sort_values("click_rate", ascending=False)

print("\n Performance by Email Type:\n")
print(performance)

# STEP 5: Identify Best Email Type

best = performance.iloc[0]
print("\n Best Performing Email Type:")
print(f"- Email Text: {best['email_text']}")
print(f"- Email Version: {best['email_version']}")
print(f"- Click Rate: {best['click_rate']:.2%}")

# STEP 6: Time and Day Analysis

# Group by hour and weekday
clicks_by_hour = email_df.groupby("hour")["clicked"].sum()
clicks_by_weekday = email_df.groupby("weekday")["clicked"].sum()

# Display click performance by time
print("\n Clicks by Hour:")
print(clicks_by_hour.sort_values(ascending=False))
print("\n Clicks by Weekday:")
print(clicks_by_weekday.sort_values(ascending=False))
