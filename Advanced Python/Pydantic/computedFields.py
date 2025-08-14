from pydantic import BaseModel, AnyUrl, Field, EmailStr, field_validator, model_validator, computed_field
from typing import List, Dict, Annotated, Optional

class Patient(BaseModel):
    name: str
    age: int
    weight: float
    height: float
    married: bool
    allergies: List[str]
    contactInfo: Dict[str,str]
    
    @computed_field
    @property
    def bmi(self) -> float:
        bmi = round(self.weight/self.height**2)
        return bmi


def insertPatientInfo(patient: Patient):
    print(patient.name)
    print(patient.age)
    print(patient.weight)
    print(patient.height)
    print(patient.married)
    print(patient.allergies)
    print(patient.contactInfo)
    print("Patient Info Added into DB")
    
    
def updatePatientInfo(patient: Patient):
    print(patient.name)
    print(patient.age)
    print(patient.weight)
    print(patient.height)
    print(patient.bmi)
    print(patient.married)
    print(patient.allergies)
    print(patient.contactInfo)
    print("Patient Info Added into DB")

patientInfo = {'name':'Shashank','age':62,'weight':72.5, 'height':1.76 ,'married':False,'allergies':['Cold'],'contactInfo':{'Mobile':'8310252671'}}
patient1 =  Patient(**patientInfo)
insertPatientInfo(patient1)
updatePatientInfo(patient1)

