import shutil
import os


dirs = [
    "cart",
    "order",
    "product",
    "website",
    "contact",
    "support"
]

for i in os.listdir("src/apps"):
    if i in dirs:
        new_dir = f"src/apps/{i}/migrations"
        for j in os.listdir(new_dir):
            if j != "__init__.py" and j != "__pycache__":
                os.remove(f"{new_dir}/{j}")
            if j == "__pycache__":
                shutil.rmtree(f"{new_dir}/{j}")
