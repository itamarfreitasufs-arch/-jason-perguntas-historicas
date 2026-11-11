"""Confere o conteúdo local contra SHA256SUMS.txt, sem rede ou dependências externas."""
from pathlib import Path
import hashlib, sys
root = Path(__file__).resolve().parent
failed = []
for line in (root / "SHA256SUMS.txt").read_text(encoding="utf-8").splitlines():
    if not line.strip():
        continue
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
# O corpo de SKILL.md, a partir do título do protocolo, deve coincidir com protocolo.md.
protocolo = (root / "protocolo.md").read_text(encoding="utf-8")
skill = (root / "SKILL.md").read_text(encoding="utf-8")
inicio = skill.find(protocolo.splitlines()[0])
if inicio < 0 or skill[inicio:] != protocolo:
    print("SKILL.md e protocolo.md divergem no texto do protocolo.")
    sys.exit(1)
print("Todos os arquivos listados conferem com o manifesto local.")
