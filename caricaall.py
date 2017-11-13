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
 ["WAS","D55WQLL","IBM Websphere Application Server Network Deployment Processor Value Unit (Pvu) for Linux on System z License + Sw Subscription & Support 12 Months	","PVU","UEL"],
 ["WAS","E025TLL","IBM WebSphere Application Server Network Deployment Processor Value Unit (PVU) for Linux on System z Annual SW Subscription & Support Renewal","PVU","UEL"],
 ["WAS","E025SLL","IBM WebSphere Application Server Network Deployment Processor Value Unit (PVU) Annual SW Subscription & Support Renewal","PVU","	7980"],
 ["WAS","E025TLL","IBM WebSphere Application Server Network Deployment Processor Value Unit (PVU) for Linux on System z Annual SW Subscription & Support Renewal","PVU","34209"],
 ["WAS","E02A5LL","IBM WebSphere Extended Deployment Processor Value Unit (PVU) Annual SW Subscription & Support Renewal","PVU","8967"],
 ["WAS","E02EALL","IBM WebSphere Extended Deployment for Processor Value Unit (PVU)","PVU","12473"],
 ["InfoSphere","E0DKFLL","IBM InfoSphere Information Server Enterprise Edition Linux on System z Processor Value Unit (PVU) Annual SW Subscription & Support Renewal","PVU","3360"],
 ["InfoSphere","E0DLELL","IBM InfoSphere Information Server Enterprise Edition for Non-Production Environments Linux on system z Processor Value Unit (PVU) Annual SW Subscription & Support Renewal","PVU","1800"],
 ["C","E04U7LL","IBM XL C/C++ for AIX Concurrent User License + SW Subscription & Support 12 Months","Concurrent","10 User"],
 ["C","E1AHNLL","IBM XL C/C++ for AIX Authorized User Annual SW Subscription & Support 12 Months","Authorized users","	2"],
 ["Db2 connect","E005DLL","IBM Db2 Connect Unlimited Edition for System z for Linux on z Host Server Annual SW Subscription & Support Renewal","Server","1"],
 ["Db2 connect","E005FLL","IBM Db2 Connect Unlimited Edition for System z for Linux on z Millions of Service Units per Hour Annual SW Subscription & Support Renewal","Service Units","3418"],
 ["Db2 connect","D50N0LL","IBM Db2 Connect Unlimited Edition for System z for Linux on z Millions of Service Units per Hour License + SW Subscription & Support 12 Months","Service Units","736"],
 ["Optim","E0DXRLL","IBM InfoSphere Optim Test Data Management Enterprise Edition Terabyte System z Annual SW Subscription & Support Renewal","TB","7"],
 ["Db2","E0HPVLL","IBM Db2 Advanced Enterprise Server Edition Processor Value Unit (PVU) Annual SW Subscription & Support Renewal","PVU","3200"],
 ["Db2","E0HPWLL","IBM Db2 Advanced Enterprise Server Edition Linux on System z Processor Value Unit (PVU) Annual SW Subscription & Support Renewal","PVU","1000"],
 ["DataPower","E0HHPLL","IBM WebSphere DataPower Integration Appliance XI52 Appliance Install Annual Appliance Maintenance + Subscription and Support Renewal","Appliance","4"],
 ["DataPower","E0HHQLL","IBM WebSphere DataPower Integration Appliance XI52 Appliance Install Subsequent Appliance Business Critical Service Upgrade 12 Months","Appliance","4"],
 ["DataPower","E0HI8LL","IBM Application Optimization for WebSphere DataPower Integration Appliance XI52 Application Instance Annual SW Subscription & Support Renewal	","Appliance","2"],
 ["DataPower","E0HI7LL","IBM Database Connectivity for WebSphere DataPower Integration Appliance XI52 Application Instance Annual SW Subscription & Support Renewal","Appliance","4"],
 ["DataPower","E0HIALL","IBM Tivoli Access Manager for WebSphere DataPower Integration Appliance XI52 Application instance Annual SW Subscription & Support Renewal","Appliance","2"],
 ["DataPower","E0KHULL","IBM DataPower Gateway Virtual Edition Processor Value Unit Annual Software Subscription & Support Renewal	","PVU","560"],
 ["DataPower","E0KHALL","IBM Integration Module for IBM DataPower Gateway Virtual Edition Processor Value Unit Annual Software Subscription & Support Renewal","PVU","	560"],
 ["DataPower","E0KHQLL","IBM DataPower Gateway Virtual Edition for Non Production Environment Processor Value Unit Annual Software Subscription & Support Renewal","PVU","560"],
 ["TWS","E02A8LL","IBM Workload Scheduler for zEnterprise BladeCenter Extension and Linux on System z Processor Value Unit (PVU) Annual SW Subscription & Support Renewal","PVU","14440"],
 ["BPM","E0BRGLL","IBM Process Designer Per Authorized User for System z Annual SW Subscription & Support Renewal	","Authorized users","15"],
 ["BPM","E0NUPLL","IBM Business Process Manager Server for Linux in z System Processor Value Unit (PVU) Annual SW Subscription And Support Renewal 12 months","PVU","	480"],
 ["BPM","E0NUPLL","IBM Business Process Manager Server for Linux in z System Processor Value Unit (PVU) Annual SW Subscription And Support Renewal 12 months","PVU","	1920"],
 ["Rational","E07RPLL","IBM Rational Asset Manager Enterprise Edition Publisher for System z Floating User Single Install","Floating User","16"],
 ["Rational","E01MJLL","IBM Rational Application Developer for WebSphere Software Authorized User Annual  	","Authorized users","163"],
 ["Rational","E08BULL","IBM Rational DOORS Next Generation Analyst for System z Floating User Single Install license  	","Floating User","40"],
 ["Rational","E06JLLL","IBM Rational Quality Manager Quality Professional for System z Floating User Single Install Annual SW Subscription & Support Renewal","Floating User","15"],
 ["Rational","E0130LL","IBM Rational ClearQuest Floating User Annual SW Subscription & Support Renewal	","Floating User","1"],
 ["Rational","E0AGPLL","IBM Rational Method Composer Floating User Single Install Annual SW Subscription & Support Renewal","Floating User","1"],
 ["Rational","E012DLL","IBM Rational Functional Tester Floating User Annual SW Subscription & Support Renewal","Floating User","1"],
 ["Rational","E0742LL","IBM Rational Publishing Engine Floating User Annual SW Subscription & Support Renewal","Floating User","1"],
 ["Rational","E0AMLLL","IBM Rational Team Concert Stakeholder Authorized User Single Install Annual SW Subscription & Support Renewal","Authorized users","40"],
 ["Rational","E0AQDLL","IBM Rational Team Concert Stakeholder Floating User Single Install Annual SW Subscription & Support Renewal","Floating User","10"],
 ["Rational","E01MALL","IBM Rational Performance Tester Floating User Annual SW Subscription & Support Renewal","Floating User","4"],
 ["Rational","E06JLLL","IBM Rational Quality Manager Quality Professional for System z Floating User Single Install Annual SW Subscription & Support Renewal","Floating User","60"],
 ["Rational","E0HNPLL","IBM Rational Developer for the Enterprise Floating User Single Install for System z Annual SW Subscription & Support Renewal","Floating User","20"],
 ["Rational","E08BULL","IBM Rational DOORS Next Generation Analyst for System z Floating User Single Install license Annual SW Subscription & Support Renewal","Floating User","26"],
 ["Rational","E01I5LL","IBM Rational Functional Tester S390 Floating User Annual SW Subscription & Support Renewal","Floating User","18"],
 ["Rational","E03MMLL","IBM Rational Service Tester for SOA Quality for System z Floating User Annual SW Subscription & Support Renewal","Floating User","	18"],
 ["Rational","E012HLL","IBM Rational Performance Test Pack Virtual Testers 500 Floating User Annual SW Subscription & Support Renewal","Floating User","3"],
 ["Rational","E03NDLL","IBM Rational Performance Tester Extension for SOA Floating User Annual SW Subscription & Support Renewal","Floating User","1"],
 ["Rational","E06JKLL","IBM Rational Quality Manager Quality Professional Floating User Single Install Annual SW Subscription & Support Renewal","Floating User","4"],
 ["Rational","E055ILL","IBM Rational Asset Analyzer Authorized User Single Install for System z SW Subscription & Support Renewal","Authorized users","18"],
 ["Rational","E07RCLL","IBM Rational Asset Manager Standard Edition Authorized User Single Install Annual SW Subscription & Support Renewal","Authorized users","12"],
 ["Rational","E0665LL","IBM Rational DOORS Next Generation Contributor Authorized User Single Install license Annual SW Subscription & Support Renewal","Authorized users","15"],
 ["Rational","E05M7LL","IBM Rational Quality Manager Quality Professional Authorized User Single Install Annual SW Subscription & Support Renewal","Authorized users","30"],
 ["Rational","E012LLL","IBM Rational Performance Test Pack Virtual Testers 1000 Floating Users Annual SW Subscription & Support Renewal","Floating User","1"],
 ["Rational","E0APFLL","IBM Rational Asset Analyzer Floating User Single Install for System z Annual SW Subscription & Support Renewal","Floating User","5"],
 ["Rational","E08BVLL","IBM Rational DOORS Next Generation Analyst Floating User Single Install license Annual SW Subscription & Support Renewal","Floating User","9"],
 ["Rational","E0AMCLL","IBM Rational Team Concert Developer for Workgroups Authorized User Single Install Annual SW Subscription & Support Renewal","Authorized users","20"],
 ["Rational","E060ILL","IBM Rational DOORS Next Generation Analyst Authorized User Single Install license Annual SW Subscription & Support Renewal","Authorized users","30"],
 ["Developer","E0DWQLL","IBM Developer for z Systems Floating Users Single Install Annual SW Subscription & Support Renewal","Floating User","	20"],
 ["Monitoring","E0LH1LL","IBM Monitoring zLinux Managed Virtual Server Annual SW Subscription & Support Renewal 12 Months","Managed Virtual Server","1665"],
 ["Monitoring","E0LH2LL","IBM Monitoring zLinux Managed Virtual Server Annual SW Subscription & Support Renewal 12 Months","Managed Virtual Server","213"],
 ["APM","E0LS0LL","IBM Cloud Application Performance Management Advanced Private  for System z Managed Virtual Server Annual SW Subscription & Support Renewal 12 Months (ex IBM Application Performance Management for System z Managed Virtual Server  SW Subscription & Support 12 Months)	","Managed Virtual Server","150"],
 ["APM","E0LS0LL","IBM Cloud Application Performance Management Advanced Private for System z Managed Virtual Server License + SW Subscription & Support 12 Months (ex IBM Application Performance Management Advanced for System z Managed Virtual Server  SW Subscription & Support 12 Months)","Managed Virtual Server","521"],
 ["Netcool","E0J97LL","IBM Netcool Operations Insight PA Operations Management Managed Virtual Server","Managed Virtual Server","	6000"],
 ["Netcool","E0J99LL","IBM Netcool Operations Insight Operations Management Managed Virtual Network Device","Managed Virtual Network Device","1200"],
 ["Netcool","E0J9DLL","IBM Netcool Operations Insight PA Connection","Connection","7"],
 ["Netcool","E0J9BLL","IBM Netcool Operations Insight Operations Management 10 Managed Client Devices","Managed Client Devices","13"],
 ["Copy Services","E0MK5LL","IBM Copy Services Manager Resource Value Units Annual SW Subscription & Support Renewal","TB /RVU","128"],
 ["Spectrum","E0M69LL","IBM Spectrum Storage Suite per Terabyte Annual SW Subscription & Support Renewal 	","Terabyte","7.824"],
 ["Spectrum","D1K7XLL","IBM Spectrum Storage Suite per Terabyte License + SW Subscription & Support 12 Months","Terabyte","4408"],
 ["Spectrum","E0M69LL","IBM Spectrum Storage Suite per Terabyte Annual SW Subscription & Support Renewal","Terabyte","4408"],
 ["Spectrum","D1K7XLL","IBM Spectrum Storage Suite per Terabyte License + SW Subscription & Support 12 Months","Terabyte","UEL"],
 ["Spectrum","E0M69LL","IBM Spectrum Storage Suite per Terabyte Annual SW Subscription & Support Renewal","Terabyte","UEL"],
 ["AppScan","E046ELL","IBM Security AppScan Standard for System Z Floating User Annual SW Subscription & Support Renewal","Floating User","	9"],
 ["AppScan","E0CRDLL","IBM Security AppScan Enterprise Server Install Annual SW Subscription & Support Renewal","Install","1"],
 ["AppScan","E06GHLL","IBM Security AppScan Enterprise Reporting Only User Floating User Single Install Annual SW Subscription & Support Renewal","Install","10"],
 ["AppScan","E046DLL","IBM Security AppScan Standard Floating User Single Install Annual SW Subscription & Support Renewal","Floating User","1"],
 ["AppScan","E086LLL","IBM Security AppScan Source for Automation Install Annual SW Subscription & Support Renewal","Install","1"],
 ["AppScan","E08KGLL","IBM Security AppScan Source for Analysis Floating User Single Install Annual SW Subscription & Support Renewal","Floating User","1"],
 ["AppScan","D0L75LL","IBM Security AppScan Enterprise Dynamic Analysis Scanner for System Z Install License + SW Subscription & Support 12 Months","Install","1"],
 ["AppScan","D07Y8LL","IBM Security AppScan Enterprise Dynamic Analysis Scanner Install License	","Floating User","3"],
 ["AppScan","E0M57LL","IBM Security Directory Suite Standard Edition Processor Value Unit (PVU) Annual SW Subscription & Support Renewal","PVU","100"],
 ["AppScan","E0M58LL","IBM Security Directory Suite Standard Standard Edition for Linux on z Systems Processor Value Unit (PVU) Annual SW Subscription & Support Renewal","PVU","3140"],
 ["BigFix","E0D75LL","IBM BigFix Inventory for Linux on System z Resource Value Unit Annual SW Subscription & Support Renewal","RVU","19975"],
 ["Data Explorer","E0IYXLL","IBM InfoSphere Data Explorer Enterprise Edition for System z Resource Value Unit Annual SW Subscription & Support Renewal","RVU","2"],
 ["Planning","E08BCLL","IBM Planning Analytics Local TM1 Server Processor Value Unit (PVU) Annual SW Subscription & Support Renewal (ex IBM Cognos Analytic Server Processor Value Unit (PVU) Annual SW Subscription & Support Renewal)","PVU","140"],
 ["Planning","E064KLL","IBM Planning Analytics Local TM1 Server for Non-Production Environment Processor Value Unit (PVU) Annual SW Subscription & Support Renewal (ex IBM Cognos Analytic Server for Non-Production Environment Processor Value Unit (PVU) Annual SW Subscription & Support Renewal)","PVU","70"],
 ["Cognos","E064ILL","IBM Cognos Performance Management User Authorized User Annual SW Subscription & Support Renewal","Authorized users","58"],
 ["Planning","E064GLL","IBM Planning Analytics Local Modeler Authorized User Annual SW Subscription & Support Renewal (ex IBM Cognos Performance Management Modeler Authorized User Annual SW Subscription & Support Renewal)","Authorized users","2"],
 ["MQ","E0256LL","IBM MQ Processor Value Unit (PVU) Annual SW Subscription & Support Renewal","PVU","2088"],
 ["MQ","E0257LL","IBM MQ for Linux on z Systems Processor Value Unit (PVU) Annual SW Subscription & Support Renewal","PVU","1162"],
 ["I2","E0BRLLL","IBM Integration Designer per Authorized User Annual SW Subscription & Support Renewal","Authorized users","33"],
 ["WAS","E025QLL","IBM WebSphere Application Server Processor Value Unit (PVU) Annual SW Subscription & Support Renewal","PVU","800"],
 ["WAS","E025RLL","IBM WebSphere Application Server Processor Value Unit (PVU), Linux on System z Annual SW Subscription & Support Renewal","PVU","1200"],
 ["Cobol","E1A1XLL","IBM COBOL for AIX Authorized User Annual SW Subscription & Support Renewal	","Authorized users","1"],
 ["Control Desk","E0CVLLL","IBM Control Desk Concurrent User Annual SW Subscription & Support Renewal","Concurrent user","20"],
 ["Control Desk","E0CVKLL","IBM Control Desk Authorized User for Linux on System z Annual SW Subscription & Support Renewal","Authorized users","1"],
 ["Control Desk","E0CVILL","IBM Control Desk Authorized User Annual SW Subscription & Support Renewal","Authorized users","4"],
 ["TADDM","E02ENLL","IBM Tivoli Application Dependency Discovery Manager Install Annual SW Subscription & Support Renewal","Install","3"],
 ["TADDM","E02EPLL","IBM Tivoli Application Dependency Discovery Manager Resource Value Unit Annual SW Subscription & Support Renewal","RVU","26682"],
 ["TADDM","E04TKLL","IBM Tivoli Application Dependency Discovery Manager for zOS Data for zEnterprise BladeCenter Extension and Linux on System z Resource Value Unit Annual SW Subscription & Support Renewal","RVU","7272"],
 ["ICO","E0K3WLL","IBM Cloud Orchestrator for Linux on System z Resource Value Unit Annual SW Subscription & Support Renewal","RVU","250"] 
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