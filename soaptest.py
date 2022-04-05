import requests
import sys
import pprint
import json
import xmltodict

url='https://horizonclinical.hcl.com/siebel/app/eai/enu?SWEExtSource=WebService&SWEExtCmd=Execute&WSSOAP=1'
#url='https://clinical.c3i-inc.com/eai_enu/start.swe?SWEExtSource=WebService&SWEExtCmd=Execute&UserName=NOVOEPIDQCINTG &Password=Hor1z0n'
#headers = {'content-type': 'text/xml'}
headers = requests.utils.default_headers()
headers['User-Agent'] = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'
headers['content-type'] = 'text/xml'
body= """<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:con="http://www.c3i-inc.com/PfizerQCIntegration/Contact" xmlns:c3i="http://www.siebel.com/xml/C3i%20Pfizer%20Contact%20IO">
   <soapenv:Header>
     <UsernameToken xmlns="http://siebel.com/webservices">PFIZERQCINTG</UsernameToken>
     <PasswordText xmlns="http://siebel.com/webservices">Hor1z0n</PasswordText>
     <SessionType xmlns="http://siebel.com/webservices">None</SessionType>
   </soapenv:Header>
   <soapenv:Body>
      <con:PfizerQCContact>
         <Siebel_spcMessage>
            <c3i:ListOfC3iPfizerContactIo>
               <c3i:Contact>
                  <c3i:Id>1-CGYPVI</c3i:Id>
               </c3i:Contact>
            </c3i:ListOfC3iPfizerContactIo>
         </Siebel_spcMessage>
         <RequestType>Query Contact</RequestType>
      </con:PfizerQCContact>
   </soapenv:Body>
</soapenv:Envelope>"""
 
r=requests.post(url, data=body, headers=headers)
r.status_code

file = open("C:/contact.xml", "w")
file.write(r.text)
file.close()
f = open("C:/contact.xml", "r")
print(r.text)
"""con_dict = xmltodict.parse(r.text)
print(r.text)
fetch_con = ['ChallengeAnswer2','Note']
final_con_data =[]
con_request = ""

for val in fetch_con:
    try:
        data = (con_dict['SOAP-ENV:Envelope']['SOAP-ENV:Body']['rpc:PfizerQCContactResponse']['Siebel_spcMessage']['ListOfC3iPfizerContactIo']['Contact']['ListOfContactNote']['ContactNote'][val])
        final_con_data.append(data)
        #print(final_con_data)        
        con_request = dict(zip(fetch_con,final_con_data))
    except:
        print("no records")
   
#print(con_request['ChallengeAnswer2'])
#print(con_request['Note'])
if con_request != "":
    print("this user have Secret Question and Answer ")
    print("Secret Question:",con_request['Note'])
    print("Answer:",con_request['ChallengeAnswer2'])
else:
    print("this user dosn't have proper secret question and answer")"""





