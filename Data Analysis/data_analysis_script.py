import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load datasets 
# Note: Update the file paths to the location of the datasets on your machine
energy_df = pd.read_csv("D:\Major Project\GenAI-Urban-Code\DataSet\synthetic_energy_usage.csv")
traffic_df = pd.read_csv("D:\Major Project\GenAI-Urban-Code\DataSet\synthetic_traffic_data.csv")
security_df = pd.read_csv("D:\Major Project\GenAI-Urban-Code\DataSet\synthetic_security_logs.csv")

# Set style for plots
sns.set_style("whitegrid")

# --- Energy Data Analysis ---
plt.figure(figsize=(10, 5))
sns.scatterplot(x=energy_df["Power_Consumption(kWh)"], y=energy_df["AI_Model_Efficiency_Score"], alpha=0.6)
plt.xlabel("Power Consumption (kWh)")
plt.ylabel("AI Model Efficiency Score")
plt.title("Energy Consumption vs. AI Efficiency")
plt.show()

# --- Traffic Data Analysis ---
plt.figure(figsize=(10, 5))
sns.boxplot(x=traffic_df["Time_of_Day"], y=traffic_df["Traffic_Density(cars/km²)"])
plt.xlabel("Time of Day")
plt.ylabel("Traffic Density (cars/km²)")
plt.title("Traffic Density Distribution by Time of Day")
plt.show()

# --- Security Data Analysis ---
plt.figure(figsize=(10, 5))
sns.histplot(security_df["Risk_Score"], bins=20, kde=True, color="red")
plt.xlabel("Security Risk Score")
plt.ylabel("Frequency")
plt.title("Distribution of Security Risk Scores")
plt.show()
