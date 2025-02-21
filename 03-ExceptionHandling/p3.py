# Finally Block (Always Executed)

try:
    file = open("sample.txt", "r")
    content = file.read()
except FileNotFoundError:
    print("File not found!")
finally:
    print("Execution complete.")
    # File will be closed, even if there's an error