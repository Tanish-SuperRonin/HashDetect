# HashDetect

HashDetect is a lightweight Python-based CLI utility designed for VAPT and cybersecurity workflows. It identifies cryptographic hash types, evaluates their security strength, and suggests password auditing tools along with corresponding Hashcat modes.

---

## Features

* Detects common cryptographic hash types
* Supports multiple hash matches (e.g., MD5 & NTLM)
* Displays security strength analysis
* Suggests password auditing/cracking tools
* Provides Hashcat mode references
* Colored CLI output for better readability

---

## Supported Hash Types

| Hash Type | Status    |
| --------- | --------- |
| MD5       | Supported |
| SHA1      | Supported |
| SHA256    | Supported |
| SHA512    | Supported |
| NTLM      | Supported |
| BCRYPT    | Supported |
| Argon2    | Supported |

---

## Technologies Used

* Python 3
* Regular Expressions (`re`)
* Colorama

---

## Installation

Clone the repository:

```bash
git clone https://github.com/Tanish-SuperRonin/HashDetect
cd hashdetect
```

---

## Usage

Run the tool:

```bash
python main.py
```

Enter a hash when prompted:

```text
Enter hash value:
5f4dcc3b5aa765d61d8327deb882cf99
```

---

## Example Output

```text
================================
HashDetect - Hash Type Detection Tool
================================

Hash Type      : MD5
Security Level : Weak

Suggested Tools:
  [+] Hashcat
  [+] JohnTheRipper

Hashcat Mode   : -m 0

================================

Hash Type      : NTLM
Security Level : Weak

Suggested Tools:
  [+] Hashcat
  [+] JohnTheRipper
  [+] Mimikatz

Hashcat Mode   : -m 1000

================================
```

---

## Project Structure

```text
hashdetect/
│
├── main.py
├── requirements.txt
└── README.md
```

---

## Educational Purpose

HashDetect is intended for:

* educational purposes
* cybersecurity learning
* authorized VAPT/security assessments

Do not use this tool for unauthorized activities.

---

## Future Improvements

* Batch hash analysis
* File input support
* Export reports
* Additional hash formats
* Confidence scoring system
* Hash metadata analysis

---

## Author

Tanish Shah
