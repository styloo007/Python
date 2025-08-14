from pydantic import BaseModel, AnyUrl, Field, EmailStr, field_validator, model_validator
from typing import List, Dict, Annotated, Optional

class Patient(BaseModel):
    name: str
    age: int
    weight: float
    married: bool
    allergies: List[str]
    contactInfo: Dict[str,str]
    
    @model_validator(mode='after')
    def validateEmergencyContact(cls, model):
        if model.age>60 and 'emergency' not in model.contactInfo:
            raise ValueError('Patients Older than 60 must have an Emergency Contact Number')
        else:
            return model
    


def insertPatientInfo(patient: Patient):
    print(patient.name)
    print(patient.age)
    print(patient.weight)
    print(patient.married)
    print(patient.allergies)
    print(patient.contactInfo)
    print("Patient Info Added into DB")

patientInfo = {'name':'Shashank','age':62,'weight':72.5,'married':False,'allergies':['Cold'],'contactInfo':{'Mobile':'8310252671'}}
patient1 =  Patient(**patientInfo)
insertPatientInfo(patient1)

