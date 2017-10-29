from cloudant.client import Cloudant
from cloudant.error import CloudantException
from cloudant.result import Result, ResultByKey


client = Cloudant("a06db065-6da8-4109-8766-ccbeb58c614b-bluemix", "e9991cfd89d62c2e744beb736553c8dcb1d72d7774ea402ef3e5b43fc6570659", url="https://a06db065-6da8-4109-8766-ccbeb58c614b-bluemix:e9991cfd89d62c2e744beb736553c8dcb1d72d7774ea402ef3e5b43fc6570659@a06db065-6da8-4109-8766-ccbeb58c614b-bluemix.cloudant.com")
client.connect()

databaseName = "prodotti"
myDatabase = client.create_database(databaseName)

if myDatabase.exists():
   print('database successfully created')

sampleData = [
   	["TADDM", "E02ENLL", "IBM Tivoli Application Dependency Discovery Manager Install Annual SW Subscription & Support Renewal", "Install", "3"],
	["TADDM", "E02EPLL", "IBM Tivoli Application Dependency Discovery Manager Resource Value Unit Annual SW Subscription & Support Renewal", "RVU", "26682"],
	["TADDM", "E04TKLL", "IBM Tivoli Application Dependency Discovery Manager for zOS Data for zEnterprise BladeCenter Extension and Linux on System z Resource Value Unit Annual SW Subscription & Support Renewal", "RVU", "7272"],
	["Control Desk", "E0CVLLL", "IBM Control Desk Concurrent User Annual SW Subscription & Support Renewal", "Concurrent User", "20"],
	["Control Desk", "E0CVKLL", "IBM Control Desk Authorized User for Linux on System z Annual SW Subscription & Support Renewal", "Authorized User", "1"],
	["Control Desk", "E0CVILL", "IBM Control Desk Authorized User Annual SW Subscription & Support Renewal", "Authorized User", "4"]
	]
# Create documents using the sample data.
# Go through each row in the array

for document in sampleData:
 # Retrieve the fields in each row.
 nomecorrente = document[0]
 partnumber = document[1]
 descrizione = document[2]
 unitadimisura = document[3]
 quantita = document[4]

 # Create a JSON document that represents
 # all the data in the row.
 jsonDocument = {
  "nomecorrente": nomecorrente,
  "partnumber": partnumber,
  "descrizione": descrizione,
  "unitadimisura": unitadimisura,
  "quantita": quantita
 }

 # Create a document using the Database API.
 newDocument = myDatabase.create_document(jsonDocument)

 # Check that the document exists in the database.
 if newDocument.exists():
    print ("Document successfully created ")