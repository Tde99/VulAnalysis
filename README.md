__     _   _ _     _   _ _____ ____        _    ____  ___ _     ___ _______     __
 \ \   / / | | | |   | \ | | ____|  _ \      / \  | __ )_ _| |   |_ _|_   _\ \   / /
  \ \ / /| | | | |   |  \| |  _| | |_) |    / _ \ |  _ \| || |    | |  | |  \ \ / / 
   \ V / | |_| | |___| |\  | |___|  _ <    / ___ \| |_) | || |___ | |  | |   \ V /  
    \_/   \___/|_____|_| \_|_____|_| \_\  /_/   \_\____/___|_____|___| |_|    |_|   
     _    _   _    _    _  __   ______ ___ ____  
    / \  | \ | |  / \  | | \ \ / / ___|_ _/ ___| 
   / _ \ |  \| | / _ \ | |  \ V /\___ \ | \___ \ 
  / ___ \| |\  |/ ___ \| |___| |  ___) || | ___) |
 /_/   \_\_| \_/_/   \_\_____|_| |____/___|____/ 

VULNERABILITY-ANALYSIS (LYNIS WRAPPER)
A powerful Python-based security auditing tool that automates system hardening 
and vulnerability scans using the 'Lynis' engine. It provides a comprehensive 
analysis of the Linux kernel, configuration files, and software packages.

**Features**
* **System-Wide Auditing:** Scans the entire OS for misconfigurations and missing patches.
* **Security Hardening:** Provides a "Hardening Index" to measure system security performance.
* **Malware Detection:** Checks for rootkits and unauthorized binary modifications.
* **Compliance Testing:** Helps in verifying security standards (PCI-DSS, ISO27001).
* **One-Step Scan:** Simplifies the complex auditing process into a single executable command.

**Prerequisites**
The following tools must be installed on the host system:
* Python 3.x
* Lynis: The core security auditing engine.
* Figlet: (The script attempts to install this automatically via apt).

**Installation**

Clone the repository:
   * git clone https://github.com/Tde99/Vulnerability-Analysis.git

Navigate to the directory:
   * cd Vulnerability-Analysis

Make the script executable:
   * chmod +x vulnerability_analysis.py

**Usage**
System auditing requires full access to system configuration files. Run with sudo:

sudo python3 vulnerability_analysis.py

**How it Works:**
The script triggers `lynis audit system`, which performs an automated security scan across hundreds of checkpoints including boot procedures, kernel tuning, and network configurations.



**Important Notes:**
* **Root Privileges:** Absolute necessity for Lynis to access protected system directories.
* **Lynis Installation:** If not present, install via `sudo apt install lynis`.
* **Report Location:** Detailed logs can be found at `/var/log/lynis.log` after the scan.
