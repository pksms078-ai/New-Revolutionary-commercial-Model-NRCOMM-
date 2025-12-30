from app.ingestion.circulars.engine import ingest_circular
from app.ingestion.judgments.engine import ingest_judgment
from app.precedence.engine import resolve_conflicts

def main():
    print("🚀 NRCOMM boot successful")

    # ---- Circular Ingestion ----
    ingest_circular(authority="CBDT", circular_no="01", content="Sample Circular Content")

    # ---- Judgment Ingestion ----
    ingest_judgment(court="Supreme Court", case_no="2025-001", content="Sample Judgment Content")

    # ---- Precedence & Conflict Resolution ----
    sample_records = ["Record1", "Record2"]
    resolve_conflicts(sample_records)

if __name__ == "__main__":
    main()

Add end-to-end GST notice analysis flow


