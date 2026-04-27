import requests

url = "https://larisadolina.com/wp-content/themes/dolina/assets/dist/js/app.js?ver=1644442923"

payload = {}
headers = {
  'sec-ch-ua-platform': '"Android"',
  'Referer': 'https://larisadolina.com/',
  'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Mobile Safari/537.36',
  'sec-ch-ua': '"Google Chrome";v="147", "Not.A/Brand";v="8", "Chromium";v="147"',
  'sec-ch-ua-mobile': '?1'
}

response = requests.request("GET", url, headers=headers, data=payload)

assert response.json()['data']

