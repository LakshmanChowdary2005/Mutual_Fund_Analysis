import subprocess

scripts = [
    "data_ingestion.py",
    "clean_nav_history.py",
    "clean_transactions.py",
    "clean_performance.py",
    "load_to_sqlite.py"
]

success = True

for script in scripts:
    print(f"\n{'='*60}")
    print(f"Running {script}")
    print(f"{'='*60}")

    try:
        subprocess.run(["python", script], check=True)
        print(f"{script} completed successfully.")
    except subprocess.CalledProcessError:
        print(f"{script} failed.")
        success = False
        break

if success:
    print("\nETL Pipeline Completed Successfully!")
else:
    print("\nETL Pipeline Failed.")