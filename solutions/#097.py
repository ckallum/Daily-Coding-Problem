class TimeKeyMapper(object):
    def __init__(self):
        self.keys = {}
        self.times = {}

    def set(self, key, value, time):
        if key not in self.keys:
            self.keys[key] = [time]
            if time not in self.times:
                self.times[time] = {key: value}
            else:
                self.times[time][key] = value
        else:
            if time not in self.times:
                self.keys[key].append(time)
                self.keys[key] = sorted(self.keys[key])
                self.times[time] = {key: value}
            else:
                self.times[time][key] = value

    def get(self, key, time):
        if key not in self.keys:
            return None
        elif time in self.times and key in self.times[time]:
            return self.times[time][key]
        else:
            m = None
            for t in self.keys[key]:
                if time >= t:
                    m = self.times[t][key]
                else:
                    break
            return m


def main():
    d = TimeKeyMapper()
    d.set(1, 1, 0)
    d.set(1, 2, 2)
    assert d.get(1, 1) == 1
    assert d.get(1, 3) == 2
    s = TimeKeyMapper()
    s.set(1, 1, 5)
    assert not s.get(1, 0)
    assert s.get(1, 10) == 1


if __name__ == '__main__':
    main()
