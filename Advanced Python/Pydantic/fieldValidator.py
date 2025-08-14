from pydantic import BaseModel, EmailStr, AnyUrl, Field, field_validator
from typing import List, Dict, Annotated, Optional

class Patient(BaseModel):
    name : Annotated[str, Field(title='Name of the Patient', description='First Name and Last of the Patient', max_length=75, examples=['Jon Doe'])]
    age : Annotated[int, Field(title='Age of the Patient', gt=0, lt=120, examples=[75,40,22])]
    email : EmailStr
    linkedinURL : AnyUrl
    weight : Annotated[float, Field(gt=0, lt=150, title='Weight of the Patient', strict=True)]
    married: Annotated[bool, Field(default=None, title='Is the Patient Married or Not')]
    allergies : Annotated[Optional[List[str]], Field(default=None, title='List of all the allergies', max_length=5, examples=['Pollen', 'Cold'])]
    contactInfo: Annotated[Dict[str,str], Field(title='Contact Details of the Patient')]
    
    @field_validator('email')
    @classmethod
    def emailValidator(cls, value):
        validDomains = ['icici.com', 'hdfc.com']
        domainName =  value.split('@')[-1]
        if domainName not in validDomains:
            raise ValueError("Domain Name not in Valid Domains")
        
        return value
    
    @field_validator('name')
    @classmethod
    def transformName(cls, value):
        return value.upper()
    
    @field_validator('age', mode='before') # Before would throw an error if the value is string, After wouldnt show an error as cohersion is already done ( After is by default)
    @classmethod
    def validateAge(cls, value):
        if 0 < value < 100:
            return value    
        else:
            raise ValueError('Age should be between 0 and 100')
            
    

def insertPatientDetails(patient: Patient):
    print(patient.name)
    print(patient.age)
    print(patient.email)
    print(patient.linkedinURL)
    print(patient.weight)
    print(patient.married)
    print(patient.allergies)
    print(patient.contactInfo)
    print("Inserted into DB Successfully")
    

patientDetails = {'name':'Shashank', 'age':22, 'email':'shashankagasimani2@hdfc.com','linkedinURL':'https://www.linkedin.com/in/shashankagasimani','weight':72.5, 'married':False,'contactInfo':{'Mobile':'8310252671'}}
patient1 = Patient(**patientDetails)

insertPatientDetails(patient1)