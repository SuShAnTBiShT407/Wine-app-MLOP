import os

dir = [

    os.path.join("data", "raw"), 
    os.path.join("data", "processed"), 
    "notebooks", 
    "saves_models",
    "src"

]

for dir_ in dir:
    if not os.path.exists(dir_):
        os.makedirs(dir_)
    with open(os.path.join(dir_, ".gitkeep"), "w") as f:
        pass

files = [

    "dvc.yaml",
    "params.yaml",
    ".gitignore",
    os.path.join("src", "__init__.py")

]
for file in files:
    with open(file, "w") as f:
        pass