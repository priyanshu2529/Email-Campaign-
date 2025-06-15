import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
email_df = pd.read_csv("email_table.csv")
opened_df = pd.read_csv("email_opened_table.csv")
clicked_df = pd.read_csv("link_clicked_table.csv")

email_df["opened"] = email_df["email_id"].isin(opened_df["email_id"])
email_df["clicked"] = email_df["email_id"].isin(clicked_df["email_id"])

features = email_df[["email_text", "email_version", "hour", "weekday"]]
labels = email_df["clicked"]

features_encoded = pd.get_dummies(features, columns=["email_text", "email_version", "weekday"])

X_train, X_test, y_train, y_test = train_test_split(features_encoded, labels, test_size=0.2, random_state=42)

# Training Random Forest model
model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)

# Prediction of our model.
y_pred = model.predict(X_test)

print("\n Model Performance:\n")
print(classification_report(y_test, y_pred))
