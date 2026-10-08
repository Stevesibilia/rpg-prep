#!/usr/bin/env python3
"""Controlla una nota di campagna scritta con il modello di campagna-rpg.

Uso: python3 controlla.py campagna.md

Gli errori violano il modello e vanno corretti; gli avvisi segnalano scelte da
rivedere. Esce con 1 se c'è almeno un errore.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

REQUIRED = [
    "A colpo d'occhio",
    "Verità del mondo",
    "Fronti",
    "Fazioni",
    "PG e agganci",
    "Archi",
    "Finali possibili",
    "Fili aperti",
    "Temi e motivi",
    "Controllo",
    "Prima della campagna",
    "Aggiornamenti",
    "Appendice",
]
FRONT_FIELDS = ["Obiettivo", "Volto", "Perché è difficile da fermare"]
ARC_FIELDS = ["Stato", "Sessioni", "Funzione", "Domanda dell'arco", "Fronti in gioco",
              "PG al centro", "Primo taglio"]
PC_FIELDS = ["Desiderio", "Paura", "Segreto", "Legame", "Domanda aperta",
             "Fronti che lo toccano", "Archi che parlano a lui"]
ARC_STATES = {"da giocare", "in corso", "chiuso"}
THREAD_STATES = {"aperto", "ripagato", "perso"}


class Report:
    def __init__(self) -> None:
        self.errors: list[str] = []
        self.warnings: list[str] = []

    def error(self, message: str) -> None:
        self.errors.append(message)

    def warn(self, message: str) -> None:
        self.warnings.append(message)


def section_name(title: str) -> str | None:
    for name in REQUIRED:
        if title == name or title.startswith(name + ":") or title.startswith(name + " "):
            return name
    return None


def split_sections(lines: list[str]) -> dict[str, tuple[int, int]]:
    heads = [(i, line[3:].strip()) for i, line in enumerate(lines) if line.startswith("## ")]
    out = {}
    for n, (start, title) in enumerate(heads):
        end = heads[n + 1][0] if n + 1 < len(heads) else len(lines)
        name = section_name(title)
        if name:
            out[name] = (start, end)
    return out


def subsections(lines: list[str], span: tuple[int, int], pattern: str) -> dict[str, str]:
    """Map the id captured by `pattern` on each ### heading to that block's text."""
    start, end = span
    heads = [i for i in range(start + 1, end) if lines[i].startswith("### ")]
    out = {}
    for n, i in enumerate(heads):
        stop = heads[n + 1] if n + 1 < len(heads) else end
        match = re.match(pattern, lines[i])
        key = match.group(1) if match else lines[i][4:].strip()
        out[key] = "\n".join(lines[i:stop])
    return out


def field(body: str, name: str) -> str | None:
    match = re.search(rf"\*\*{re.escape(name)}:\*\* ?(.*)", body)
    return match.group(1).strip() if match else None


def session_range(text: str | None) -> tuple[int, int] | None:
    if not text:
        return None
    match = re.match(r"(\d+)(?:-(\d+))?", text)
    if not match:
        return None
    low = int(match.group(1))
    return low, int(match.group(2) or low)


def check(path: Path) -> Report:
    report = Report()
    lines = path.read_text().splitlines()
    text = "\n".join(lines)
    sections = split_sections(lines)

    for i, line in enumerate(lines):
        if line.startswith("## ") and not section_name(line[3:].strip()):
            report.warn(f"riga {i + 1}: sezione fuori modello «{line[3:].strip()}»")
    for name in REQUIRED:
        if name not in sections:
            report.error(f"manca la sezione «## {name}»")
    present = [n for n in REQUIRED if n in sections]
    if [sections[n][0] for n in present] != sorted(sections[n][0] for n in present):
        report.error("le sezioni non seguono l'ordine del modello")

    title = next((l for l in lines if l.startswith("# ")), "")
    if not title.startswith("# Campagna: "):
        report.warn("il titolo dovrebbe essere «# Campagna: <nome>», come la nota Joplin")

    # Forbidden dashes, glued fields, visual/mood outside the appendix.
    in_comment = False
    appendix = sections.get("Appendice", (len(lines), len(lines)))[0]
    for i, line in enumerate(lines):
        for dash in ("—", "–"):
            if dash in line:
                report.error(f"riga {i + 1}: trattino «{dash}» vietato: {line.strip()[:70]}")
        if "<!--" in line:
            in_comment = "-->" not in line
            continue
        if in_comment:
            in_comment = "-->" not in line
            continue
        previous = lines[i - 1].strip() if i else ""
        if re.match(r"(\*\*|_|\*[^\s*])", line) and previous and not previous.startswith("#"):
            report.error(f"riga {i + 1}: manca una riga vuota prima di «{line.strip()[:40]}»")
        if i < appendix and re.match(r"\s*(visual|mood):", line):
            report.error(f"riga {i + 1}: «{line.split(':')[0].strip()}:» fuori dall'appendice")

    budget = session_range(re.search(r"\*\*Sessioni:\*\* ?(.*)", "\n".join(lines[:15])).group(1)
                           if re.search(r"\*\*Sessioni:\*\*", "\n".join(lines[:15])) else None)
    if not budget:
        report.error("l'intestazione non dichiara «**Sessioni:** 12-16»")

    # Fronts: fields and a clock that ends in «Se vince».
    fronts = subsections(lines, sections["Fronti"], r"### (F\d+)\. \S") if "Fronti" in sections else {}
    for fid, body in fronts.items():
        if not re.fullmatch(r"F\d+", fid):
            report.error(f"titolo di fronte fuori modello, atteso «### F1. Nome»: {fid}")
            continue
        for name in FRONT_FIELDS:
            if field(body, name) is None:
                report.error(f"{fid}: manca «{name}»")
        steps = re.findall(rf"^- \[[ x]\] \*\*{fid}\.\d+\*\*", body, re.M)
        if not 3 <= len(steps) <= 6:
            report.error(f"{fid}: l'orologio ha {len(steps)} passi «- [ ] **{fid}.1** …» (da 3 a 6)")
        if not re.search(r"^- \[[ x]\] \*\*Se vince\.\*\*", body, re.M):
            report.error(f"{fid}: l'orologio non finisce con «**Se vince.**»")
    if "Fronti" in sections and not fronts:
        report.error("nessun fronte «### F1. Nome»")

    # Arcs: fields, state, session range, references to fronts and PCs.
    arcs = subsections(lines, sections["Archi"], r"### (A\d+)\. \S") if "Archi" in sections else {}
    low = high = 0
    for aid, body in arcs.items():
        if not re.fullmatch(r"A\d+", aid):
            report.error(f"titolo di arco fuori modello, atteso «### A1. Nome»: {aid}")
            continue
        for name in ARC_FIELDS:
            if field(body, name) is None:
                report.error(f"{aid}: manca «{name}»")
        state = (field(body, "Stato") or "").lower()
        if state and state not in ARC_STATES:
            report.error(f"{aid}: stato «{state}» fuori modello ({', '.join(sorted(ARC_STATES))})")
        span = session_range(field(body, "Sessioni"))
        if span:
            low, high = low + span[0], high + span[1]
        for fid in re.findall(r"F\d+", field(body, "Fronti in gioco") or ""):
            if fid not in fronts:
                report.error(f"{aid} cita {fid}, che non esiste")
    if "Archi" in sections and not arcs:
        report.error("nessun arco «### A1. Nome»")
    if budget and arcs and (high < budget[0] or low > budget[1]):
        report.warn(f"gli archi coprono {low}-{high} sessioni, la campagna ne prevede "
                    f"{budget[0]}-{budget[1]}")

    # PCs: fields, references, and the spotlight check.
    pcs = subsections(lines, sections["PG e agganci"], r"### (.+)") if "PG e agganci" in sections else {}
    centred = " ".join(field(body, "PG al centro") or "" for body in arcs.values())
    for name, body in pcs.items():
        for key in PC_FIELDS:
            if field(body, key) is None and f"**{key}:**" not in body:
                report.error(f"PG {name}: manca «{key}»")
        for aid in re.findall(r"A\d+", field(body, "Archi che parlano a lui") or ""):
            if aid not in arcs:
                report.error(f"PG {name} cita {aid}, che non esiste")
        for fid in re.findall(r"F\d+", field(body, "Fronti che lo toccano") or ""):
            if fid not in fronts:
                report.error(f"PG {name} cita {fid}, che non esiste")
        first = name.split(",")[0].split()[0]
        if first not in centred:
            report.warn(f"PG {name} non è fra i «PG al centro» di nessun arco")
    if "PG e agganci" in sections and not pcs:
        report.error("nessun PG «### Nome» in «PG e agganci»")

    # Threads: statuses, and every arc or thread they cite exists.
    threads = {}
    if "Fili aperti" in sections:
        start, end = sections["Fili aperti"]
        for line in lines[start:end]:
            cells = [c.strip() for c in line.strip().strip("|").split("|")]
            if cells and re.fullmatch(r"T\d+", cells[0]) and len(cells) >= 5:
                threads[cells[0]] = cells
                if cells[4].lower() not in THREAD_STATES:
                    report.error(f"{cells[0]}: stato «{cells[4]}» fuori modello "
                                 f"({', '.join(sorted(THREAD_STATES))})")
                for aid in re.findall(r"A\d+", cells[2]):
                    if aid not in arcs:
                        report.error(f"{cells[0]} è seminato in {aid}, che non esiste")
    # Endings: at least two, each seeded in some arc.
    if "Finali possibili" in sections:
        start, end = sections["Finali possibili"]
        endings = [l for l in lines[start:end] if re.match(r"- \*\*.+\.\*\*", l)]
        if len(endings) < 2:
            report.error(f"«Finali possibili» ha {len(endings)} finali (minimo 2)")
        for ending in endings:
            label = re.match(r"- \*\*(.+?)\.\*\*", ending).group(1)
            if "_Condizioni:_" not in ending:
                report.error(f"finale «{label}»: mancano le condizioni")
            seeds = ending.split("_Da seminare:_")[1] if "_Da seminare:_" in ending else ""
            if not re.search(r"A\d+", seeds):
                report.error(f"finale «{label}»: «Da seminare» non indica un arco")
            for tid in re.findall(r"T\d+", seeds):
                if tid not in threads:
                    report.error(f"finale «{label}» cita {tid}, che non è fra i fili")
            for aid in re.findall(r"A\d+", seeds):
                if aid not in arcs:
                    report.error(f"finale «{label}» cita {aid}, che non esiste")

    # The header's current arc must exist.
    current = re.search(r"\*\*Arco corrente:\*\* ?(A\d+)", text)
    if not current:
        report.warn("l'intestazione non indica «**Arco corrente:** A1. …»")
    elif current.group(1) not in arcs:
        report.error(f"l'arco corrente {current.group(1)} non esiste")

    return report


def main() -> int:
    if len(sys.argv) != 2:
        print(__doc__.strip())
        return 2
    report = check(Path(sys.argv[1]))
    for message in report.errors:
        print(f"errore: {message}")
    for message in report.warnings:
        print(f"avviso: {message}")
    print(f"\n{len(report.errors)} errori, {len(report.warnings)} avvisi")
    return 1 if report.errors else 0


if __name__ == "__main__":
    sys.exit(main())
