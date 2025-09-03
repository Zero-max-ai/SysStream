import json
import pandas as pd
from  pathlib import Path
from datetime import datetime

def load_logs(date=None):
    # logs will be taken by the date and by default it would be the curernt datelog
    log_dir = Path('logs')
    if not date:
        date = datetime.now().date()
    log_file = log_dir / f"logs_{date}.json"

    if not log_file.exists():
        raise FileNotFoundError(f"No log file found for {date}")
    
    with open(log_file, 'r') as f:
        data = json.load(f)
    return pd.DataFrame(data)


def event_summary(df: pd.DataFrame):
    # here we will be generating the summary
    return {
        "Total Records ": len(df),
        "Avg CPU (%) ": df["cpu"].mean().round(2),
        "Avg Memory (%) ": df["memory"].mean().round(2),
        "Max Disk Usage (%) ": df["disk"].max(),
    }

def get_cpu_trend(df: pd.DataFrame):
    # extracting cpu usage over time for plotting

    df["timeStamp"] = pd.to_datetime(df["timeStamp"])
    return df[["timeStamp", "cpu"]]

def top_process(df: pd.DataFrame):
    process_list = []
    for procs in df["top_processes"]:
        for proc in procs:
            if proc["name"]:
                process_list.append((proc["name"], proc["cpu_percent"]))
    proc_df = pd.DataFrame(process_list, columns=["process_name", "cpu_percent"])
    # proc_df = pd.Series(process_list).value_counts().reset_index()
    # proc_df.columns = ["process_name", "count"]
    return proc_df.groupby("process_name")["cpu_percent"].mean().sort_values(ascending=False).head(10)