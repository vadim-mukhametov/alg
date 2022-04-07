import collections

graph = {
    'you': ['alice', 'bob', 'claire', ],
}


def person_is_seller(name):
    return name[-1] == 'e'


# breadth-first search
def bfs(name):
    search_queue = collections.deque()
    search_queue += graph[name]
    searched = []
    while search_queue:
        person = search_queue.popleft()
        if person not in searched:
            if person_is_seller(person):
                print(person)
                return True
            else:
                search_queue += graph[person]
                searched.append(person)


bfs('you')
