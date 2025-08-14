from pydantic import BaseModel

class Address(BaseModel):
    country: str
    state: str
    city: str
    pincode: int

class Patient(BaseModel):
    name: str
    age: int
    weight: float
    height: float
    address: Address

addressDict = {'country':'India', 'state':'Karnataka', 'city':'Bengaluru', 'pincode':510032}

patientDict = {'name':'Shashank','age':22, 'weight':72.5, 'height':1.78, 'address':addressDict}

patient1 = Patient(**patientDict)

export = patient1.model_dump()
exportNameOnly = patient1.model_dump(include=['name'])
exportExcludeName = patient1.model_dump(exclude=['name'])
exportIncludeStateFromAddress = patient1.model_dump(include={'address':['state']})
print(export)
print(exportNameOnly)
print(exportExcludeName)
print(exportIncludeStateFromAddress)