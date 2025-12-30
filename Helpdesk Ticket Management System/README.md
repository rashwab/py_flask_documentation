# Helpdesk Ticket Management System (PyQt6 UI)

Short demo app that manages simple support tickets. A PyQt6 UI is provided in `main_pyqt.py` as a modern replacement for the original Tkinter UI (`Main.py`).

**Prerequisites**
- Python 3.8+ (recommend using Anaconda/conda environment)
- Either install via `pip` or use `conda` for a binary-compatible Qt runtime

**Install (pip)**
```bash
python -m pip install -r requirements.txt
```

**Install (conda, recommended for Windows)**
```bash
conda install -c conda-forge pyqt=6
```

**Run the app**
```bash
python "main_pyqt.py"
```

**Troubleshooting (DLL load failed / Qt import errors)**
- If you see errors like "DLL load failed while importing QtWidgets" then either:
  - Install PyQt6 from conda-forge (recommended): `conda install -c conda-forge pyqt=6`
  - Or reinstall the PyQt6 runtime with pip: `python -m pip install --force-reinstall PyQt6 PyQt6-Qt6 PyQt6-sip`
  - On Windows, also ensure the Microsoft Visual C++ Redistributable (2015–2022, x64) is installed.

**Alternative**
- If conda networking or permissions block installation, consider using `PySide6` (official Qt bindings). The app code uses standard Qt APIs and can be adapted with minimal changes.

**Files**
- `main_pyqt.py`: PyQt6 GUI implementation
- `Main.py`: original Tkinter UI (kept for reference)
- `requirements.txt`: suggested pip requirements

If you want, I can: update the code to support `PySide6` automatically, or create a small `conda` environment YAML. Which would you prefer? 
