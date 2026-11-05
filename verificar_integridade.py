"""Confere o conteúdo local contra SHA256SUMS.txt, sem rede ou dependências externas."""
from pathlib import Path
import hashlib, sys
root = Path(__file__).resolve().parent
failed = []
for line in (root / "SHA256SUMS.txt").read_text(encoding="utf-8").splitlines():
    expected, name = line.split("  ", 1)
    file = (root / name).resolve()
    if not file.is_relative_to(root) or not file.is_file():
        failed.append(name)
        continue
    if hashlib.sha256(file.read_bytes()).hexdigest() != expected:
        failed.append(name)
if failed:
    print("Arquivos ausentes ou alterados: " + ", ".join(failed))
    sys.exit(1)
print("Todos os arquivos listados conferem com o manifesto local.")
