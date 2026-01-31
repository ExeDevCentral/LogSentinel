#!/usr/bin/env python3
"""
Módulo de parseo de logs.
Responsable de leer y analizar archivos de log.
"""

import re
from collections import defaultdict

class LogParser:
    def __init__(self):
        self.patterns = {
            'ERROR': re.compile(r'\[ERROR\]'),
            'WARNING': re.compile(r'\[WARNING\]'),
            'INFO': re.compile(r'\[INFO\]'),
        }

    def parse_file(self, file_path):
        """
        Parsea el archivo de log y devuelve un diccionario con conteos.
        """
        counts = defaultdict(int)
        total_lines = 0
        lines = []

        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                for line in file:
                    total_lines += 1
                    line = line.strip()
                    lines.append(line)
                    for level, pattern in self.patterns.items():
                        if pattern.search(line):
                            counts[level] += 1
        except FileNotFoundError:
            raise FileNotFoundError(f"Archivo '{file_path}' no encontrado.")
        except Exception as e:
            raise Exception(f"Error al leer el archivo: {e}")

        return counts, total_lines, lines

    def filter_by_level(self, lines, level):
        """
        Filtra líneas por nivel de log.
        """
        pattern = self.patterns.get(level.upper())
        if not pattern:
            return []
        return [line for line in lines if pattern.search(line)]
