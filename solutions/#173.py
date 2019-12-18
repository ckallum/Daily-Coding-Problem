def flatten_dict(dictionary):
    result = dict()
    for key, value in dictionary.items():
        if type(value) == dict:
            for k, v in flatten_dict(value).items():
                result[key + "." + k] = v
        else:
            result[key] = value
    print(result)
    return result


def main():
    assert flatten_dict({
        "key": 3,
        "foo": {
            "a": 5,
            "bar": {
                "baz": 8
            }
        }
    }) == {
               "key": 3,
               "foo.a": 5,
               "foo.bar.baz": 8
           }


if __name__ == '__main__':
    main()
