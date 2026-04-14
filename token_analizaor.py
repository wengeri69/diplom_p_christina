import requests
import json

url = "https://bynex.io/investment/api/graphql"

payload = json.dumps({
  "operationName": "ico",
  "variables": {
    "payload": {
      "sorts": [
        {
          "columnName": "status",
          "direction": "asc"
        },
        {
          "columnName": "createdDate",
          "direction": "desc"
        }
      ],
      "filters": [],
      "paginate": {
        "skip": 0,
        "take": 10
      }
    }
  },
  "query": "query ico($payload: IcoGetDTO!) {\n  ico(payload: $payload) {\n    items {\n      id\n      isEarlyRedemption\n      lastDateToken\n      endDateICO\n      nameToken\n      rate\n      status\n      tokenCurrentPrice\n      tokenVolumeAvailable\n      tokenVolumeIssueAll\n      partnership\n      provision\n      organization {\n        ...Organization\n        __typename\n      }\n      currency {\n        ...Currency\n        __typename\n      }\n      documentLogo {\n        ...DocumentIcoList\n        __typename\n      }\n      __typename\n    }\n    meta {\n      skip\n      take\n      total\n      lastDateTokenMax\n      lastDateTokenMin\n      rateMax\n      rateMin\n      tokenCurrentPriceMax\n      tokenCurrentPriceMin\n      __typename\n    }\n    __typename\n  }\n}\n\nfragment Organization on OrganizationModel {\n  id\n  name\n  __typename\n}\n\nfragment Currency on CurrencyModel {\n  id\n  letterCode\n  decimals\n  __typename\n}\n\nfragment DocumentIcoList on DocumentModel {\n  id\n  hashname\n  extension\n  __typename\n}\n"
})
headers = {
  'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
  'Connection': 'keep-alive',
  'Origin': 'https://bynex.io',
  'Referer': 'https://bynex.io/',
  'Sec-Fetch-Dest': 'empty',
  'Sec-Fetch-Mode': 'cors',
  'Sec-Fetch-Site': 'same-origin',
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Safari/537.36',
  'accept': '*/*',
  'content-type': 'application/json',
  'sec-ch-ua': '"Chromium";v="146", "Not-A.Brand";v="24", "Google Chrome";v="146"',
  'sec-ch-ua-mobile': '?0',
  'sec-ch-ua-platform': '"Windows"'
}

response = requests.request("POST", url, headers=headers, data=payload)
response_json = response.json()
items = response_json["data"]["ico"]["items"]

filtered_names = [
    item["organization"]["name"]
    for item in items
    if 5 <= item["rate"] <= 15 and 5 <= item["tokenCurrentPrice"] <= 100
]

print("Подходящие компании:")
for name in filtered_names:
    print(f"- {name}")
