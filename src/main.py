#!/usr/bin/env python3
"""
Punto de entrada principal para el analizador de logs LogSentinel.
"""

import sys
import os

# Agregar el directorio actual al path para importar módulos locales
current_dir = os.path.dirname(os.path.abspath(__file__))
if current_dir not in sys.path:
    sys.path.insert(0, current_dir)

from parser import LogParser
from rules import LogRules

def generate_report(counts, total_lines, alerts, file_path, output_dir='reports'):
    """
    Genera un reporte en un archivo de texto.
    """
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    report_path = os.path.join(output_dir, f'report_{os.path.basename(file_path)}.txt')

    with open(report_path, 'w', encoding='utf-8') as f:
        f.write("=== Reporte de Análisis de Logs ===\n")
        f.write(f"Archivo analizado: {file_path}\n")
        f.write(f"Total de líneas: {total_lines}\n\n")
        f.write("Conteo de mensajes:\n")
        for level, count in counts.items():
            f.write(f"  {level}: {count}\n")
        f.write("\nPorcentajes:\n")
        if total_lines > 0:
            for level, count in counts.items():
                percentage = (count / total_lines) * 100
                f.write(f"  {level}: {percentage:.2f}%\n")
        f.write("\nAlertas detectadas:\n")
        for rule, lines in alerts.items():
            f.write(f"  {rule}: {len(lines)} ocurrencias\n")
            for line in lines[:5]:  # Mostrar máximo 5 líneas por regla
                f.write(f"    - {line}\n")
        f.write("\n=== Fin del Reporte ===\n")

    print(f"Reporte generado: {report_path}")

def main():
    if len(sys.argv) != 2:
        print("Uso: python src/main.py <ruta_al_archivo_de_log>")
        sys.exit(1)

    file_path = sys.argv[1]

    # Inicializar componentes
    parser = LogParser()
    rules = LogRules()

    try:
        # Parsear el log
        counts, total_lines, lines = parser.parse_file(file_path)

        # Aplicar reglas
        alerts = rules.apply_rules(lines)

        # Generar reporte
        generate_report(counts, total_lines, alerts, file_path)

        print("Análisis completado exitosamente.")

    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
