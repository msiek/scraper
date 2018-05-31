import requests
from scrapy.http import TextResponse

r = requests.get('https://www.linkedin.com/jobs/search?keywords=Permit+Expeditor&locationId=OTHERS%2Eworldwide&f_L=us%3A0&locationType=Y&orig=FCTD&trk=jobs_jserp_facet_geo_region')

response = TextResponse(r.url, body=r.text, encoding='utf-8')

print(response)