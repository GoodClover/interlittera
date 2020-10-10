import zipapp
from pathlib import Path

source_dir = Path(__file__).parent
dest_file = source_dir/"dist/interlittera.pyz"

print(f"Creating zipapp from \"{source_dir}\" to \"{dest_file}\" ...")

zipapp.create_archive(source_dir, dest_file)
