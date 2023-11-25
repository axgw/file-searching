def same_bytes(left_filename, right_filename):
    return open(left_filename, "rb").read() == open(right_filename, "rb").read()


# Unfinished
def find_duplicates(filenames):
    matches = []
    for i_left in range(len(filenames)):
        for i_right in range(i_left):
            if same_bytes(left, right):
                matches.append((left, right))
    return matches


if __name__ == "__main__":
    filepaths = ["tests/a1.txt", "tests/a2.txt",
                 "tests/a3.txt", "tests/b1.txt",
                 "tests/b2.txt", "tests/c1.txt"]
    duplicates = find_duplicates(filepaths)
    for (x, y) in duplicates:
        print(x, y)