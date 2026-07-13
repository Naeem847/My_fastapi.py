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
   
