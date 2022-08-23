import requests
import xml.dom.minidom
# Still import the JSON library just to handle our request to the APIC for login
import json
# Disable certificate warnings
requests.packages.urllib3.disable_warnings()
encoded_body = json.dumps({
            "aaaUser": {
                "attributes": {
                    "name": "admin",
                    "pwd": "!v3G@!4@Y"
                 }
            }
})

resp = requests.post("https://sandboxapicdc.cisco.com/api/aaaLogin.json", data=encoded_body, verify=False)
header = {"Cookie": "APIC-cookie=" +  resp.cookies["APIC-cookie"]}
tenants = requests.get("https://sandboxapicdc.cisco.com/api/node/class/fvTenant.xml?rsp-subtree-include=health,faults", headers=header, verify=False)

dom = xml.dom.minidom.parseString(tenants.text)
xml = dom.toprettyxml()
print(xml)
