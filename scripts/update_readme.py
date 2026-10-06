#!/usr/bin/env python3
"""README의 풀이 현황 표를 디렉터리 구조에서 다시 계산해 갱신한다.

마커(<!-- STATS:START --> ~ <!-- STATS:END -->) 사이만 교체하므로
나머지 README 내용은 손대지 않는다.
"""

from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parent.parent
README = ROOT / "README.md"

START = "<!-- STATS:START -->"
END = "<!-- STATS:END -->"

# 플랫폼별: (폴더명, 표시명, 난이도 정렬 순서, 난이도 라벨 함수)
PLATFORMS = [
    ("백준", "백준", ["Bronze", "Silver", "Gold", "Platinum", "Diamond", "Ruby"], lambda d: d),
    ("프로그래머스", "프로그래머스", ["0", "1", "2", "3", "4", "5"], lambda d: f"Lv.{d}"),
    ("SWEA", "SWEA", ["D1", "D2", "D3", "D4", "D5"], lambda d: d),
    ("LeetCode", "LeetCode", ["Easy", "Medium", "Hard"], lambda d: d),
]


def sort_key(order):
    """알려진 난이도는 정해진 순서대로, 모르는 난이도는 뒤에 이름순으로."""
    def key(name):
        return (order.index(name), "") if name in order else (len(order), name)
    return key


def count_platform(folder, order, label):
    """플랫폼 폴더를 훑어 (총 문제 수, '난이도 n · 난이도 n' 문자열)을 돌려준다."""
    base = ROOT / folder
    if not base.is_dir():
        return 0, ""

    tiers = sorted((d for d in base.iterdir() if d.is_dir()), key=lambda d: sort_key(order)(d.name))

    parts, total = [], 0
    for tier in tiers:
        n = sum(1 for p in tier.iterdir() if p.is_dir())
        if n:
            parts.append(f"{label(tier.name)} {n}")
            total += n
    return total, " · ".join(parts)


def count_languages():
    """확장자별 풀이 파일 수를 센다."""
    counts = {}
    for path in ROOT.rglob("*"):
        if not path.is_file() or ".git" in path.parts:
            continue
        if path.suffix.lower() in {".md", ".json", ".yml", ".yaml"}:
            continue
        counts[path.suffix.lower()] = counts.get(path.suffix.lower(), 0) + 1
    return counts


def build_table():
    rows, grand = [], 0
    for folder, display, order, label in PLATFORMS:
        total, detail = count_platform(folder, order, label)
        if total:
            rows.append(f"| [{display}](./{folder}) | {total} | {detail} |")
            grand += total

    lines = [
        "| 플랫폼 | 문제 수 | 난이도별 |",
        "| --- | --- | --- |",
        *rows,
        f"| **합계** | **{grand}** | |",
    ]
    return "\n".join(lines), grand


def main():
    if not README.exists():
        sys.exit("README.md를 찾을 수 없습니다.")

    text = README.read_text(encoding="utf-8")
    if START not in text or END not in text:
        sys.exit(f"README.md에 {START} / {END} 마커가 없습니다.")

    table, grand = build_table()
    block = f"{START}\n\n{table}\n\n{END}"

    new_text = re.sub(
        re.escape(START) + r".*?" + re.escape(END),
        lambda _: block,
        text,
        flags=re.DOTALL,
    )

    if new_text == text:
        print(f"변경 없음 (총 {grand}문제)")
        return

    README.write_text(new_text, encoding="utf-8")
    print(f"README 갱신 완료 (총 {grand}문제)")
    for ext, n in sorted(count_languages().items(), key=lambda kv: -kv[1]):
        print(f"  {ext}: {n}")


if __name__ == "__main__":
    main()
