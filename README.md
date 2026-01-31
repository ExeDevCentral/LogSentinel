# LogSentinel - Analizador de Logs de Seguridad

Un analizador simple y efectivo de archivos de log para detectar amenazas básicas de seguridad.

## 🚀 Características

- **Detección de logins fallidos**: Identifica patrones como "login failed", "autenticación fallida", "invalid credentials"
- **Detección de accesos sospechosos**: Encuentra patrones como "acceso no autorizado", "acceso sospechoso", "intento de intrusión", "ip bloqueada"
- **Reportes claros y detallados**: Muestra un resumen con conteos, porcentajes y líneas específicas donde se encontraron amenazas
- **Fácil de usar**: Solo ejecutá el script con un archivo de log como parámetro
- **Sin dependencias externas**: Usa solo librerías estándar de Python

## 📋 Requisitos

- Python 3.6 o superior
- No se requieren dependencias externas

## 🛠️ Instalación

1. Cloná el repositorio:
```bash
git clone https://github.com/ExeDevCentral/LogSentinel.git
cd LogSentinel
```

2. Asegurate de tener Python instalado:
```bash
python --version
```

## 📖 Uso

### Análisis básico
```bash
python log_analyzer.py ruta/al/archivo/log.log
```

### Ejemplo con archivo de prueba
```bash
python log_analyzer.py sample_security_log.txt
```

## 📊 Salida del Programa

El programa genera un reporte como este:

```
=== REPORTE DE ANÁLISIS DE LOGS ===
Archivo analizado: sample_security_log.txt
Total de líneas procesadas: 14

🔐 INTENTOS FALLIDOS DE LOGIN:
   Total detectados: 5
   Línea 3: [ERROR] 2023-10-01 08:16:00 Login failed for user: hacker123 from IP 192.168.1.100
   ...

🚨 ACCESOS SOSPECHOSOS:
   Total detectados: 4
   Línea 7: [WARNING] 2023-10-01 08:25:00 Acceso no autorizado detectado desde IP 10.0.0.50
   ...

📊 RESUMEN:
   Total de amenazas detectadas: 9
   Porcentaje de líneas con amenazas: 64.29%

=== FIN DEL REPORTE ===
```

## 🏗️ Estructura del Proyecto

```
LogSentinel/
├── log_analyzer.py          # Script principal del analizador
├── sample_security_log.txt  # Archivo de log de ejemplo con eventos de seguridad
├── requirements.txt         # Dependencias (vacío, usa solo librerías estándar)
├── README.md               # Este archivo (español)
├── README_EN.md            # Versión en inglés
└── src/                    # Código fuente adicional (versión modular)
    ├── main.py
    ├── parser.py
    └── rules.py
```

## 🔍 Patrones Detectados

### Intentos de Login Fallidos
- "login failed"
- "autenticación fallida"
- "authentication failed"
- "invalid credentials"
- "credenciales inválidas"
- "account locked"

### Accesos Sospechosos
- "acceso no autorizado"
- "unauthorized access"
- "acceso sospechoso"
- "suspicious access"
- "intento de intrusión"
- "intrusion attempt"
- "ip bloqueada"
- "blocked ip"

## 🤝 Contribuyendo

1. Hacé fork del proyecto
2. Creá una rama para tu feature (`git checkout -b feature/NuevaCaracteristica`)
3. Commiteá tus cambios (`git commit -am 'Agrego nueva característica'`)
4. Pusheá a la rama (`git push origin feature/NuevaCaracteristica`)
5. Abrí un Pull Request

## 📝 Licencia

Este proyecto está bajo la Licencia MIT - ver el archivo [LICENSE](LICENSE) para más detalles.

## 👨‍💻 Autor

**ExeDevCentral** - [GitHub](https://github.com/ExeDevCentral)

## 🙏 Agradecimientos

- Inspirado en herramientas de análisis de logs empresariales
- Desarrollado para aprendizaje y uso práctico en entornos de producción

---

*Desarrollado con ❤️ en Argentina*
