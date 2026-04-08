'''
import requests 
from bs4 import BeautifulSoup 
import pandas as pd
import os
os.makedirs("data/raw", exist_ok=True)
os.makedirs("data/processed",exist_ok=True)
url="https://remoteok.com/remote-cybersecurity-jobs"
headers={"User-Agent": "Mozilla/5.0"}
response=requests.get(url,headers=headers)
soup=BeautifulSoup(response.text,"html.parser")
jobs=[]
for job in soup.find_all("tr",class_="job"):
    title_tag=job.find("h2")
    company_tag=job.find("h3")
    location_tag=job.find("div",class_="tag")
    if title_tag and company_tag:
        jobs.append({
            "title":title_tag.text.strip(),
            "company":company_tag.text.strip(),
            "location":location_tag.text.strip() if location_tag else "Remote",
            "skills": ",".join([tag.text.strip() for tag in tags_tag])
            })
raw_csv="data/raw/cybersecurity_jobs_raw.csv"
df=pd.DataFrame(jobs)
df.to_csv(raw_csv,index=False)
print(f"raw data saved :{raw_csv}")
'''
        

import requests
import pandas as pd
import os

os.makedirs("data/raw", exist_ok=True)

url = "https://remoteok.com/api"

response = requests.get(url)
data = response.json()

jobs = []

for job in data[1:]: 
   # if "Cyber" in job.get("position", " ") or "Security" in job.get("position", " "):
        jobs.append({
            "title": job.get("position"),
            "company": job.get("company"),
            "location": job.get("location"),
            "skills": ", ".join(job.get("tags", []))
        })
df = pd.DataFrame(jobs)
df.to_csv("data/raw/cybersecurity_jobs_raw.csv", index=False)
print("✅ Data collected:", len(df))  
