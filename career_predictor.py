import os
import mysql.connector
import pandas as pd
from dotenv import load_dotenv
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import LabelEncoder
load_dotenv()
DB_CONFIG = {
    "host": os.environ.get("DB_HOST", "localhost"),
    "user": os.environ.get("DB_USER", "root"),
    "password": os.environ.get("DB_PASSWORD", ""),
    "database": os.environ.get("DB_NAME", "dummy"),
}
def main():
    conn = mysql.connector.connect(**DB_CONFIG)
    query = "SELECT age, passion, location, career FROM sample WHERE career IS NOT NULL"
    data = pd.read_sql_query(query, conn)
    conn.close()
    le_passion = LabelEncoder()
    le_location = LabelEncoder()
    le_career = LabelEncoder()
    data["passion"] = le_passion.fit_transform(data["passion"])
    data["location"] = le_location.fit_transform(data["location"])
    data["career"] = le_career.fit_transform(data["career"])
    X = data[["age", "passion", "location"]]
    y = data["career"]
    knn = KNeighborsClassifier(n_neighbors=3)
    knn.fit(X, y)
    new_age = 20
    new_passion = "Arts"
    new_location = "Dubai"
    try:
        new_passion_encoded = le_passion.transform([new_passion])[0]
        new_location_encoded = le_location.transform([new_location])[0]
        prediction = knn.predict([[new_age, new_passion_encoded, new_location_encoded]])
        predicted_career = le_career.inverse_transform(prediction)
        print("Suggested Career:", predicted_career[0])
    except ValueError as e:
        print("Error:", e)
        print("Make sure the test inputs exist in the training data.")
if __name__ == "__main__":
    main()
