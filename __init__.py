
import requests as requests

_API_ENDPOINT = 'http://ec.europa.eu/taxation_customs/vies/checkVatService.wsdl'

headers = {"content-type" : "application/soap+xml"}
body = """
<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:urn="urn:ec.europa.eu:taxud:vies:services:checkVat:types">
   <soapenv:Header/>
   <soapenv:Body>
      <urn:checkVat>
         <urn:countryCode>SK</urn:countryCode>
         <urn:vatNumber>2020016449</urn:vatNumber>
      </urn:checkVat>
   </soapenv:Body>
</soapenv:Envelope>
"""

response = requests.post(_API_ENDPOINT, data = body, headers = headers)
print(response.text)