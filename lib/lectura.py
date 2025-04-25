class Lectura:
  def __init__(self, libro, fecha_limite):
    self.libro = libro
    self.fecha_limite = fecha_limite
    self.progreso = 0

  def __str__(self):
    return f"Lectura de '{self.libro.titulo}' hasta {self.fecha_limite}, progreso: {self.progreso}%"