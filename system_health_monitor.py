import psutil
import time

# Thresholds
CPU_THRESHOLD = 80
MEMORY_THRESHOLD = 80
DISK_THRESHOLD = 80

def check_cpu_usage():
    usage = psutil.cpu_percent(interval=1)
    if usage > CPU_THRESHOLD:
        print(f"ALERT: High CPU usage detected: {usage}%")
    return usage

def check_memory_usage():
    memory = psutil.virtual_memory()
    usage = memory.percent
    if usage > MEMORY_THRESHOLD:
        print(f"ALERT: High memory usage detected: {usage}%")
    return usage

def check_disk_usage():
    disk = psutil.disk_usage('/')
    usage = disk.percent
    if usage > DISK_THRESHOLD:
        print(f"ALERT: High disk usage detected: {usage}%")
    return usage

def check_running_processes():
    processes = [p.info for p in psutil.process_iter(attrs=['pid', 'name', 'username'])]
    print(f"Running processes: {len(processes)}")
    return processes

def monitor_system():
    while True:
        print("System Health Check:")
        cpu_usage = check_cpu_usage()
        memory_usage = check_memory_usage()
        disk_usage = check_disk_usage()
        running_processes = check_running_processes()
        print(f"CPU Usage: {cpu_usage}%")
        print(f"Memory Usage: {memory_usage}%")
        print(f"Disk Usage: {disk_usage}%")
        time.sleep(60)

if __name__ == "__main__":
    monitor_system()
