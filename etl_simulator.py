import time
import random
import json
from datetime import datetime

# ANSI Colors for "Interactive" Feel
class Colors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'

def log(msg, type="INFO"):
    timestamp = datetime.now().strftime("%H:%M:%S")
    color = Colors.BLUE
    if type == "SUCCESS": color = Colors.GREEN
    if type == "WARN": color = Colors.WARNING
    if type == "ERROR": color = Colors.FAIL
    if type == "HEADER": color = Colors.HEADER
    
    print(f"{Colors.BOLD}[{timestamp}] {color}{type}:{Colors.ENDC} {msg}")
    time.sleep(0.8) # Simulate processing time

def simulate_etl():
    print(f"{Colors.HEADER}{Colors.BOLD}")
    print("╔════════════════════════════════════════════════════╗")
    print("║   UKG PRO WFM -> BIGQUERY ETL SIMULATOR v2.0   ║")
    print("╚════════════════════════════════════════════════════╝")
    print(f"{Colors.ENDC}")
    
    # STEP 1: EXTRACT
    log("Initiating API Connection to UKG Data Hub...", "HEADER")
    log("Endpoint: /api/v1/commons/people", "INFO")
    time.sleep(1)
    
    people_count = random.randint(150, 500)
    log(f"Extracted {people_count} person records (Raw JSON)", "SUCCESS")
    
    log("Endpoint: /api/v1/timekeeping/punches", "INFO")
    punch_count = people_count * 4
    log(f"Extracted {punch_count} punch records (Raw JSON)", "SUCCESS")
    
    # STEP 2: TRANSFORM
    log("Starting Transformation Layer...", "HEADER")
    
    # Simulate finding a data quality issue
    bad_record = {
        "person_id": "KG-8842",
        "punch_dt": "2026-02-03T08:00:00Z",
        "punch_type": "IN",
        "duration": None # BAD DATA
    }
    
    log(f"Processing Batch #1024...", "INFO")
    log(f"Flattening nested JSON structures...", "INFO")
    
    # Interactive check
    log(f"DQ ALERT: Found null duration for active timeframe on PersonID {bad_record['person_id']}", "WARN")
    log(f"Applying fix: Coalescing null duration to 0.0 based on business rule #4", "WARNING")
    
    # Simulate Join logic
    log("Calculating Worked Org vs Home Org splits...", "INFO")
    transfers = int(punch_count * 0.05)
    log(f"Identified {transfers} labor transfers. Mapping to Cost Center dimension...", "SUCCESS")

    # STEP 3: LOAD
    log("Connecting to Google BigQuery...", "HEADER")
    log("Dataset: `ukg_marketing_prod.wfm_refined`", "INFO")
    
    # Simulate loading bar
    print(f"{Colors.BLUE}Uploading: [", end="", flush=True)
    for _ in range(20):
        time.sleep(0.1)
        print("█", end="", flush=True)
    print(f"] 100%{Colors.ENDC}")
    
    log("Merge operation complete. 0 Duplicates inserted.", "SUCCESS")
    
    # STEP 4: VALIDATION
    log("Running 'Good Data Leads Data' Audits...", "HEADER")
    
    variance = round(random.uniform(0.01, 0.05), 3)
    log(f"Payroll Summary Variance: {variance}% (Threshold < 0.1%)", "SUCCESS")
    
    print("\n")
    print(f"{Colors.GREEN}>> ETL PIPELINE COMPLETED SUCCESSFULLY. DATA IS READY FOR REPORTING.{Colors.ENDC}")

if __name__ == "__main__":
    simulate_etl()
