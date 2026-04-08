import pandas as pd 
import os
os.makedirs("data/processed",exist_ok=True) 
df=pd.read_csv("data/raw/cybersecurity_jobs_raw.csv")
keywords_title="security|cyber|soc|infosec|devsecops|penetration|threat|vulnerability"
keywords_skills = "security engineer|cloud security|network security|application security"
exclude_title = "marketing|sales|payroll|finance|social|recruiter|customer|account"
df_filtered=df[df["title"].str.contains(keywords_title,case=False,na=False)| 
               df["skills"].str.contains(keywords_skills,case=False,na=False)]
df_filtered = df_filtered[
    ~df_filtered["title"].str.contains(exclude_title, case=False, na=False)]
df_filtered.to_csv("data/processed/cybersecurity_jobs.csv",index=False)
print(f"filtered jobs:",len(df_filtered))
print(df_filtered[["title","company"]])