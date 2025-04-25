class Club:
  def __init__(self, nombre):
    self.nombre = nombre
    self.grupos = []
    self.miembros = []

  def __str__(self):
    return f"Club '{self.nombre}' con {len(self.grupos)} grupos y {len(self.miembros)} miembros."
  
  def agregar_grupo(self, grupo):
    self.grupos.append(grupo)

  def agregar_miembro(self, miembro):
    self.miembros.append(miembro)

  def agregar_miembro_a_grupo(self, miembro, grupo):
    grupo.agregar_miembro(miembro)

  def asignar_lectura_a_grupo(self, lectura, grupo):
    grupo.agregar_lectura(lectura)

  def mostrar_grupos(self):
    for grupo in self.grupos:
      print(grupo)
      grupo.mostrar_miembros()
      grupo.mostrar_lecturas()

  def actualizar_progreso_lectura(self,valor, lectura):
    lectura.progreso += valor
    print(f"Progreso de la lectura '{lectura.libro.titulo}' actualizado a {lectura.progreso}%")