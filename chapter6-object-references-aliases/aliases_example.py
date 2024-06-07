andres_student = { 'name' : 'Andres', 'lastname': 'Laurito', 'age': 32 } 
andres_software_engineer = andres_student

"Same objects"
print(f"Ids: {id(andres_student)}, {id(andres_software_engineer)}")

print(andres_student is andres_software_engineer)

impostor = { 'name' : 'Andres', 'lastname': 'Laurito', 'age': 32 }

"Same values, different objects"
print(f"Equality: {andres_student == impostor}")
print(f"Identity: {andres_student is impostor}")
