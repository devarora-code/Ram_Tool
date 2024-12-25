import psutil
import time

while True:
    def get_ram_usage():
        return psutil.virtual_memory().percent

    def terminate_high_ram_processes(threshold):
        for process in psutil.process_iter(['pid', 'name', 'memory_info']):
            try:
                if process.info['memory_info'].rss > threshold:
                    process_pid = process.info['pid']
                    print(f"Terminating process {process.info['name']} (PID: {process_pid}) due to high memory usage.")
                    psutil.Process(process_pid).terminate()
            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                pass

    def main():
        threshold =  70 * 1024 * 1024  
        while True:
            ram_usage = get_ram_usage()
            print(f"RAM Usage: {ram_usage}%")

            if ram_usage > 40:
                print("RAM usage exceeds 40%. Taking action...")
                terminate_high_ram_processes(threshold)

            time.sleep(20)

    if __name__ == "__main__":
        try:
            main()
        except KeyboardInterrupt:
            print("\nProgram terminated by user.")