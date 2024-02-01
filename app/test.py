import requests

with open('app/urls.txt', 'r') as f:
    url_list = f.read().split('\n')
    for url in url_list:
        if not url.startswith('http'):
            continue
        try:
            res = requests.get(url.strip(), timeout=10)
        except:
            print("error opening", url)
            continue
        print(url, ":", res.status_code)