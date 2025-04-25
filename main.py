from lib.libro import Libro
from lib.alumno import Alumno
from lib.lectura import Lectura
from lib.grupo import Grupo
from lib.club import Club

# Creamos un club de lectura
club = Club("Club de Lectura de la Prepa")

# Agregamos grupos al club
club.agregar_grupo(
  Grupo(
    "Ladrones de libros", 
    "Para leer, disfrutar y llorar juntos"
  )
)

club.agregar_grupo(
  Grupo(
    "Cuentos de terror", 
    "Para leer, disfrutar y tener pesadillas"
  )
)

# Agregamos miembros al club
club.agregar_miembro(Alumno("Juan Perez", 14, "Cuarto"))
club.agregar_miembro(Alumno("Maria Lopez", 15, "Quinto"))
club.agregar_miembro(Alumno("Pedro Gonzalez", 16, "Sexto"))

# Registramos a los miembros en los grupos
club.agregar_miembro_a_grupo(club.miembros[0], club.grupos[0])
club.agregar_miembro_a_grupo(club.miembros[1], club.grupos[0])
club.agregar_miembro_a_grupo(club.miembros[2], club.grupos[1])

# Registramos lecturas en los grupos
club.asignar_lectura_a_grupo(
  Lectura(
    Libro("Frankenstein", "Mary Shelley", "Ficción"),
    "2025-05-31"
  ),
  club.grupos[0]
)

club.asignar_lectura_a_grupo(
  Lectura(
    Libro("Dracula", "Bram Stoker", "Terror"),
    "2025-05-30"
  ),
  club.grupos[1]
)

# Actualizamos el progreso de las lecturas
club.actualizar_progreso_lectura(20, club.grupos[0].lecturas[0]) 
club.actualizar_progreso_lectura(30, club.grupos[1].lecturas[0])

# print(club)
club.mostrar_grupos()