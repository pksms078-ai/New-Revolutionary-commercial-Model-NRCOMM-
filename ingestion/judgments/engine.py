from pathlib import Path
import hashlib

def ingest_judgment(court: str, case_no: str, content: str):
    print(f"⚖️ Ingesting judgment {court} {case_no}")

    # Prepare folder
    folder_path = Path(f"data/judgments/{court}_{case_no}")
    folder_path.mkdir(parents=True, exist_ok=True)

    # Generate file name using content hash
    content_hash = hashlib.md5(content.encode()).hexdigest()
    file_path = folder_path / f"{court}_{case_no}_{content_hash[:10]}.txt"

    file_path.write_text(content, encoding="utf-8")
    print(f"✅ Judgment saved: {file_path}")
