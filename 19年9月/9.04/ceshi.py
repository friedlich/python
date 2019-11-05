import json

import requests

cookies = {
            'SUB': '_2A25wa-vWDeRhGeBM71IR9y3FzDyIHXVTl_WerDV6PUJbkdAKLXDFkW1NRMmDYj8lM3iq9VPFBqbDWsYDWRVMuYmK',
            'SUHB': '0jBITY2lOBDsuu',
            }
print(type(cookies))

cookies = json.dumps(cookies)
print(type(cookies))

cookies = json.loads(cookies)
print(type(cookies))

cookies = requests.utils.cookiejar_from_dict(cookies)
print(type(cookies))