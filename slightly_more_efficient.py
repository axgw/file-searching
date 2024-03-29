def same_bytes(left_filename, right_filename):
    return open(left_filename, "rb").read() == open(right_filename, "rb").read()


def find_duplicates(filenames):
    matches = []
    for i_left in range(len(filenames)):
        left = filenames[i_left]
        for i_right in range(i_left):
            right = filenames[i_right]
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
