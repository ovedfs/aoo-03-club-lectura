class Grupo:
  def __init__(self, nombre, descripcion):
    self.nombre = nombre
    self.descripcion = descripcion
    self.miembros = []
    self.lecturas = []

  def __str__(self):
    return f"Grupo '{self.nombre}': {self.descripcion}"
  
  def agregar_miembro(self, miembro):
    self.miembros.append(miembro)

  def agregar_lectura(self, lectura):
    self.lecturas.append(lectura)

  def mostrar_miembros(self):
    for miembro in self.miembros:
      print(miembro)

  def mostrar_lecturas(self):
    for lectura in self.lecturas:
      print(lectura)