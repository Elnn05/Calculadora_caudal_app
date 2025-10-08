
# Calculadora de Caudal para Tuberías

Esta aplicación web desarrollada con Streamlit permite calcular el caudal ($Q$) en tuberías a partir del diámetro y la velocidad del fluido. Es útil para ingenieros, estudiantes y profesionales que requieren realizar cálculos hidráulicos de manera rápida y sencilla.

## Características
- Interfaz intuitiva y fácil de usar.
- Visualización de la fórmula $Q = A \times v$.
- Ingreso de datos: diámetro de la tubería (cm) y velocidad del fluido (m/s).
- Cálculo automático del caudal en $m^3/s$.
- Mensajes de advertencia para entradas inválidas.

## Uso
1. Instala las dependencias ejecutando:
	```bash
	pip install -r requirements.txt
	```
2. Ejecuta la aplicación con:
	```bash
	streamlit run app.py
	```
3. Ingresa los valores requeridos y presiona "Calcular Caudal" para ver el resultado.

## Contexto
El cálculo de caudal es fundamental en el diseño y análisis de sistemas hidráulicos, permitiendo determinar el volumen de fluido que atraviesa una tubería en un tiempo determinado. Esta herramienta facilita el proceso y reduce errores manuales.
