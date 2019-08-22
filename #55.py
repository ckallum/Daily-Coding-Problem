import hashlib

class URLShortener(object):
    def __init__(self):
        self.hashdict = dict()
        self.hash = hashlib.sha256

    def shorten(self, url):
        urlHash = self.hash(url.encode()).hexdigest()
        shortenedHash = urlHash[:6]
        self.hashdict[shortenedHash] = url
        return shortenedHash

    def restore(self, shorthash):
        if shorthash in self.hashdict:
            return self.hashdict[shorthash]


def main():
    url = "http://www.dailycodingproblem.com"
    shortner = URLShortener()
    short = shortner.shorten(url)
    assert shortner.restore(short) == url


if __name__ == '__main__':
    main()
