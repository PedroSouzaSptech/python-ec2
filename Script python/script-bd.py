import psutil
import time
import subprocess
from datetime import datetime

atualizador = 5  # Número de repetições

i = 0

while i < atualizador:

    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    cpu_percent = psutil.cpu_percent(interval=1)

    mem = psutil.virtual_memory()
    total_ram = mem.total
    used_ram = mem.used
    free_ram = mem.available

    disk = psutil.disk_usage('/')
    total_storage = disk.total
    used_storage = disk.used
    free_storage = disk.free

    print(f"{current_time} - CPU usada: {cpu_percent}%")
    print(f"{current_time} - Total de RAM: {total_ram / (1024 ** 3):.2f} GB")
    print(f"{current_time} - RAM usada: {used_ram / (1024 ** 3):.2f} GB")
    print(f"{current_time} - RAM livre: {free_ram / (1024 ** 3):.2f} GB")
    print(f"{current_time} - Armazenamento total: {total_storage / (1024 ** 3):.2f} GB")
    print(f"{current_time} - Armazenamento usado: {used_storage / (1024 ** 3):.2f} GB")
    print(f"{current_time} - Armazenamento livre: {free_storage / (1024 ** 3):.2f} GB")

    time.sleep(120)

