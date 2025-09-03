import analyzer

df = analyzer.load_logs()
print(analyzer.event_summary(df))
print(analyzer.get_cpu_trend(df))
print(analyzer.top_process(df))