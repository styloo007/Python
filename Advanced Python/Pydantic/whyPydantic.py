# 1 - A Simple function

def insertPatientData(name, age):
    print(name)
    print(age)
    print("Inserted into Database")
    

insertPatientData("Nitish","Twenty Two")


# 2 - Data Type being declare, but still not helpful

def insertPatientData2(name: str, age: int):
    print(name)
    print(age)
    print("Inserted into Database")
    

insertPatientData2("Shashank","Twenty Two")

# 3 - Data Type Validation Done

def insertPatientData3(name: str, age: int):
    if type(age)==int and type(name)==str:
        print(name)
        print(age)
        print("Inserted Into Database")
    else:
        raise TypeError("Incorrect Data Type")

insertPatientData3("Shashank", 22)

# 4 - Data Validation also done

def insertPatientData4(name: str, age: int):
    if type(name)==str and type(age)==int:
        if age<0:
            raise ValueError("Age cannot be negative")
        print(name)
        print(age)
        print("Inserted into database")
    else:
        raise TypeError('Incorrect Data Type')

insertPatientData4("Shashank", 22)

# 5 - Pydantic

from pydantic import BaseModel

class Patient(BaseModel):
    name: str
    age: int


def insertPatientInfo5(patient: Patient):
    print(patient.name)
    print(patient.age)
    print("Inserted into DB")

def updatePatientInfo(patient: Patient):
    print(patient.name)
    print(patient.age)
    print("Patient Info Updated")

patientInfo = {'name':'Shashank','age':22}
patient1 =  Patient(**patientInfo)

insertPatientInfo5(patient1)
updatePatientInfo(patient1)

# 6 - Pydantic - Exploring More

from pydantic import EmailStr, AnyUrl, Field
from typing import List, Dict, Optional, Annotated

class Patient(BaseModel):
    name: Annotated[str, Field(max_length=75, title='Name of the Patient', description='Full name of the person, including given name and family name.', examples=['Jon Doe'])]
    age: int = Field(gt=0, lt=150)
    email: EmailStr
    linkedinURL: AnyUrl
    weight: float = Field(gt=0, strict=True)
    married: Annotated[bool, Field(default=None, description='Is the Person Single or Married')]
    allergies: Annotated[Optional[List[str]], Field(default=None, title='List of allergies', description='List of all the allergies encountered by the patient', max_length=5, examples=['Pollen','Cold'])] 
    contactDetails: Dict[str, str]
    
    

def insertPatientInfo6(patient: Patient):
    print(patient.name)
    print(patient.age)
    print(patient.email)
    print(patient.linkedinURL)
    print(patient.weight)
    print(patient.married)
    print(patient.allergies)
    print(patient.contactDetails)
    print("Inserted into DB")

def updatePatientInfo6(patient: Patient):
    print(patient.name)
    print(patient.age)
    print(patient.email)
    print(patient.linkedinURL)
    print(patient.weight)
    print(patient.married)
    print(patient.allergies)
    print(patient.contactDetails)
    print("Patient Info Updated")

patientInfo = {'name':'Shashank','age':22,'email':'shashank@gmail.com','linkedinURL':'https://www.linkedin.com/in/shashankagasimani' ,'weight':72.5, 'married': False, 'allergies':['pollen', 'dust', 'cold'], 'contactDetails': {'mobile':'9900992541'}}
patient2 =  Patient(**patientInfo)

insertPatientInfo6(patient2)
updatePatientInfo6(patient2)


