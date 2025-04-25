class Libro:
  def __init__(self, titulo, autor, genero):
    self.titulo = titulo
    self.autor = autor
    self.genero = genero

  def __str__(self):
    return f"{self.titulo} de {self.autor}, del genero {self.genero}"