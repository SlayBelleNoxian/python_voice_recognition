import requests

s = requests.Session()

url = "https://www.thinkdigital.pt/tools/echo.php?data="
sentence = "testar"
myUrl = url+sentence;

r = s.get(myUrl)

print(r.text)