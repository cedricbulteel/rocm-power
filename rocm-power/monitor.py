import subprocess
import time
import threading

class GpuMonitor:
    def __init__(self, output_file="gpu_data.csv", interval=0.1):
        self.output_file = output_file
        self.interval = interval
        self.monitoring = False
        self.thread = None

    def _monitor(self):
        """Internal method to continuously log GPU power usage."""
        with open(self.output_file, "a") as f:
            while self.monitoring:
                result = subprocess.run(["rocm-smi", "-P", "--csv"], capture_output=True, text=True)
                f.write(result.stdout)
                time.sleep(self.interval)

    def start(self):
        """Start monitoring in a separate thread."""
        if not self.monitoring:
            self.monitoring = True
            self.thread = threading.Thread(target=self._monitor, daemon=True)
            self.thread.start()
            print("GPU monitoring started...")

    def stop(self):
        """Stop monitoring."""
        if self.monitoring:
            self.monitoring = False
            self.thread.join()
            print("GPU monitoring stopped.")

