# Cost O(v^2 * e)
# This problem can be solved with a DFS starting on every
# course, the goal condition is met when one of the paths reaches
# the lenght of the number of the courses.
# To add a new path we have to meet to conditions; one is that
# the course we're adding to the path must not connect the last
# course of the path with one of the nodes specified on the
# restrictions (to avoid bad solutions) and the other one is
# that we can't add a course that has already been taken into
# consideration (to avoid loops)
def find_valid_course(m):
    frontier = []
    courses = set()

    for course in m:
        frontier.append([course])
        courses.add(course)

    while frontier:
        path = frontier.pop()

        if len(path) == len(courses):
            return path

        last = path[-1]

        for course in courses.difference(m[last]):
            if course not in path:
                frontier.append(path + [course])

    return None


courses = {'CSC300': ['CSC100', 'CSC200'], 'CSC200': ['CSC100'], 'CSC100': []}
print(find_valid_course(courses))
