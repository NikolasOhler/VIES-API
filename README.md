# Installation
`$ pip3 install vatvie` 

# Usage 
```python
from vatvie import VatRequest

# intialising vatvie class
vo = VatRequest('AT', '123212')
# sending soap request to VIEs library
response = vo.send_soap_request()

# Country Code
country_code = response['countryCode']

# VAT Number
vat_number = response['vatNumber']

# Request Date
request_date = response['requestDate']

# Validation Status - 'true' / 'false'
validation_status = response['valid']

# Company Name
company_name = response['name']

# Company Address
company_address = response['address']
```

# Error Validation 
VAT number and country name should follow predefined **regex patterns**:
- VAT Number = `'^[0-9A-Za-z\+\*\.]{2,12}$'`
- Country name = `'^[A-Z]{2}$'`


# License 
MIT License 