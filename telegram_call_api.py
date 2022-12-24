import requests

try:

    url="https://api.callmebot.com/start.php?user=@Tomas201513&text=There+is+a+link+from+muferihat"
    requests.get(url)
    print("done")
except:
    print("fail")

