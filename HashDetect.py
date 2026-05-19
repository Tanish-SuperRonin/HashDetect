import re
from colorama import Fore, Style, init

init(autoreset=True)

HASH_DATABASE = {

    "MD5": {
        "pattern": r"^[a-fA-F0-9]{32}$",
        "strength": "Weak",
        "tools": [
            "Hashcat",
            "JohnTheRipper"
        ],
        "hashcat_mode": "-m 0"
    },

    "SHA1": {
        "pattern": r"^[a-fA-F0-9]{40}$",
        "strength": "Weak",
        "tools": [
            "Hashcat",
            "JohnTheRipper"
        ],
        "hashcat_mode": "-m 100"
    },

    "SHA256": {
        "pattern": r"^[a-fA-F0-9]{64}$",
        "strength": "Moderate",
        "tools": [
            "Hashcat"
        ],
        "hashcat_mode": "-m 1400"
    },

    "SHA512": {
        "pattern": r"^[a-fA-F0-9]{128}$",
        "strength": "Strong",
        "tools": [
            "Hashcat"
        ],
        "hashcat_mode": "-m 1700"
    },

    "BCRYPT": {
        "pattern": r"^\$2[aby]?\$.{56}$",
        "strength": "Very Strong",
        "tools": [
            "Hashcat",
            "JohnTheRipper"
        ],
        "hashcat_mode": "-m 3200"
    },

    "NTLM": {
        "pattern": r"^[a-fA-F0-9]{32}$",
        "strength": "Weak",
        "tools": [
            "Hashcat",
            "JohnTheRipper",
            "Mimikatz"
        ],
        "hashcat_mode": "-m 1000"
    },

    "Argon2": {
        "pattern": r"^\$argon2(id|i|d)\$.*",
        "strength": "Excellent",
        "tools": [
            "Hashcat"
        ],
        "hashcat_mode": "-m 32000"
    }
}


def detect_hash(hash_value):

    possible_hashes = []

    for hash_name, details in HASH_DATABASE.items():

        if re.fullmatch(details["pattern"], hash_value):
            possible_hashes.append(hash_name)

    return possible_hashes


def print_report(hash_type):

    details = HASH_DATABASE[hash_type]

    print(Fore.YELLOW + f"\nHash Type      : {hash_type}")
    print(Fore.YELLOW + f"Security Level : {details['strength']}")

    print(Fore.GREEN + "\nSuggested Tools:")

    for tool in details["tools"]:
        print(f"  [+] {tool}")

    print(Fore.MAGENTA + f"\nHashcat Mode   : {details['hashcat_mode']}")

    print(Fore.RED + "\n================================")


def main():

    print(Fore.RED + "\n================================")
    print(Fore.RED + "HashDetect - Hash Type Detection Tool")
    print(Fore.RED + "================================")

    hash_input = input(Fore.CYAN + "Enter hash value: ").strip()

    detected_hash = detect_hash(hash_input)

    if detected_hash:

        for hash_type in detected_hash:
            print_report(hash_type)

    else:
        print(Fore.RED + "\n[!] Unknown or Unsupported Hash Type")


if __name__ == "__main__":
    main()