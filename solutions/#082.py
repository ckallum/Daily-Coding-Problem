class File(object):
    def __init__(self, contents):
        self.contents = contents
        self.offset = 0
        self.current_chars = ""

    def read7(self):
        start = self.offset
        end = min(self.offset + 7, len(self.contents))
        self.offset = end
        return self.contents[start:end].strip()

    def read_n(self, n):
        while len(self.current_chars) < n:
            new_chars = self.read7()
            if not new_chars:
                break
            self.current_chars += new_chars
        res = self.current_chars[:n]
        self.current_chars = self.current_chars[n:]
        return res


def main():
    file = File("Hello World")
    assert file.read7() == "Hello W"
    assert file.read7() == "orld"
    assert file.read7() == ""

    file2 = File("Hello World")
    assert file2.read_n(8) == "Hello Wo"
    assert file2.read_n(8) == "rld"
    assert file2.read_n(8) == ""


if __name__ == '__main__':
    main()