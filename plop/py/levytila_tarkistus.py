import os
from datetime import datetime
import shutil

# Get current date and time
current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Get disk space for C: drive
disk_usage = shutil.disk_usage("C:\\")
total = disk_usage.total / (1024**3)  # Convert to GB
used = disk_usage.used / (1024**3)
free = disk_usage.free / (1024**3)

# Create output message
output = f"""Levytilan raportti
==================
Päivämäärä: {current_date}

C: asema:
- Yhteensä: {total:.2f} GB
- Käytetty: {used:.2f} GB
- Vapaa: {free:.2f} GB
- Käyttöaste: {(used/total*100):.1f}%
"""

# Create or append to levytilaraportti.txt
file_path = "levytilaraportti.txt"
mode = "a" if os.path.exists(file_path) else "w"

with open(file_path, mode, encoding="utf-8") as f:
    f.write(output + "\n")
