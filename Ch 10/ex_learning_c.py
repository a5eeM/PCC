file_path = "/Users/billo/Development/Python/PCC/Ch 10/text_files/learning_python.txt"

# with open(file_path) as f:
#     for line in f:
#         print(line.replace("Python", "C").rstrip())

with open(file_path) as f:
    lines = f.readlines()

for line in lines:
    line = line.rstrip()
    print(line.replace("Python", "C"))
