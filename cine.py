# Programa de gestión de venta de boletos para MovieTime
import csv
import os
from datetime import datetime

FUNCIONES_FILE = 'funciones.csv'
VENTAS_FILE = 'ventas.csv'

def cargar_funciones():
	funciones = []
	if os.path.exists(FUNCIONES_FILE):
		with open(FUNCIONES_FILE, newline='', encoding='utf-8') as f:
			reader = csv.DictReader(f)
			for row in reader:
				row['precio'] = float(row['precio'])
				funciones.append(row)
	return funciones

def guardar_funcion(funcion):
	existe = os.path.exists(FUNCIONES_FILE)
	with open(FUNCIONES_FILE, 'a', newline='', encoding='utf-8') as f:
		fieldnames = ['codigo', 'pelicula', 'hora', 'precio']
		writer = csv.DictWriter(f, fieldnames=fieldnames)
		if not existe:
			writer.writeheader()
		writer.writerow(funcion)

def cargar_ventas():
	ventas = []
	if os.path.exists(VENTAS_FILE):
		with open(VENTAS_FILE, newline='', encoding='utf-8') as f:
			reader = csv.DictReader(f)
			for row in reader:
				row['cantidad'] = int(row['cantidad'])
				row['total'] = float(row['total'])
				ventas.append(row)
	return ventas

def guardar_venta(venta):
	existe = os.path.exists(VENTAS_FILE)
	with open(VENTAS_FILE, 'a', newline='', encoding='utf-8') as f:
		fieldnames = ['fecha', 'codigo', 'cantidad', 'total']
		writer = csv.DictWriter(f, fieldnames=fieldnames)
		if not existe:
			writer.writeheader()
		writer.writerow(venta)

def registrar_funcion():
	print('\n--- Registrar nueva función ---')
	codigo = input('Código de la función: ').strip()
	funciones = cargar_funciones()
	if any(f['codigo'] == codigo for f in funciones):
		print('Ya existe una función con ese código.')
		return
	pelicula = input('Nombre de la película: ').strip()
	hora = input('Hora (HH:MM): ').strip()
	while True:
		try:
			precio = float(input('Precio del boleto: '))
			if precio <= 0:
				print('El precio debe ser mayor a 0.')
				continue
			break
		except ValueError:
			print('Precio inválido.')
	funcion = {'codigo': codigo, 'pelicula': pelicula, 'hora': hora, 'precio': precio}
	guardar_funcion(funcion)
	print('Función registrada exitosamente.')

def listar_funciones():
	print('\n--- Funciones disponibles ---')
	funciones = cargar_funciones()
	if not funciones:
		print('No hay funciones registradas.')
		return
	print(f"{'Código':<10}{'Película':<30}{'Hora':<10}{'Precio':<10}")
	for f in funciones:
		print(f"{f['codigo']:<10}{f['pelicula']:<30}{f['hora']:<10}{f['precio']:<10.2f}")

def vender_boletos():
	print('\n--- Venta de boletos ---')
	funciones = cargar_funciones()
	if not funciones:
		print('No hay funciones disponibles.')
		return
	codigo = input('Código de la función: ').strip()
	funcion = next((f for f in funciones if f['codigo'] == codigo), None)
	if not funcion:
		print('Función inexistente.')
		return
	while True:
		try:
			cantidad = int(input('Cantidad de boletos: '))
			if cantidad <= 0:
				print('Cantidad inválida. Debe ser mayor a 0.')
				continue
			break
		except ValueError:
			print('Cantidad inválida.')
	total = cantidad * funcion['precio']
	print(f"Total a pagar: ${total:.2f}")
	venta = {
		'fecha': datetime.now().strftime('%Y-%m-%d'),
		'codigo': codigo,
		'cantidad': cantidad,
		'total': total
	}
	guardar_venta(venta)
	print('Venta registrada exitosamente.')

def resumen_ventas():
	print('\n--- Resumen de ventas del día ---')
	ventas = cargar_ventas()
	hoy = datetime.now().strftime('%Y-%m-%d')
	ventas_hoy = [v for v in ventas if v['fecha'] == hoy]
	total_boletos = sum(v['cantidad'] for v in ventas_hoy)
	total_dinero = sum(v['total'] for v in ventas_hoy)
	print(f"Boletos vendidos hoy: {total_boletos}")
	print(f"Dinero recaudado hoy: ${total_dinero:.2f}")

def menu():
	while True:
		print('\n--- MovieTime ---')
		print('1. Registrar función nueva')
		print('2. Listar funciones disponibles')
		print('3. Vender boletos')
		print('4. Resumen de ventas del día')
		print('5. Salir')
		opcion = input('Seleccione una opción: ').strip()
		if opcion == '1':
			registrar_funcion()
		elif opcion == '2':
			listar_funciones()
		elif opcion == '3':
			vender_boletos()
		elif opcion == '4':
			resumen_ventas()
		elif opcion == '5':
			print('¡Hasta luego!')
			break
		else:
			print('Opción inválida.')

if __name__ == '__main__':
	menu()
