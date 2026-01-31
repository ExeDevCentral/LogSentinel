# LogSentinel - Security Log Analyzer

A simple and effective log file analyzer for detecting basic security threats.

## 🚀 Features

- **Failed login detection**: Identifies patterns like "login failed", "authentication failed", "invalid credentials"
- **Suspicious access detection**: Finds patterns like "unauthorized access", "suspicious access", "intrusion attempt", "blocked ip"
- **Clear and detailed reporting**: Shows a summary with counts, percentages, and specific lines where threats were found
- **Easy to use**: Just run the script with a log file as a parameter
- **No external dependencies**: Uses only Python standard libraries

## 📋 Requirements

- Python 3.6 or higher
- No external dependencies required

## 🛠️ Installation

1. Clone the repository:
```bash
git clone https://github.com/ExeDevCentral/LogSentinel.git
cd LogSentinel
```

2. Make sure you have Python installed:
```bash
python --version
```

## 📖 Usage

### Basic analysis
```bash
python log_analyzer.py path/to/log/file.log
```

### Example with test file
```bash
python log_analyzer.py sample_security_log.txt
```

## 📊 Program Output

The program generates a report like this:

```
=== LOG ANALYSIS REPORT ===
Analyzed file: sample_security_log.txt
Total lines processed: 14

🔐 FAILED LOGIN ATTEMPTS:
   Total detected: 5
   Line 3: [ERROR] 2023-10-01 08:16:00 Login failed for user: hacker123 from IP 192.168.1.100
   ...

🚨 SUSPICIOUS ACCESSES:
   Total detected: 4
   Line 7: [WARNING] 2023-10-01 08:25:00 Unauthorized access detected from IP 10.0.0.50
   ...

📊 SUMMARY:
   Total threats detected: 9
   Percentage of lines with threats: 64.29%

=== END OF REPORT ===
```

## 🏗️ Project Structure

```
LogSentinel/
├── log_analyzer.py          # Main analyzer script
├── sample_security_log.txt  # Sample log file with security events
├── requirements.txt         # Dependencies (empty, uses only standard libraries)
├── README.md               # This file (Spanish)
├── README_EN.md            # This file (English)
└── src/                    # Additional source code (modular version)
    ├── main.py
    ├── parser.py
    └── rules.py
```

## 🔍 Detected Patterns

### Failed Login Attempts
- "login failed"
- "autenticación fallida"
- "authentication failed"
- "invalid credentials"
- "credenciales inválidas"
- "account locked"

### Suspicious Accesses
- "acceso no autorizado"
- "unauthorized access"
- "acceso sospechoso"
- "suspicious access"
- "intento de intrusión"
- "intrusion attempt"
- "ip bloqueada"
- "blocked ip"

## 🤝 Contributing

1. Fork the project
2. Create a feature branch (`git checkout -b feature/NewFeature`)
3. Commit your changes (`git commit -am 'Add new feature'`)
4. Push to the branch (`git push origin feature/NewFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👨‍💻 Author

**ExeDevCentral** - [GitHub](https://github.com/ExeDevCentral)

## 🙏 Acknowledgments

- Inspired by enterprise log analysis tools
- Developed for learning and practical use in production environments

---

*Developed with ❤️ in Argentina*
