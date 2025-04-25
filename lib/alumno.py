class Alumno:
  def __init__(self, nombre, edad, grado):  
    self.nombre = nombre
    self.edad = edad
    self.grado = grado
    self.grupos = []
  
  def __str__(self):
    return f"{self.nombre}, {self.edad} años, {self.grado} grado"