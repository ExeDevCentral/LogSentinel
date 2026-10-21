<div align="center">

# LogSentinel • Deterministic Security Log Analyzer
### *Zero-Dependency Log Telemetry, Regular Expression Heuristics & Incident Classification Engine*

[![Python: 3.8+](https://img.shields.io/badge/Python-3.8%2B_Standard_Library-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Zero Dependencies](https://img.shields.io/badge/Dependencies-Zero_External_Overhead-success?style=for-the-badge)](https://docs.python.org/3/library/)
[![Complexity: O(N)](https://img.shields.io/badge/Algorithmic_Complexity-O(N)_Linear_Stream-orange?style=for-the-badge)](https://en.wikipedia.org/wiki/Streaming_algorithm)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg?style=for-the-badge)](https://opensource.org/licenses/MIT)

<p align="center">
  <b>A lightweight, high-performance security log auditing engine designed for air-gapped environments, minimal runtime overhead, and deterministic pattern classification without third-party dependencies.</b>
</p>

---

</div>

## 1. Abstract & System Taxonomy

System administrators operating in classified, air-gapped, or resource-constrained embedded edge nodes frequently cannot install heavy log ingestion daemons (e.g., Elastic Filebeat, Splunk Universal Forwarder) due to kernel dependency constraints or strict security posture requirements.

**LogSentinel** provides an autonomous, zero-dependency command-line parsing engine built entirely on **Python Standard Library primitives**:
- **Linear Stream Processing:** Evaluates structured and semi-structured syslog streams in single-pass $\mathcal{O}(N)$ computational complexity without buffering entire multi-gigabyte logs into resident memory.
- **Bi-Lingual Heuristic Tokenization:** Pre-compiled regular expression state machines correlate authentication failures and intrusion vectors across Spanish and English administrative dialects.
- **Statistical Threat Profiling:** Generates quantitative threat density metrics ($\Delta_{\text{threat}} = \frac{\sum E_{\text{malicious}}}{N_{\text{total}}}$) with precise source line referencing.

```
┌────────────────────────────────────────────────────────────────────────┐
│                        LOG STREAM INGESTION (O(N))                     │
│  [Syslog / Auth.log / EventLog] ──► [Chunked Text Stream Generator]   │
└──────────────────────────────────┬─────────────────────────────────────┘
                                   │
                                   ▼
┌────────────────────────────────────────────────────────────────────────┐
│               DETERMINISTIC REGULAR EXPRESSION PARSER                  │
│    • Auth Failures: `login failed`, `invalid credentials`, `locked`    │
│    • Intrusion Vectors: `unauthorized access`, `intrusion`, `blocked` │
│    • Multi-Lingual Regex Compilation via `re.compile()`                │
└──────────────────────────────────┬─────────────────────────────────────┘
                                   │
         ┌─────────────────────────┴─────────────────────────┐
         ▼                                                   ▼
┌──────────────────────────────────┐        ┌──────────────────────────────────┐
│      STATISTICAL DENSITY AUDIT   │        │     INCIDENT LINE TRACE REPORT   │
│   Quantitative Threat Frequency  │        │   Line-indexed Forensic Trace    │
│   Percentage Breach Calculation  │        │   Zero-Memory Resident Footprint │
└──────────────────────────────────┘        └──────────────────────────────────┘
```

---

## 2. Computational Complexity & Heuristic Automata

### 2.1. Memory and Time Envelope
By leveraging Python's streaming iterator pattern over file descriptors, LogSentinel enforces strict memory bounds:

$$\mathcal{M}_{\text{resident}} \le \mathcal{O}(1) \quad \text{relative to log file size } S$$
$$\mathcal{T}_{\text{execution}} = \mathcal{O}(N \cdot K)$$

Where $N$ is the number of ingested log records and $K$ is the bounded evaluation depth of the pre-compiled regular expression set.

### 2.2. Pattern Classification Taxonomy

| Incident Class | Regex Signature Vectors | Forensic Significance |
| :--- | :--- | :--- |
| **Authentication Anomaly** | `authentication failed`, `invalid credentials`, `account locked` | Precursor to brute-force credential stuffing |
| **Access Control Breach** | `unauthorized access`, `acceso no autorizado`, `forbidden` | Privilege escalation or directory traversal attempts |
| **Perimeter Rejection** | `intrusion attempt`, `ip bloqueada`, `connection dropped` | Port scan sweeps or firewall drop notifications |

---

## 3. Systems Directory Hierarchy

```text
LogSentinel/
├── log_analyzer.py          # Monolithic single-file execution entrypoint
├── sample_security_log.txt  # Calibrated security event validation dataset
├── requirements.txt         # Dependency manifest (Strictly empty: standard library only)
├── README.md               # Primary technical specification (English)
├── README_EN.md            # Concise quickstart reference
└── src/                    # Modular engine architecture
    ├── main.py             # Orchestration CLI wrapper
    ├── parser.py           # Stream parser and token evaluator
    └── rules.py            # Pre-compiled regular expression rule definitions
```

---

## 4. Operational Execution & Lifecycle

### Prerequisites
- **Python**: $\ge 3.8$ (Compatible across all POSIX and Windows NT platforms)
- **External Dependencies**: Zero ($0$)

### Execution Commands
```bash
# Clone the repository
git clone https://github.com/ExeDevCentral/LogSentinel.git
cd LogSentinel

# Analyze target log file
python log_analyzer.py path/to/auth.log

# Execute verification against included test telemetry
python log_analyzer.py sample_security_log.txt
```

### Typical Forensic Telemetry Output
```text
=== LOGSENTINEL SECURITY AUDIT REPORT ===
Analyzed Target: sample_security_log.txt
Total Records Ingested: 14

[!] AUTHENTICATION FAILURES DETECTED:
    Total Incidents: 5
    Line 3: [ERROR] 2023-10-01 08:16:00 Login failed for user: admin from IP 192.168.1.100
    ...

[!] ACCESS VIOLATIONS & SUSPICIOUS EVENTS:
    Total Incidents: 4
    Line 7: [WARNING] 2023-10-01 08:25:00 Unauthorized access attempt from IP 10.0.0.50
    ...

STATISTICAL INCIDENT SUMMARY:
    Total Threats Identified: 9
    Threat Density Ratio:     64.29%

=== END FORENSIC AUDIT ===
```

---

## 5. License

Distributed under the **MIT License**. Engineered for defensive log auditing and air-gapped system diagnostics.

<div align="center">
  <sub>Engineered by <a href="https://github.com/ExeDevCentral">ExeDevCentral</a>.</sub>
</div>
