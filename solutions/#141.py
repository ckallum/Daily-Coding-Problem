class Stack:
    def __init__(self):
        self.list = []

    def pop(self, stack_number):
        if stack_number > len(self.list):
            return None
        if self.list[stack_number-1]:
            return self.list[stack_number-1].pop()
        else:
            return None

    def push(self, item, stack_number):
        if stack_number <= len(self.list):
            self.list[stack_number-1].append(item)
        else:
            if stack_number == len(self.list)+1:
                self.list.append([item])
            else:
                return None


def main():
    st = Stack()

    st.push(1, 1)
    assert st.list == [[1]]
    st.push(2, 2)
    st.push(3, 3)
    assert st.list == [[1], [2], [3]]
    val = st.pop(4)
    assert not val
    val = st.pop(3)
    assert val == 3
    assert st.list == [[1], [2], []]
    st.push(6, 1)
    st.push(7, 1)
    assert st.list == [[1, 6, 7], [2], []]
    val = st.pop(1)
    assert st.list == [[1, 6], [2], []]


if __name__ == '__main__':
    main()
