import psutil, time, json
from datetime import datetime
from pathlib import Path

# init path
log_dir = Path('logs')
log_dir.mkdir(exist_ok=True)

"""
    creating file for daily basis,
    storing events,
    appending data in the file,
"""
while True:
    log_file = log_dir / f"logs_{datetime.now().date()}.json"
    event = {
        "timeStamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "cpu": psutil.cpu_percent(),
        "memory": psutil.virtual_memory().percent,
        "disk": psutil.disk_usage('/').percent,
        "top_processes": [p.info for p in psutil.process_iter(['pid', 'name', 'cpu_percent'])][:20]
    }

    with open(log_file, "a") as f:
        f.write(json.dumps(event) + ',\n')
    time.sleep(10) # placing interval