# Ejercicio 3: Sistema de Club de Lectura Escolar

## Enunciado:
Un grupo escolar tiene un **club de lectura** donde los alumnos pueden **registrarse** y **formar grupos de lectura**. Cada **grupo de lectura** **elige un libro**, **establece una fecha límite para terminarlo**, y registra el **progreso de lectura** de cada miembro en forma de porcentaje.

Cada **alumno** tiene un **nombre** y puede **participar** en uno o varios grupos.  
El sistema debe permitir **crear grupos**, **añadir miembros**, **asignar libros**, y **actualizar el progreso de lectura por alumno**. También debe permitir **ver el progreso promedio del grupo**.

---

## Instrucciones:
- Identifica sustantivos y verbos
- Crea las clases necesarias
- Establece relaciones entre objetos
- Haz un diagrama de clases simple
- Crea una implementación básica en Python

---

## Sustantivos:
- club
- grupo
- libro
- alumno
- lectura

## Verbos:
- registro (crear cuenta)
- crear (grupo)
- asignar lectura
- agregar miembro
- asignar libro
- registrar progreso
- ver progreso

---

# CLASES:

| CLASES | ATRIBUTOS | MÉTODOS |
| :--- | :--- | :--- |
| **Club** | lista de grupos | crear grupo, mostrar grupos, buscar grupo |
| **Grupo** | nombre, descripción, miembros (lista de alumnos), lecturas asignadas | agregar miembro, asignar lectura, ver progreso del grupo |
| **Lectura** | libro, fecha límite, progreso por alumno | registrar progreso, obtener progreso alumno, calcular progreso promedio |
| **Libro** | título, autor, género | mostrar información |
| **Alumno** | nombre, edad, grado, grupos (lista de grupos en los que participa) | unirse a grupo, actualizar progreso |

```mermaid
classDiagram
    Club "1" --> "*" Grupo : tiene varios
    Club "1" --> "*" Miembro : tiene varios

    Grupo "1" --> "*" Miembro : tiene varios
    Grupo "1" --> "*" Lectura : tiene varias

    Lectura "1" --> "1" Libro : tiene un

    Miembro <|-- Alumno : (Alumno es un tipo de Miembro)
