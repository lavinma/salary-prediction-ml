import kagglehub
import shutil
from pathlib import Path

# Download dataset
path = kagglehub.dataset_download("arshkon/linkedin-job-postings")

print("Downloaded to:", path)

# Project folders
project_root = Path(__file__).resolve().parents[1]
raw_dir = project_root / "data" / "raw"
raw_dir.mkdir(parents=True, exist_ok=True)

# Copy every downloaded file into data/raw
for file in Path(path).rglob("*"):
    if file.is_file():
        shutil.copy(file, raw_dir / file.name)

print("Copied dataset to:", raw_dir)