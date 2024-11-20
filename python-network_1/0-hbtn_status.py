import urllib.request
'''Python script that fetches a URL'''
with urllib.request.urlopen('https://alu-intranet.hbtn.io/status') as response:
    html = response.read()
    print(html)
