from pathlib import Path
import hashlib

def ingest_circular(authority: str, circular_no: str, content: str):
    print(f"📄 Ingesting circular {authority} {circular_no}")

    # Prepare folder
    folder_path = Path(f"data/circulars/{authority}_{circular_no}")
    folder_path.mkdir(parents=True, exist_ok=True)

    # Generate file name using content hash
    content_hash = hashlib.md5(content.encode()).hexdigest()
    file_path = folder_path / f"{authority}_{circular_no}_{content_hash[:10]}.txt"
    
    file_path.write_text(content, encoding="utf-8")
    print(f"✅ Circular saved: {file_path}")
