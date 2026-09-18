"""
rev_git.py — the git SHA for output headers (standing rule 8 of CLAUDE.md), shared by the notes/ scripts
that write under notes/review_results/.

SHA is the short SHA of HEAD, with "-dirty" appended if scripts/, notes/*.py or the record
(manuscript/analysis_record.md) have uncommitted changes, and "nogit" if git is unavailable — the test
partB10–partB13 use, computed once at import. Each script prints "git=<SHA>" as its first output line (so
it lands in the run log) and writes it into the header of every .md and .log it produces; a "# ...; git=<SHA>"
first line is added to a .csv only where every reader of that file reads it with comment="#".
"""
import subprocess
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]


def git_sha(repo=REPO):
    try:
        sha = subprocess.check_output(["git", "rev-parse", "--short", "HEAD"], text=True, cwd=repo).strip()
        if subprocess.check_output(["git", "status", "--porcelain", "--", "scripts", "notes/*.py", "manuscript/analysis_record.md"],
                                   text=True, cwd=repo).strip():
            sha += "-dirty"
    except Exception:
        sha = "nogit"
    return sha


SHA = git_sha()
