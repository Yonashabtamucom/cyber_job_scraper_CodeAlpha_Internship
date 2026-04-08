import pandas as pd 
import matplotlib.pyplot as plt
import os
processed_csv="data/processed/cybersecurity_jobs.csv"
df=pd.read_csv(processed_csv)
top_companies=df["company"].value_counts().head(10)
print("Top 10 hiring companies:\n",top_companies)
skills_series=df["skills"].str.split(",").explode()
top_skills=skills_series.value_counts().head(10)
print("\n Top 10 requested companies:\n",top_companies)
os.makedirs("reports/figures",exist_ok=True)
top_companies.plot(kind="bar",figsize=(10,6),title="top 10 hiring companies ")
plt.savefig("reports/figures/top_companies.png")
plt.close()
top_skills.plot(kind="bar",figsize=(10,6),title="top 10 requested skills")
plt.savefig("reports/figures/top_skills.png")
plt.close()
print("Analysis plots saved in reports/figures/")
