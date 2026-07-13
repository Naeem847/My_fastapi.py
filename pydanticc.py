def insert_patient_data(name:str, age:int):

    if type(name) == str and type(age) == int:
       if age<0:
            raise ValueError("Age cannot be negative")
       else:

        print(name)
        print(age)

        print("insert into database")
    else:
        raise TypeError("Incorrect data type")  
      
insert_patient_data('ali', 25)


# update patient data

def update_patient_data(name:str, age:int):

    if type(name) == str and type(age) == int:
         if age<0:
                raise ValueError("Age cannot be negative")
         else:
          print(name)
          print(age)

          print("update in database")
    else:
        raise TypeError("Incorrect data type")  
      
update_patient_data('ali', 25)
   
from pydantic import BaseModel

class Patient(BaseModel):
    name: str
    age: int

def insert_patient_data(patient: Patient):
    print(patient.name)
    print(patient.age)
    print("inserted")
    print("insert into database")

patient_info={'name':'Ali', 'age':25}

patient1=Patient(**patient_info)


insert_patient_data(patient1)





