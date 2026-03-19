#!/usr/bin/env python3
import re
import subprocess
import sys
from pathlib import Path

PW_CHECKER = Path("./pw_checker.py")
PYTHON = sys.executable  # uses the same python running this script

TOTAL = 0
PASSED = 0
FAILED = 0
FAILED_OUTPUT = ""


LEVEL_RE = re.compile(r"\b(WEAK|MEDIUM|STRONG)\b")


def extract_level(output: str) -> str:
    """
    Find the first occurrence of WEAK/MEDIUM/STRONG anywhere in the output.
    This is intentionally tolerant of different formatting (prompts, extra text, etc.).
    """
    m = LEVEL_RE.search(output)
    return m.group(1) if m else ""


def run_test(name: str, expected: str, password_input: str) -> None:
    global TOTAL, PASSED, FAILED, FAILED_OUTPUT

    TOTAL += 1

    if not PW_CHECKER.exists():
        raise SystemExit(f"Could not find pw_checker script at: {PW_CHECKER}")

    # Feed one password, then q to exit
    test_input = f"{password_input}\nq\n"

    try:
        proc = subprocess.run(
            [PYTHON, str(PW_CHECKER)],
            input=test_input,
            text=True,
            capture_output=True,
            timeout=5,
        )
    except subprocess.TimeoutExpired:
        FAILED += 1
        FAILED_OUTPUT += (
            "\n----------------------------------------\n"
            f"FAILED TEST: {name}\n"
            f"EXPECTED:    {expected}\n"
            f"ACTUAL:      <timeout>\n"
            "INPUT:\n"
            f"{password_input}\n"
        )
        return

    combined_output = (proc.stdout or "") + "\n" + (proc.stderr or "")
    actual = extract_level(combined_output).strip()

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
            f"{password_input}\n"
        )


# ==================================================
# TEST CASES
# ==================================================

run_test("TC01 - strong 1", "STRONG", "G7m!Qp9xR2vN")
run_test("TC02 - strong 2", "STRONG", "Kp3_8Zx+vN72tR")
run_test("TC03 - medium short12", "MEDIUM", "L9q!T2sK")
run_test("TC04 - medium missing symbol", "MEDIUM", "N4x7pQv8")
run_test("TC05 - medium missing digit", "MEDIUM", "HqT!pZxv")
run_test("TC06 - medium missing uppercase", "MEDIUM", "m7q!t2sk")
run_test("TC07 - medium missing lowercase", "MEDIUM", "M7Q!T2SK")
run_test("TC08 - weak too short (<8)", "WEAK", "A7!qT2")
run_test("TC09 - missing uppercase (3 categories)", "MEDIUM", "m7q!t2sk9xv")
run_test("TC10 - missing lowercase (3 categories)", "MEDIUM", "M7Q!T2SK9XV")
run_test("TC11 - missing digit (3 categories)", "MEDIUM", "JqT!pZxvNmRs")
run_test("TC12 - missing symbol (3 categories)", "MEDIUM", "R7mQp9xT2vNs")
run_test("TC13 - weak unallowed symbol & others", "WEAK", "ZxT2vNs9?Qp")
run_test("TC14 - weak unallowed symbol 2", "WEAK", "Kp3_8Zx+vN?2")
run_test("TC15 - weak contains space", "WEAK", "G7m! Qp9xR2vN")
run_test("TC16 - weak contains tab", "WEAK", "G7m!\tQp9xR2vN")
run_test("TC17 - weak common word admin", "WEAK", "AdminConsole1!")
run_test("TC18 - weak common word password", "WEAK", "PasswordPolicy9!")
run_test("TC19 - weak common word network", "WEAK", "NetworkTeam9!")
run_test("TC20 - weak no digit no symbol", "WEAK", "QpVnRsTjLmXc")
run_test("TC21 - weak digits only", "WEAK", "739104628516")
run_test("TC22 - weak all symbols", "WEAK", "!!!!!!!!!!!!")

# ==================================================
# FINAL GRADE
# ==================================================

GRADE = (PASSED * 100 // TOTAL) if TOTAL else 0

print("")
print("========== PW_CHECKER TEST RESULTS ==========")
print(f"Total Tests:  {TOTAL}")
print(f"Passed:       {PASSED}")
print(f"Failed:       {FAILED}")
print(f"Grade:        {GRADE} / 100")
print("============================================")

if FAILED > 0:
    print("")
    print("========== FAILED TEST DETAILS ==========")
    print(FAILED_OUTPUT, end="")