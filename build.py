from pathlib import Path
import shutil
import subprocess

# Fresh build of CnC and sharpSAT
subprocess.run(["sh", "build.sh", "clean"], cwd="CnC").check_returncode()
subprocess.run(["sh", "build.sh", "march_cu"], cwd="CnC").check_returncode()

if Path("sharpSAT/build").exists():
    shutil.rmtree("sharpSAT/build", ignore_errors=True)
subprocess.run(["sh", "setupdev.sh"], cwd="sharpSAT").check_returncode()
subprocess.run(["make", ], cwd="sharpSAT/build/Release").check_returncode()
