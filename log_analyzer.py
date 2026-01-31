#!/usr/bin/env python3
"""
Analizador simple de logs para detectar intentos fallidos de login y accesos sospechosos.
"""

import sys
import re

def detectar_patron(linea, patrones):
    """
    Verifica si una línea contiene alguno de los patrones dados.
    """
    for patron in patrones:
        if re.search(patron, linea, re.IGNORECASE):
            return True
    return False

def analizar_log(ruta_archivo):
    """
    Lee el archivo de log y detecta intentos fallidos de login y accesos sospechosos.
    """
    # Patrones para detectar
    patrones_login_fallido = [
        r'login failed',
        r'autenticación fallida',
        r'authentication failed',
        r'invalid credentials',
        r'credenciales inválidas'
    ]

    patrones_acceso_sospechoso = [
        r'acceso no autorizado',
        r'unauthorized access',
        r'acceso sospechoso',
        r'suspicious access',
        r'intento de intrusión',
        r'intrusion attempt',
        r'ip bloqueada',
        r'blocked ip'
    ]

    # Contadores
    intentos_login_fallidos = []
    accesos_sospechosos = []
    total_lineas = 0

    try:
        with open(ruta_archivo, 'r', encoding='utf-8') as archivo:
            for numero_linea, linea in enumerate(archivo, 1):
                total_lineas += 1
                linea = linea.strip()

                if detectar_patron(linea, patrones_login_fallido):
                    intentos_login_fallidos.append((numero_linea, linea))
                elif detectar_patron(linea, patrones_acceso_sospechoso):
                    accesos_sospechosos.append((numero_linea, linea))

    except FileNotFoundError:
        print(f"Error: No se encontró el archivo '{ruta_archivo}'")
        return None
    except Exception as e:
        print(f"Error al leer el archivo: {e}")
        return None

    return {
        'total_lineas': total_lineas,
        'login_fallidos': intentos_login_fallidos,
        'accesos_sospechosos': accesos_sospechosos
    }

def generar_reporte(resultados, ruta_archivo):
    """
    Genera un reporte claro con los resultados del análisis.
    """
    print("=== REPORTE DE ANÁLISIS DE LOGS ===")
    print(f"Archivo analizado: {ruta_archivo}")
    print(f"Total de líneas procesadas: {resultados['total_lineas']}")
    print()

    print("🔐 INTENTOS FALLIDOS DE LOGIN:")
    if resultados['login_fallidos']:
        print(f"   Total detectados: {len(resultados['login_fallidos'])}")
        for numero_linea, linea in resultados['login_fallidos'][:10]:  # Mostrar máximo 10
            print(f"   Línea {numero_linea}: {linea}")
        if len(resultados['login_fallidos']) > 10:
            print(f"   ... y {len(resultados['login_fallidos']) - 10} más")
    else:
        print("   Ninguno detectado")
    print()

    print("🚨 ACCESOS SOSPECHOSOS:")
    if resultados['accesos_sospechosos']:
        print(f"   Total detectados: {len(resultados['accesos_sospechosos'])}")
        for numero_linea, linea in resultados['accesos_sospechosos'][:10]:  # Mostrar máximo 10
            print(f"   Línea {numero_linea}: {linea}")
        if len(resultados['accesos_sospechosos']) > 10:
            print(f"   ... y {len(resultados['accesos_sospechosos']) - 10} más")
    else:
        print("   Ninguno detectado")
    print()

    # Resumen
    total_amenazas = len(resultados['login_fallidos']) + len(resultados['accesos_sospechosos'])
    print("📊 RESUMEN:")
    print(f"   Total de amenazas detectadas: {total_amenazas}")
    if resultados['total_lineas'] > 0:
        porcentaje = (total_amenazas / resultados['total_lineas']) * 100
        print(f"   Porcentaje de líneas con amenazas: {porcentaje:.2f}%")
    print()
    print("=== FIN DEL REPORTE ===")

def main():
    if len(sys.argv) != 2:
        print("Uso: python log_analyzer.py <ruta_al_archivo_de_log>")
        print("Ejemplo: python log_analyzer.py logs/ejemplo.log")
        sys.exit(1)

    ruta_archivo = sys.argv[1]
    resultados = analizar_log(ruta_archivo)

    if resultados:
        generar_reporte(resultados, ruta_archivo)
    else:
        sys.exit(1)

if __name__ == "__main__":
    main()
