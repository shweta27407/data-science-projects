# 📡 Collecting the Data with an API

In this video, we will review **Collecting the Data with an API**.

In this capstone assignment, we will be working with **SpaceX launch data** gathered from an **API**, specifically the **SpaceX REST API**. This API provides data about launches, including:

- Information about the **rocket used**
- **Payload delivered**
- **Launch specifications**
- **Landing specifications**
- **Landing outcomes**

Our goal is to use this data to **predict whether SpaceX will attempt to land a rocket or not**.

---

## 🔗 API Endpoint

The **SpaceX REST API** endpoint starts with:

```
https://api.spacexdata.com/v4/
```

Some useful endpoints include:

- `/capsules`
- `/cores`
- `/launches/past` → **This is the endpoint we will use**

We will use this URL to **target past launch data**.

---

## 🧪 Making an API Request

We will perform a **GET request** using the `requests` library in Python to obtain the launch data.

```python
import requests
response = requests.get("https://api.spacexdata.com/v4/launches/past")
data = response.json()
```

This result is in the form of **JSON**, specifically a **list of JSON objects**—each representing a single launch.

To convert this structured JSON into a flat table, we can use:

```python
from pandas import json_normalize
df = json_normalize(data)
```

This function **normalizes** nested JSON into a usable tabular format (DataFrame).

---

## 🛰️ Web Scraping Additional Data

Another valuable source of **Falcon 9 launch data** is **Wikipedia**.

We will use the **BeautifulSoup** package to:

1. Scrape **HTML tables** from Wikipedia
2. **Parse** the data
3. Convert it into a **Pandas DataFrame**

This helps us **clean and structure raw data** for analysis.

---

## 🧹 Data Wrangling Objectives

You’ll tackle tasks such as:

- **Using the API** to pull data
- **Sampling data** (e.g., removing Falcon 1 launches)
- **Dealing with NULL values**

### Example: Dealing with Missing Data

- In some columns (e.g., `rocket`), we get an **ID number**, not readable data
- We use **additional API endpoints** to extract data for:
  - **Booster**
  - **Launchpad**
  - **Payload**
  - **Core**

These will be stored in lists to build a complete dataset.

---

## ⚠️ Cleaning the Dataset

### Filtering Falcon 9 Only

The launch data includes **Falcon 1** entries. You will:

- Filter or sample the dataset
- Remove Falcon 1 records

### Handling NULL Values

- Some columns (like `PayloadMass`) have missing values
- You will calculate the **mean** of `PayloadMass` and **replace nulls**

```python
mean_payload_mass = df["PayloadMass"].mean()
df["PayloadMass"].fillna(mean_payload_mass, inplace=True)
```

- **LandingPad** will be left with nulls, to be handled later via **one-hot encoding**

---

> 🎯 The final goal is to transform raw launch data into a **clean dataset** to support machine learning modeling and analysis.