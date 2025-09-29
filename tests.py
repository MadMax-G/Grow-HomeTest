import requests

url = "https://sandbox.meshulam.co.il/api/light/server/1.0/createPaymentProcess"

payload = {'pageCode': 'e19e0b687744',
'userId': '52e95954cd5c1311',
'sum': '1',
'paymentNum': '1',
'description': 'ORDER123',
'pageField[fullName]': 'שם מלא',
'pageField[phone]': '0534738605',
'pageField[email]': 'debbie@meshulam.co.il'}
files=[

]
headers = {
  'Cookie': 'incap_ses_352_2943609=2RtBFRr0Fght4hkLkI7iBHyw12gAAAAAHPZ7LMtTq1ZAGvm5z2cPKw==; nlbi_2943609=4nG2Obn0HBRMwJACido8KgAAAACtHKSnXszkZ2PWlv3D4umW; visid_incap_2943609=/lopITtDRcCf/IpPzn1aM3uw12gAAAAAQUIPAAAAAACAmJe/KQ50K+naoCsHPyGh; AWSALB=viSdTTnBMMSxINsvVDLO0A7AxD3hdcb56Sa5SDW3b3uCyVo5WmaaK5RkSu29u9WR7bMB/AluX8GT68CzN+ZmJl/8Cm+/4JJUoPLThDizKh0wACyvT1SGatd+wT5/; AWSALBCORS=viSdTTnBMMSxINsvVDLO0A7AxD3hdcb56Sa5SDW3b3uCyVo5WmaaK5RkSu29u9WR7bMB/AluX8GT68CzN+ZmJl/8Cm+/4JJUoPLThDizKh0wACyvT1SGatd+wT5/; PHPSESSID=mm3ebikih108h5dujap54b9jjd'
}


def api_test():
    try:
        response = requests.post(url, headers=headers, data=payload, files=files)
        json_data = response.json()

        if response.status_code != 200:
           raise ValueError(f"Bad status code: {response.status_code}")

        if json_data["err"] != "" and json_data["err"] is not None:
            raise ValueError(f"{json_data["err"]["message"]}")

        new_url = json_data["data"]["url"]
        if new_url is None:
            raise ValueError("URL is missing")

        return response.status_code, new_url


    except KeyError as e:
        print(f"Missing key: {e}")

    except ValueError as e:
        print(e)

    except Exception as e:
        print(f"Unexpected error: {e}")



print(api_test())