from bs4 import BeautifulSoup
import requests

# url = "https://biomatravel.org/testimonies-page"
# result = requests.get(url)

with open("sample-1.html", "r") as f:
    doc = BeautifulSoup(f, "html.parser")

words = doc.find_all(string = "Medium")

print(words)