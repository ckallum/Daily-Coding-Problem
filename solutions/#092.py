from copy import deepcopy


def courses_to_take(course_to_prereqs):
    if not course_to_prereqs:
        return []

    for course in course_to_prereqs:
        if not course_to_prereqs[course]:
            ret = [course]
            next_prereqs = deepcopy(course_to_prereqs)
            del next_prereqs[course]
            if not next_prereqs:
                return ret
            for pre_req in next_prereqs:
                if course in next_prereqs[pre_req]:
                    next_prereqs[pre_req].remove(course)
            extra = courses_to_take(next_prereqs)
            if extra is not None:
                return ret + extra
    return None


def main():
    courses = {
        'CSC300': ['CSC100', 'CSC200'],
        'CSC200': ['CSC100'],
        'CSC100': []
    }
    assert courses_to_take(courses) == ['CSC100', 'CSC200', 'CSC300']
    prereqs = {
        'CSC400': ['CSC200'],
        'CSC300': ['CSC100', 'CSC200'],
        'CSC200': ['CSC100'],
        'CSC100': []
    }
    assert courses_to_take(prereqs) == ['CSC100', 'CSC200', 'CSC400', 'CSC300']
    prereqs = {
        'CSC400': ['CSC300'],
        'CSC300': ['CSC100', 'CSC200'],
        'CSC200': ['CSC100'],
        'CSC100': ['CSC400']
    }
    assert not courses_to_take(prereqs)


if __name__ == '__main__':
    main()
