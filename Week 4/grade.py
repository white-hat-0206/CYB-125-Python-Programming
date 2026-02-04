#!/usr/bin/env python3
import subprocess
import sys
from pathlib import Path

IDS = Path("./ids.py")
PYTHON = sys.executable  # uses the same python running this script

TOTAL = 0
PASSED = 0
FAILED = 0
FAILED_OUTPUT = ""


def extract_risk_level(stdout: str) -> str:
    """
    Mimics: grep "Risk Level:" | awk '{print $3}'
    So it finds the first line containing 'Risk Level:' and returns the 3rd whitespace token.
    Example line: 'Risk Level: Low' -> tokens = ['Risk', 'Level:', 'Low'] -> 'Low'
    """
    for line in stdout.splitlines():
        if "Risk Level:" in line:
            parts = line.split()
            return parts[2] if len(parts) >= 3 else ""
    return ""


def run_test(name: str, expected: str, test_input: str) -> None:
    global TOTAL, PASSED, FAILED, FAILED_OUTPUT

    TOTAL += 1

    try:
        proc = subprocess.run(
            [PYTHON, str(IDS)],
            input=test_input,
            text=True,
            capture_output=True,
        )
    except FileNotFoundError:
        raise SystemExit(f"Could not find IDS script at: {IDS}")

    actual = extract_risk_level(proc.stdout).strip()

    if actual == expected:
        PASSED += 1
    else:
        FAILED += 1
        FAILED_OUTPUT += (
            "\n----------------------------------------\n"
            f"FAILED TEST: {name}\n"
            f"EXPECTED:    {expected}\n"
            f"ACTUAL:      {actual or '<none>'}\n"
            "INPUT:\n"
            f"{test_input}\n"
        )


# ==================================================
# LOGIN TESTS
# ==================================================

run_test(
    "Standard Internal Login (1 attempt)",
    "Low",
    """login
internal
alice
1""",
)

run_test(
    "Standard Internal Login (3 attempts)",
    "Medium",
    """login
internal
alice
3""",
)

run_test(
    "Standard Internal Login (5 attempts)",
    "High",
    """login
internal
alice
5""",
)

run_test(
    "Standard Internal Login (10 attempts)",
    "Critical",
    """login
internal
alice
10""",
)

run_test(
    "Standard External Login (1 attempts)",
    "Medium",
    """login
external
alice
1""",
)

run_test(
    "Standard External Login (3 attempts)",
    "High",
    """login
external
alice
3""",
)

run_test(
    "Standard External Login (5 attempts)",
    "Critical",
    """login
external
alice
5""",
)

run_test(
    "Privileged Internal Login (1 attempt)",
    "Medium",
    """login
internal
admin
1""",
)

run_test(
    "Privileged Internal Login (3 attempts)",
    "High",
    """login
internal
admin
3""",
)

run_test(
    "Privileged Internal Login (5 attempts)",
    "Critical",
    """login
internal
admin
5""",
)

run_test(
    "Privileged External Login (1 attempt)",
    "High",
    """login
external
admin
1""",
)

run_test(
    "Privileged External Login (2 attempts)",
    "Critical",
    """login
external
admin
2""",
)

# ==================================================
# FINAL GRADE
# ==================================================

GRADE = (PASSED * 100 // TOTAL) if TOTAL else 0

print("")
print("========== IDS TEST RESULTS ==========")
print(f"Total Tests:  {TOTAL}")
print(f"Passed:       {PASSED}")
print(f"Failed:       {FAILED}")
print(f"Grade:        {GRADE} / 100")
print("=====================================")

if FAILED > 0:
    print("")
    print("========== FAILED TEST DETAILS ==========")
    print(FAILED_OUTPUT, end="")
