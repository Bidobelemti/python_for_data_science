import requests  # we import requests to make HTTP requests to download data from a URL
from pyodide.http import pyfetch  # we import pyfetch to fetch data from a URL

url = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DA0101EN-SkillsNetwork/labs/Data%20files/automobileEDA.csv','automobileEDA.csv'
response = requests.get(url)
path = "Data Analysis with Python/data/automobileEDA.csv"
if response.status_code == 200:
    with open(path, "wb") as f:
        f.write(response.content)

print("Download completed successfully!")