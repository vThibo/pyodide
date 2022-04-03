from setuptools_scm import get_version
from pathlib import Path
PYODIDE_ROOT = Path(__file__).parents[1]

version = get_version(root=PYODIDE_ROOT, version_scheme="release-branch-semver")
(PYODIDE_ROOT / "src/js/version.ts").write_text(f"export let version = {version!r}")
(PYODIDE_ROOT / "src/py/pyodide/version.py").write_text(f"__version__ = {version!r}")
