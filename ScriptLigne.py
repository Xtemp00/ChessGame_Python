import os
import glob
# on récupère le répertoire courant
parent_dir = os.getcwd()
total = 0

for filename in glob.glob(os.path.join(parent_dir, "*.py")):
    with open(filename, 'r') as f:
        num_lines = sum(1 for line in f)
        print(f"{filename}: {num_lines} lignes")
        total += num_lines
print(total)