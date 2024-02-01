import sys

def append_to_file(title, body, version, output_file):
    with open(output_file, 'a') as file:
        file.write(f"{title}\n{body}\n{version}\n")

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: python append_to_file.py <title> <body> <version> <output_file>")
        sys.exit(1)

    title = sys.argv[1]
    body = sys.argv[2]
    version = sys.argv[3]
    output_file = sys.argv[4]

    append_to_file(title, body, version, output_file)
    print("Data appended to file successfully.")
