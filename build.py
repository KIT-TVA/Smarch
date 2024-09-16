import subprocess

# Fresh build of CnC and sharpSAT
subprocess.run(["sh", "build.sh", "clean"], cwd="CnC")
subprocess.run(["sh", "build.sh", "march_cu"], cwd="CnC")

subprocess.run(["rm", "-r", "sharpSAT/build"], cwd=".")
subprocess.run(["sh", "setupdev.sh"], cwd="sharpSAT")
subprocess.run(["make", ], cwd="sharpSAT/build/Release")
