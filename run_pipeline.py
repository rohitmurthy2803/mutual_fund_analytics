"""
Master ETL pipeline execution script.

Tasks:
- Execute ingestion process
- Run cleaning scripts
- Load cleaned data into database
- Automate end-to-end ETL workflow
"""
import subprocess

scripts = [
    "live_nav_fetch.py",
    "data_ingestion.py",
    "clean_nav_history.py",
    "clean_investor_transactions.py",
    "clean_scheme_performance.py",
    "load_data.py"
]

for script in scripts:
    print(f"Running {script}...")
    subprocess.run(["python", script], check=True)

print("ETL pipeline completed successfully.")