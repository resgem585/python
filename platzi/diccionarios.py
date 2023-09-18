""" En este desafío, deberás calcular el promedio general de una clase, así como el promedio individual de cada estudiante.

Para ello, se te proporcionará una lista de diccionarios, cada uno de los cuales representará a un estudiante y tendrá las siguientes propiedades:

"name": El nombre del estudiante
"grades": Las notas de cada materia del estudiante
A partir de esta información, debes retornar un nuevo diccionario que tenga la propiedad "class_average" con el promedio de la clase y una lista de "students" con los estudiantes y sus promedios individuales. """


def get_student_average(students):
  rta = {
    "class_average": 0,
    "students": []
  }
  
  for student in students:
    average = 0
    grades = student["grades"]
    
    for grade in grades:
      average += grade
      
    
    average = average / len(grades)
    rta["class_average"] += average
    rta["students"].append({
      "name": student["name"],
      "average": round(average, 2)
    })
  
  rta["class_average"] = rta["class_average"] / len(students)
  rta["class_average"] = round(rta["class_average"], 2)
  
  return rta

response = get_student_average([
  {
    "name": "Pedro",
    "grades": [90, 87, 88, 90],
  },
  {
    "name": "Jose",
    "grades": [99, 71, 88, 96],
  },
  {
    "name": "Maria",
    "grades": [92, 81, 80, 96],
  },
])

print(response)