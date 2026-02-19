#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
GESTOR DE TAREAS - VERSIÓN 1
Aprenderás: listas, menús, bucles, condiciones
"""

def mostrar_menu():
    """Muestra las opciones disponibles"""
    print("\n" + "="*40)
    print("           GESTOR DE TAREAS")
    print("="*40)
    print("1. Ver todas las tareas")
    print("2. Añadir nueva tarea")
    print("3. Completar tarea")
    print("4. Eliminar tarea")
    print("5. Salir")
    print("="*40)

def ver_tareas(tareas):
    """Muestra la lista de tareas con su estado"""
    if not tareas:
        print("\n📋 No hay tareas pendientes. ¡Añade alguna!")
        return
    
    print("\n📋 TUS TAREAS:")
    for i, tarea in enumerate(tareas, 1):
        estado = "✅" if tarea['completada'] else "❌"
        print(f"{i}. {estado} {tarea['nombre']}")

def añadir_tarea(tareas):
    """Añade una nueva tarea"""
    nombre = input("\n📝 Nombre de la tarea: ")
    if nombre:  # Si no está vacío
        tareas.append({'nombre': nombre, 'completada': False})
        print(f"✅ Tarea '{nombre}' añadida correctamente")
    else:
        print("❌ El nombre no puede estar vacío")

def completar_tarea(tareas):
    """Marca una tarea como completada"""
    ver_tareas(tareas)
    if not tareas:
        return
    
    try:
        num = int(input("\n📌 Número de tarea a completar: "))
        if 1 <= num <= len(tareas):
            tareas[num-1]['completada'] = True
            print(f"✅ Tarea {num} completada. ¡Bien hecho!")
        else:
            print("❌ Número de tarea no válido")
    except ValueError:
        print("❌ Por favor, introduce un número válido")

def eliminar_tarea(tareas):
    """Elimina una tarea de la lista"""
    ver_tareas(tareas)
    if not tareas:
        return
    
    try:
        num = int(input("\n🗑️  Número de tarea a eliminar: "))
        if 1 <= num <= len(tareas):
            tarea_eliminada = tareas.pop(num-1)
            print(f"✅ Tarea '{tarea_eliminada['nombre']}' eliminada")
        else:
            print("❌ Número de tarea no válido")
    except ValueError:
        print("❌ Por favor, introduce un número válido")

def main():
    """Función principal del programa"""
    tareas = []  # Aquí guardaremos las tareas
    
    while True:
        mostrar_menu()
        opcion = input("👉 Elige una opción (1-5): ")
        
        if opcion == "1":
            ver_tareas(tareas)
        
        elif opcion == "2":
            añadir_tarea(tareas)
        
        elif opcion == "3":
            completar_tarea(tareas)
        
        elif opcion == "4":
            eliminar_tarea(tareas)
        
        elif opcion == "5":
            print("\n👋 ¡Hasta luego! Sigue organizado/a")
            break
        
        else:
            print("❌ Opción no válida. Intenta del 1 al 5")
        
        # Pequeña pausa para que el usuario lea el mensaje
        input("\n⏎ Presiona Enter para continuar...")

if __name__ == "__main__":
    main()