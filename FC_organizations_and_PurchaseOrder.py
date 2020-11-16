import json
import uuid
import xlrd
import os
import xlwt
import xlsxwriter
import openpyxl
import os.path
import datetime
from datetime import datetime
import requests
import csv
import io

class purchaseOrder():
    def __init__(self,poNumber,vendor,orderType,notas,Order_status):
        self.poNumber=poNumber
        self.vendor=vendor
        self.orderType=orderType
        #self.notes=notas
        self.workflowStatus=Order_status
        #self.tags="EBSCOTEST"


    


######==========================================================        

#    def printPurchaseOrderOngoingEbscoNet(self, Order_format, currency, renewalDate, purchase_method, eprice, id_loc, title, subscrition_from, subscription_to, package, publisher, fund, acq_method, expectedActivationDate,materialType,polId,secuence,fileName,Acqbill,manualpo,ispkg,receiptstatus,polinedescription,instructionsVendor,uuidorder,notas,instanceid):
#        Ordarchivo=open(fileName+"_orders.json", 'a')
#        if (instructionsVendor):
#            order= {
#                "id":uuidorder,
#                "approved": True,
#                "billTo": Acqbill,
#                "manualPo": False,
#                "notes": notas,
#                "poNumber": self.poNumber,
#                "orderType": "Ongoing",
#                "reEncumber": False,
#                "ongoing": {"interval": 365,"isSubscription": True,"renewalDate": renewalDate},
#                "shipTo": Acqbill,
#                "totalEstimatedPrice": eprice,
#                "totalItems": 1,
#                "vendor": self.vendor,
#                "workflowStatus": "Pending",
#                "compositePoLines": [
#                    {
#                        "id": str(polId),
#                        "checkinItems": False,
#                        "acquisitionMethod": "Purchase At Vendor System",
#                        "alerts": [],
#                        "claims": [],
#                        "collection": False,
#                        "contributors": [],
#                        "cost": {"listUnitPriceElectronic": eprice,"currency": currency,"discountType": "percentage","quantityElectronic": 1,"poLineEstimatedPrice": eprice},
#                        "details": {"productIds": [],"subscriptionInterval": 0},
#                        "eresource": {"activated": True,"activationDue": -623,"createInventory": "None","trial": False,"expectedActivation": expectedActivationDate,"userLimit":"",      "accessProvider": self.vendor,"materialType": materialType},
#                        "fundDistribution": [{"code": fund[1],"fundId": fund[0],"distributionType": "percentage","value": 100.0}],
#                        "isPackage": False,
#                        #"locations": [{"locationId": id_loc,"quantity": 1,"quantityElectronic": 1,"quantityPhysical": 0}],
#                        "orderFormat": "Electronic Resource",
#                        "paymentStatus": "Payment Not Required",
#                        "physical": {"createInventory": "None","materialSupplier": self.vendor,"volumes": []},
#                        "poLineNumber": self.poNumber+"-"+str(secuence),
#                        "receiptStatus": "Receipt Not Required",
#                        "reportingCodes": [],
#                        "rush": False,
#                        "source": "User",
#                        "titleOrPackage": title,
#                        #"vendorDetail": {"instructions": instructionsVendor,"refNumber": "refnumeber","refNumberType": "Internal vendor number","vendorAccount": "accountnumber"},
#                        "vendorDetail": {"instructions": instructionsVendor,"refNumber": self.poNumber,"refNumberType": "Internal vendor number","vendorAccount": ""},
#                     }],
#                "acqUnitIds": [],
#              }
#        else:
#            order= {
#                "id":uuidorder,
#                "approved": True,
#                "billTo": Acqbill,
#                "manualPo": False,
#                "notes": notas,
#                "poNumber": self.poNumber,
#                "orderType": "Ongoing",
#                "reEncumber": False,
#                "ongoing": {"interval": 365,"isSubscription": True,"renewalDate": renewalDate},
#                "shipTo": Acqbill,
#                "totalEstimatedPrice": 0.0,
#                "totalItems": 1,
#                "vendor": self.vendor,
#                "workflowStatus": "Pending",
#                "compositePoLines": [
#                    {
#                        "id": str(polId),
#                        "checkinItems": False,
#                        "acquisitionMethod": "Purchase At Vendor System",
#                        "alerts": [],
#                        "claims": [],
#                        "collection": False,
#                        "contributors": [],
#                        "cost": {"listUnitPriceElectronic": 0.0,"currency": "USD","discountType": "percentage","quantityElectronic": 1,"poLineEstimatedPrice": 0.0},
#                        "details": {"productIds": [],"subscriptionInterval": 0},
#                        "eresource": {"activated": True,"activationDue": -623,"createInventory": "None","trial": False,"expectedActivation": expectedActivationDate,"userLimit":"",      "accessProvider": self.vendor,"materialType": materialType},
#                        "fundDistribution": [{"code": fund[1],"fundId": fund[0],"distributionType": "percentage","value": 100.0}],
#                        "isPackage": False,
#                        #"locations": [{"locationId": id_loc,"quantity": 1,"quantityElectronic": 1,"quantityPhysical": 0}],
#                        "orderFormat": "Electronic Resource",
#                        "paymentStatus": "Payment Not Required",
#                        "physical": {"createInventory": "None","materialSupplier": self.vendor,"volumes": []},
#                        "poLineNumber": self.poNumber+"-"+str(secuence),
#                        "receiptStatus": "Receipt Not Required",
#                        "reportingCodes": [],
#                        "rush": False,
#                        "source": "User",
#                        "titleOrPackage": title,
#                        #"vendorDetail": {"instructions": instructionsVendor,"refNumber": "refnumeber","refNumberType": "Internal vendor number","vendorAccount": "accountnumber"},
#                     }],
#                "acqUnitIds": [],
#              }

#        #json_ord = json.dumps(order,indent=2)
#        json_ord = json.dumps(order)
#        print('Datos en formato JSON', json_ord)
#        Ordarchivo.write(json_ord+"\n")




def floatHourToTime(fh):
    h, r = divmod(fh, 1)
    m, r = divmod(r*60, 1)
    return (
        int(h),
        int(m),
        int(r*60),
    )

def date_stamp(ilsdate):
    dt=""
    if (ilsdate.find("/")>=0):
        dt=ilsdate
        dia=dt[0:2]
        mes=dt[3:5]
        ano=dt[6:10]
        dt=ano+"-"+mes+"-"+dia+"T"+"00:00:00+0000"
    elif (ilsdate.find(".")>=0):
        dt = datetime.fromordinal(datetime(1900, 1, 1).toordinal() + int(ilsdate) - 2)
        hour, minute, second = floatHourToTime(ilsdate % 1)
        dt = str(dt.replace(hour=hour, minute=minute,second=second))+".000+0000" #Approbal by
        #2019-12-12T10:11:16.449+0000
        dt=dt.replace(" ","T")
        renewalDate=dt
    elif (ilsdate=="0"):
        dt="0000-00-00T00:00:00+0000"
    else:
        dt=ilsdate
        dia=dt[7:8]
        mes=dt[5:6]
        ano=dt[6:4]
        dt=ano+"-"+mes+"-"+dia+"T"+"00:00:00+0000"

    return dt


def exitfile(arch):    
    if os.path.isfile(arch):
        print ("File exist")
        os.remove(arch)
    else:
        print ("File not exist")

def price(cost):
    if cost:
        return cost
    else:
        cost=0.01
        return cost

def search(fileB,code_search):
    idlicense=""
    foundc=False
    with open(fileB,'r',encoding = 'utf-8') as h:
        for lineh in h:
            if (lineh.find(code_search) != -1):
                #print(lineh)
                foundc=True
                if (foundc):                    
                    idlicense=lineh[8:44]
                    break
    if (foundc):
        return idlicense
    else:
        idlicense="No Vendor"
        return idlicense

def is_empty(data_structure):
    if data_structure:
        print("No está vacía")
        return False
    else:
        print("Está vacía")
        return True

def Aleph_Order_Type(AlephOrderType):
    if (AlephOrderType=="S"):
        ot= "Ongoing"
    elif (AlephOrderType=="O"):
        ot="Ongoing"
    else:
         ot="One-Time"
    return ot

def Aleph_workFlowStatus(AlephWorkFlowStatus):
    if (AlephWorkFlowStatus=="LC"):
        wfs= "Pending"
    elif (AlephWorkFlowStatus=="VC"):
        wfs="Pending"
    else:
         wfs="Open"
    return wfs


def Aleph_paymentStatus(AlephPayStatus):
    if (AlephPayStatus=="P"):
        aps= "Pending"
    elif (AlephPayStatus=="C"):
        aps="Pending"
    return aps

def notes_tupla(noteTosave):
    notes=[]
    if noteTosave[3]:
       notes= notes.append("Order Number 1: "+noteTosave[3].strip()+"\n")
    elif noteTosave[4]:
           notes= notes.append("Order Number 2: "+noteTosave[4].strip()+"\n")
    elif noteTosave[5]:
       notes= notes.append("Order Group: "+noteTosave[5].strip())
    elif noteTosave[17]:
       notes= notes.append("Order Group: "+noteTosave[17].strip())
    return notes

def instructionsVendor(l):
    ivendor=""
    if (l):
        ivendor=l
    return ivendor
                       
def get_OrgId(orgname):
        dic={}
        #pathPattern="/organizations-storage/organizations" #?limit=9999&query=code="
        pathPattern="/organizations/organizations" #?limit=9999&query=code="
        okapi_url="https://okapi-fivecolleges-sandbox.folio.ebsco.com"
        okapi_token="eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJlYnNjb01pZ3JhdGlvbiIsInVzZXJfaWQiOiIyYmQ3NTBiOS0xMzYyLTQ4MDctYmQ3My0yYmU5ZDhkNjM0MzYiLCJpYXQiOjE2MDI1NTA2MDksInRlbmFudCI6ImZzMDAwMDEwMDYifQ.jnT-wDKlXAUbAKr9L5uzESApkJuGreYKEb1RcZH2URc"
        okapi_tenant="fs00001006"
        okapi_headers = {"x-okapi-token": okapi_token,"x-okapi-tenant": okapi_tenant,"content-type": "application/json"}
        length="1"
        start="1"
        element="organizations"
        query=f"query=code=="
        #/organizations-storage/organizations?query=code==UMPROQ
        paging_q = f"?{query}"+orgname
        path = pathPattern+paging_q
        #data=json.dumps(payload)
        url = okapi_url + path
        req = requests.get(url, headers=okapi_headers)
        idorg=[]
        if req.status_code != 201:
            json_str = json.loads(req.text)
            total_recs = int(json_str["totalRecords"])
            if (total_recs!=0):
                rec=json_str[element]
                #print(rec)
                l=rec[0]
                if 'id' in l:
                    idorg.append(l['id'])
                    #idorg.append(l['name'])
        if len(idorg)==0:
            return "00000-000000-000000-00000"
        else:
            return idorg
#END
def get_funId(fund_name):
        dic={}
        #pathPattern="/organizations-storage/organizations" #?limit=9999&query=code="
        pathPattern="/finance/funds" #?limit=9999&query=code="
        okapi_url="https://okapi-ua.folio.ebsco.com"
        okapi_token="eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJmb2xpbyIsInVzZXJfaWQiOiJkOTE2ZTg4My1mOGYxLTQxODgtYmMxZC1mMGRjZTE1MTFiNTAiLCJpYXQiOjE1OTg1NDY2MzIsInRlbmFudCI6ImZzMDAwMDEwMDUifQ.aptR-bH8IbePZCdoGd3lomRI4-cI2jbK4AMmyAU2AOM"
        okapi_tenant="fs00001005"
        okapi_headers = {"x-okapi-token": okapi_token,"x-okapi-tenant": okapi_tenant,"content-type": "application/json"}
        length="1"
        start="1"
        element="funds"
        query=f"query=name=="
        #/finance/funds?query=name==UMPROQ
        search='"'+fund_name+'"'
        #paging_q = f"?{query}"+search
        paging_q = f"?{query}"+search
        path = pathPattern+paging_q
        #data=json.dumps(payload)
        url = okapi_url + path
        req = requests.get(url, headers=okapi_headers)
        idfund=[]
        if req.status_code != 201:
            json_str = json.loads(req.text)
            total_recs = int(json_str["totalRecords"])
            if (total_recs!=0):
                rec=json_str[element]
                #print(rec)
                l=rec[0]
                if 'id' in l:
                    idfund.append(l['id'])
                    idfund.append(l['name'])
        return idfund
#END

def get_title(title_hrid):
        dic={}
        #pathPattern="/instance-storage/instances" #?limit=9999&query=code="
        #https://okapi-ua.folio.ebsco.com/instance-storage/instances?query=hrid=="264227"
        pathPattern="/instance-storage/instances" #?limit=9999&query=code="
        okapi_url="https://okapi-fivecolleges-sandbox.folio.ebsco.com"
        okapi_token="eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJlYnNjb01pZ3JhdGlvbiIsInVzZXJfaWQiOiIyYmQ3NTBiOS0xMzYyLTQ4MDctYmQ3My0yYmU5ZDhkNjM0MzYiLCJpYXQiOjE2MDMxOTY5MTksInRlbmFudCI6ImZzMDAwMDEwMDYifQ.44-JmfKuHg--4f1X56VxzbY0vmgiA0eZzxhWqXTAZC0"
        okapi_tenant="fs00001006"
        okapi_headers = {"x-okapi-token": okapi_token,"x-okapi-tenant": okapi_tenant,"content-type": "application/json"}
        length="1"
        start="1"
        element="instances"
        query=f"query=hrid=="
        #/finance/funds?query=name==UMPROQ
        search='"'+title_hrid+'"'
        #paging_q = f"?{query}"+search
        paging_q = f"?{query}"+search
        path = pathPattern+paging_q
        #data=json.dumps(payload)
        url = okapi_url + path
        req = requests.get(url, headers=okapi_headers)
        idhrid=[]
        if req.status_code != 201:
            json_str = json.loads(req.text)
            total_recs = int(json_str["totalRecords"])
            if (total_recs!=0):
                rec=json_str[element]
                #print(rec)
                l=rec[0]
                if 'id' in l:
                    idhrid.append(l['id'])
                    idhrid.append(l['title'])            
        return idhrid
#END

def get_locId(orgname):

    if orgname== "UM":
        idorg="e87c933e-b136-4d07-85c3-37f49e583fa9"
    elif orgname== "SC":
        idorg="6382e0b7-debb-4067-9ecd-e4dcd6253ee2"
    elif orgname=="MH":
        idorg="100532ff-f972-47f4-ab67-5bf44c4d648e"
    elif orgname=="HC":
       idorg="8e76446a-fe15-46af-aabf-3939c249307f"
    elif orgname== "HC":
       idorg="7c25ce2b-db09-4e35-99df-fa6a4c07a70d"
    return idorg

#        dic={}
#        #pathPattern="/organizations-storage/organizations" #?limit=9999&query=code="
#        pathPattern="/locations" #?limit=9999&query=code="
#        okapi_url="https://okapi-ua.folio.ebsco.com"
#        okapi_token="eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJmb2xpbyIsInVzZXJfaWQiOiJkOTE2ZTg4My1mOGYxLTQxODgtYmMxZC1mMGRjZTE1MTFiNTAiLCJpYXQiOjE1OTg1NDY2MzIsInRlbmFudCI6ImZzMDAwMDEwMDUifQ.aptR-bH8IbePZCdoGd3lomRI4-cI2jbK4AMmyAU2AOM"
#        okapi_tenant="fs00001005"
#        okapi_headers = {"x-okapi-token": okapi_token,"x-okapi-tenant": okapi_tenant,"content-type": "application/json"}
#        length="1"
#        start="1"
#        element="locations"
#        query=f"query=name=="
#        #/organizations-storage/organizations?query=code==UMPROQ
#        paging_q = f"?{query}"+orgname
#        path = pathPattern+paging_q
#        #data=json.dumps(payload)
#        url = okapi_url + path
#        req = requests.get(url, headers=okapi_headers)
#        idorg=[]
#        if req.status_code != 201:
#            json_str = json.loads(req.text)
#            total_recs = int(json_str["totalRecords"])
#            if (total_recs!=0):
#                rec=json_str[element]
#                #print(rec)
#                l=rec[0]
#                if 'id' in l:
#                    idorg.append(l['id'])
#                    idorg.append(l['name'])
#        return idorg
##END

def purchase_method(mc):
    PurchaseMethod=""
    if mc=="P":
        PurchaseMethod="Purchase"
    elif mc=="G":
        PurchaseMethod="Gift"
    elif mc=="AF":
        PurchaseMethod="Purchase"
    elif mc=="PF":
        PurchaseMethod="Purchase"
    elif mc=="A":
        PurchaseMethod="Approval"
    elif mc=="DA":
        PurchaseMethod="Purchase"
    elif mc=="D":
        PurchaseMethod="Purchase"
    elif mc=="PX":
        PurchaseMethod="Gift"
    elif mc=="NL":
        PurchaseMethod="Purchase"
    elif mc=="E":
        PurchaseMethod="Exchange"
    elif mc=="EP":
        PurchaseMethod="Exchange"
    elif mc=="M":
        PurchaseMethod="Purchase"
    elif mc=="MT":
        PurchaseMethod="Purchase"
    elif mc=="CC":
        PurchaseMethod="Purchase"
    
    return PurchaseMethod


def acquisition_unit(aqunit):
    if aqunit=="Orders/amherst_orderst.dsv":
       adqui="155e37bb-c5ae-4179-8a24-a6b625ff96f7"
    elif aqunit=="HC":
        adqui="c9607f4b-2c99-4a41-941a-34b8624a80e1"
    elif aqunit=="MH":
        adqui="c9607f4b-2c99-4a41-941a-34b8624a80e1"
    elif aqunit=="SC":
        adqui="32a2bcc6-0c65-437d-a7d7-17bf8785ec4d"
    elif aqunit=="UM":
        adqui="7e8d460a-93dc-40b4-a1b7-f4a85a0a0dba"

    return adqui 

def get_MaterialType(alepamh):
    idorg=[]
    search=materialType(alepamh)
    #pathPattern="/organizations-storage/organizations" #?limit=9999&query=code="
    pathPattern="/material-types" #?limit=9999&query=code="
    okapi_url="https://okapi-fivecolleges-sandbox.folio.ebsco.com"
    okapi_token="eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJlYnNjb01pZ3JhdGlvbiIsInVzZXJfaWQiOiIyYmQ3NTBiOS0xMzYyLTQ4MDctYmQ3My0yYmU5ZDhkNjM0MzYiLCJpYXQiOjE2MDI1NTA2MDksInRlbmFudCI6ImZzMDAwMDEwMDYifQ.jnT-wDKlXAUbAKr9L5uzESApkJuGreYKEb1RcZH2URc"
    okapi_tenant="fs00001006"
    okapi_headers = {"x-okapi-token": okapi_token,"x-okapi-tenant": okapi_tenant,"content-type": "application/json"}
    length="1"
    start="1"
    element="mtypes"
    query=f"query=name=="
    #/organizations-storage/organizations?query=code==UMPROQ
    paging_q = f"?{query}"+search
    path = pathPattern+paging_q
    #data=json.dumps(payload)
    url = okapi_url + path
    req = requests.get(url, headers=okapi_headers)
    idorg=[]
    if req.status_code != 201:
        json_str = json.loads(req.text)
        total_recs = int(json_str["totalRecords"])
        if (total_recs!=0):
            rec=json_str[element]
            #print(rec)
            l=rec[0]
            if 'id' in l:
               idorg.append(l['id'])
               #idorg.append(l['name'])
        if len(idorg)==0:
            idorg=""
    return idorg
#END
#One-Time
def order_format(of):
    orfor=""
    if of=="2D":
        orfor="Physical Resource"
    elif of=="AC":
        orfor="Physical Resource"
    elif of=="AR":
        orfor="Physical Resource"
    elif of=="CD":
        orfor="Physical Resource"
    elif of=="CN":
        orfor="Physical Resource"
    elif of=="DB":
        orfor="Physical Resource"
    elif of=="DV":
        orfor="Physical Resource"
    elif of=="EB":
        orfor="Electronic Resource"
    elif of=="EJ":
        orfor="Electronic Resource"
    elif of=="EP":
        orfor="Electronic Resource"
    elif of=="FL":
        orfor="Physical Resource"
    elif of=="GP":
        orfor="Physical Resource"
    elif of=="IM":
        orfor="Physical Resource"
    elif of=="IS":
        orfor="Electronic Resource"
    elif of=="JP":
        orfor="Electronic Resource"
    elif of=="LP":
        orfor="Physical Resource"
    elif of=="M":
        orfor="Physical Resource"
    elif of=="MC":
        orfor="Physical Resource"
    elif of=="MF":
        orfor="Physical Resource"
    elif of=="MP":
        orfor="Physical Resource"
    elif of=="NE":
        orfor="Physical Resource"
    elif of=="PJ":
        orfor="Physical Resource"
    elif of=="SC":
        orfor="Physical Resource"
    elif of=="SE":
        orfor="Physical Resource"
    elif of=="ST":
        orfor="Electronic Resource"
    elif of=="T":
        orfor="Physical Resource"
    elif of=="TH":
        orfor="Physical Resource"
    return orfor

def materialType(of):
    orfor=""
    if of=="2D":
        orfor="Image"
    elif of=="AC":
        orfor="Audiocassette"
    elif of=="AR":
        orfor="Archival Material"
    elif of=="CD":
        orfor="CD-ROM"
    elif of=="CN":
        orfor="Serial"
    elif of=="DB":
        orfor="Database"
    elif of=="DV":
        orfor="DVD/Blu-ray"
    elif of=="EB":
        orfor="E-Book"
    elif of=="EJ":
        orfor="E-Journal"
    elif of=="EP":
        orfor="E-Book Package"
    elif of=="FL":
        orfor="Film"
    elif of=="GP":
        orfor="Government Publication"
    elif of=="IM":
        orfor="Image"
    elif of=="IS":
        orfor="Admin"
    elif of=="JP":
        orfor="E-Journal Package"
    elif of=="LP":
        orfor="LP Phonorecord"
    elif of=="M":
        orfor="Book"
    elif of=="MC":
        orfor="Audio CD"
    elif of=="MF":
        orfor="Microform"
    elif of=="MP":
        orfor="Map"
    elif of=="NE":
        orfor="Newspaper"
    elif of=="PJ":
        orfor="Journal"
    elif of=="SC":
        orfor="Music Score"
    elif of=="SE":
        orfor="Serial"
    elif of=="ST":
        orfor="Streaming Video"
        #Streaming Video or Streaming Audio?
    elif of=="T":
        orfor="Admin"
    elif of=="TH":
        orfor="Thesis/Dissertation"
    return orfor


def one_time(lineToread,cust):
    Ordarchivo=open(cust+"_orders.json", 'a')
    acqUnitIds=[]
    #acqUnitIds=acquisition_unit(cust)
    uuid_order=str(uuid.uuid4())
    print("Procesing Monograph Order: ", lineToread[3])
    id_loc=get_locId(cust)
    productIdType= "913300b2-03ed-469a-8179-c1092c991227"
    if lineToread[26]:
        details={"productIds": [{"productId": str(lineToread[26].strip()),"productIdType": productIdType}],"subscriptionFrom": "","subscriptionTo":"","subscriptionInterval": ""}
    else:
        details=""

    #no date is not a suscription
    order={
        "id": uuid_order,
        "assignedTo": "",
        "billTo": acquisition_unit(cust), 
        "shipTo": acquisition_unit(cust),
        "manualPo": False,
        "approved": True, #add
        "orderType":"One-Time",
        "poNumber": str(lineToread[3].strip()),
        "totalItems":1,
        "vendor": get_OrgId(lineToread[16].strip()),
        "workflowStatus": "Open",
        "notes": notes_tupla(lineToread),
        "totalEstimatedPrice": price(lineToread[19].strip()),
        "tags":{"tagList":["ALEPH"]},
        "compositePoLines": [
            {
                "id": str(uuid.uuid4()),
                "acquisitionMethod": purchase_method(lineToread[15].strip()),
                "cancellationRestriction": False,
                "rush": False,
                "selector": "",
                "cost": {"currency": "USD","listUnitPrice": price(lineToread[19].strip()),"quantityPhysical": 1},
                "locations": [{"locationId":id_loc, "quantityPhysical":1}],
                "receiptStatus": "Pending",
                "orderFormat" : "Physical Resource",
                  #"details":{"receivingNote": "ABCDEFGHIJKL"},
                    #"poLineDescription": publisher,
                "poLineNumber": str(lineToread[3].strip())+"-1",
                "details": details,
                "physical":{"createInventory":"None","volumes":"","materialType": get_MaterialType(lineToread[27].strip())},##add mt, exp receipt
                    "source": "User",
                "titleOrPackage": lineToread[24].strip(),
                "contributors": [{"contributor": str(lineToread[25].strip()) ,"contributorNameTypeId": "2b94c631-fca9-4892-a730-03ee529ffe2a"}],
                #"fundDistribution":funds_p,#[{"code":sierra_fund_code, "fundId": fund_id, "distributionType": "percentage","value": 100}], ##add
                "isPackage": False,
                "vendorDetail": {"instructions": instructionsVendor(lineToread[28].strip())},
                }]
             }
    json_ord = json.dumps(order)
    print('Datos en formato JSON', json_ord)
    Ordarchivo.write(json_ord+"\n")



def ongoing(lineToread,cust):
    Ordarchivo=open(cust+"_orders.json", 'a')
    uuid_order=str(uuid.uuid4())
    acqUnitIds=[]
    productIdType= "913300b2-03ed-469a-8179-c1092c991227"
    renewalDate=date_stamp(str(lineToread[23]).strip())
    subscriptionFrom=date_stamp(str(lineToread[21])).strip()
    subscriptionTo=date_stamp(str(lineToread[22])).strip()
    expectedActivationDate=subscriptionTo
    id_loc=get_locId(cust)
    orderFormat=""
    if lineToread[26]:
        details={"productIds": [{"productId": str(lineToread[26].strip()),"productIdType": productIdType}],"subscriptionFrom": "","subscriptionTo":"","subscriptionInterval": ""}
    else:
        details=""

    orderFormat=order_format(lineToread[27].strip())
    
    vendor=get_OrgId(lineToread[16].strip())
    if (orderFormat=="Electronic Resource"):
            order= {
                "id":uuid_order,
                "approved": True,
                "billTo": acquisition_unit(cust), 
                "manualPo": False,
                "notes": notes_tupla(lineToread),
                "poNumber": str(lineToread[3].strip()),
                "orderType": "Ongoing",
                "reEncumber": False,
                "ongoing": {"interval": 365,"isSubscription": True,"renewalDate": renewalDate},
                "shipTo": acquisition_unit(cust),
                "totalEstimatedPrice": price(lineToread[19].strip()),
                "totalItems": 1,
                "vendor": vendor,
                "workflowStatus": "Open",
                "compositePoLines": [
                    {
                        "id": str(uuid.uuid4()),
                        "checkinItems": False,
                        "acquisitionMethod": "Purchase At Vendor System",
                        "alerts": [],
                        "claims": [],
                        "collection": False,
                        "contributors": [],
                        "cost": {"listUnitPriceElectronic": price(lineToread[19].strip()),"currency": "USD","discountType": "percentage","quantityElectronic": 1,"poLineEstimatedPrice": price(lineToread[19].strip())},
                        "details": {"productIds": [],"subscriptionInterval": 0},
                        "eresource": {"activated": True,"activationDue": -623,"createInventory": "None","trial": False,"expectedActivation": expectedActivationDate,"userLimit":"", "accessProvider": vendor,"materialType": get_MaterialType(lineToread[27].strip())},
                        #"fundDistribution": [{"code": fund[1],"fundId": fund[0],"distributionType": "percentage","value": 100.0}],
                        "isPackage": False,
                        #"locations": [{"locationId": id_loc,"quantity": 1,"quantityElectronic": 1,"quantityPhysical": 0}],
                        "orderFormat": "Electronic Resource",
                        "paymentStatus": "Payment Not Required",
                        "physical": {"createInventory": "None","materialSupplier": vendor,"volumes": []},
                        "poLineNumber": str(lineToread[3].strip())+"-1",
                        "receiptStatus": "Receipt Not Required",
                        "reportingCodes": [],
                        "rush": False,
                        "source": "User",
                        #"instanceId": instanceid,
                        "titleOrPackage": lineToread[24].strip(),
                        "contributors": [{"contributor": str(lineToread[25].strip()) ,"contributorNameTypeId": "2b94c631-fca9-4892-a730-03ee529ffe2a"}],
                        "vendorDetail": {"instructions": instructionsVendor(lineToread[28].strip())},
                        #"vendorDetail": {"instructions": instructionsVendor,"refNumber": self.poNumber,"refNumberType": "Internal vendor number","vendorAccount": ""},
                     }],
                "acqUnitIds": [],
               }

    elif (orderFormat=="Physical Resource"):
                order= {
                    "id":uuid_order,
                    "approved": True,
                    "billTo": acquisition_unit(cust), 
                    "manualPo": False,
                    "notes": notes_tupla(lineToread),
                    "poNumber": str(lineToread[3].strip()),
                    "orderType": "Ongoing",
                    "reEncumber": False,
                    "ongoing": {"interval": 365,"isSubscription": True,"renewalDate": renewalDate},
                    "shipTo": acquisition_unit(cust),
                    "totalEstimatedPrice": price(lineToread[19].strip()),
                    "totalItems": 1,
                    "vendor": vendor,
                    "workflowStatus": "Open",
                    "compositePoLines": [
                        {
                            "id": str(uuid.uuid4()),
                            "checkinItems": False,
                            "acquisitionMethod": "Purchase At Vendor System",
                            "alerts": [],
                            "claims": [],
                            "collection": False,
                            "contributors": [],
                            "cost": {"listUnitPrice": price(lineToread[19].strip()),"currency": "USD","discountType": "percentage","quantityPhysical": 1,"poLineEstimatedPrice": price(lineToread[19].strip())},
                            "details": {"productIds": [],"subscriptionInterval": 0},
                            "eresource": {"activated": True,"activationDue": -623,"createInventory": "None","trial": False,"expectedActivation": expectedActivationDate,"userLimit":"",      "accessProvider": vendor,"materialType": materialType},
                            "fundDistribution": [{"code": fund[1],"fundId": fund[0],"distributionType": "percentage","value": 100.0}],
                            "isPackage": False,
                            "locations": [{"locationId":id_loc, "quantityPhysical":1}],
                            "orderFormat": "Physical Resource",
                            "paymentStatus": "Payment Not Required",
                            "physical": {"createInventory": "None","materialSupplier": vendor,"volumes": []},
                            "poLineNumber": str(lineToread[3].strip())+"-1",
                            "receiptStatus": "Receipt Not Required",
                            "reportingCodes": [],
                            "rush": False,
                            "source": "User",
                            #"instanceId": instanceid,
                            "titleOrPackage": title,
                            #"vendorDetail": {"instructions": instructionsVendor},
                        }],
                    "acqUnitIds": [],
                   }
         
    #json_ord = json.dumps(order,indent=2)
    json_ord = json.dumps(order)
    print('Datos en formato JSON', json_ord)
    Ordarchivo.write(json_ord+"\n")
###############################################
##
##
##############################################
def Orders_AlephToFolio(NamefileToRead, NamefileToPrint):
    org=NamefileToPrint 
    m=0
    o=0
    s=0
    count=0
    f = open("Error_Original_EBSCO_Recurring_Orders.txt", "a")
    with open(NamefileToRead, encoding="utf-8") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter='|')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                print(f'Column names are {", ".join(row)}')
                line_count += 1
            else:
                count+=1
                print("Record No.", str(count))
                print(f'\t{row[0]} working with Purchase Number: {row[3]} title {row[25]} order type {row[2]}, {row[26]}')
                if row[1].strip()=="S":
                    #if row[22]!="0":
                     s+=1
                     ongoing(row,NamefileToPrint)
                    #else:
                    #    'm+=1
                    #    'one_time(row,NamefileToPrint)
                elif row[1].strip()=="O":
                   # if row[22]!="0":
                     o+=1
                     ongoing(row,NamefileToPrint)
                    #else:
                    #    m+=1
                    #    one_time(row,NamefileToPrint)
                elif row[1].strip()=="M":
                    if row[22]=="0":
                       m+=1
                       one_time(row,NamefileToPrint)
            line_count += 1

        print(f'Processed {line_count} lines.')
        f.write(str(m),str(s))
        
##end

if __name__ == "__main__":
    """This is the Starting point for the script"""
    customerName="UM"
    Orders_AlephToFolio("Orders/UMA_ORDERS_z13.dsv",customerName)
    