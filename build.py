from pathlib import Path
from shutil import copyfile

root = Path(__file__).resolve().parent
output = root / "public"
output.mkdir(exist_ok=True)
for name in ("index.html", "yes-or-no.html"):
    copyfile(root / "yes-or-no.html", output / name)
