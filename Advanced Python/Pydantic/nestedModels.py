from pydantic import BaseModel

class Address(BaseModel):
    city: str
    state: str
    pincode: int

class Patient(BaseModel):
    name: str
    age: int
    gender: str
    address: Address

addressDict = {'city':'Bangalore', 'state':'Karnataka', 'pincode':510024}
patientDict = {'name':'Shashank', 'age':22, 'gender':'Male', 'address':addressDict}
patient1 = Patient(**patientDict)

print(patient1.name)
print(patient1.age)
print(patient1.gender)
print(patient1.address.city)
print(patient1.address.state)
print(patient1.address.pincode)