import zipapp
from pathlib import Path
from time import time


print("\nGetting directories... ", end="")
t = time()

root = Path(__file__).parent
src = root / "src"
dist = root / "dist"
dist.mkdir(exist_ok=True)  # Make `dist` directory if it dosen't exist.
dest_file = dist / "interlittera.pyz"
i = 0
while dest_file.exists():
    i += 1
    dest_file = dist / f"interlittera_{i}.pyz"


t = time()-t
print(f"done. {int(t*1000)}ms")
print(f" {src=}")
print(f" {dest_file=}")

print(f"\nCreating zipapp... ", end="")
t = time()

zipapp.create_archive(src, dest_file)

t = time()-t
print(f"done!\a {int(t*1000)}ms")
