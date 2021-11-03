# A RouteTrie will store our routes and their associated handlers
class RouteTrie:
    def __init__(self, root_handler = None):
        self.root = RouteTrieNode(root_handler)

    def insert(self, paths, handler):
        curr = self.root
        for path in paths:
            if path not in curr.children:
                curr.children[path] = RouteTrieNode()
            curr = curr.children[path]
        curr.handler = handler

    def find(self, paths):
        if len(paths) == 0:
            return self.root.handler

        curr = self.root
        for path in paths:
            if path not in curr.children:
                return None
            curr = curr.children[path]
        return curr.handler

# A RouteTrieNode will be similar to our autocomplete TrieNode... with one additional element, a handler.
class RouteTrieNode:
    def __init__(self, handler = None):
        self.handler = handler
        self.children = {}

    def insert(self, path, handler):
        self.children[path] = RouteTrieNode(handler)

    def __repr__(self):
        return str(self.children)


# The Router class will wrap the Trie and handle 
class Router:
    def __init__(self, handler = None):
        self.routes = RouteTrie(handler)
        self.routes.root.handler = handler

    def add_handler(self, path = None, handler = None):
        paths = self.split_path(path)
        self.routes.insert(paths, handler)

    def lookup(self, path):
        paths = self.split_path(path)
        return self.routes.find(paths)

    def split_path(self, path):
        if path in ['/', None, '']:
            return []
        paths = path.split('/')
        if paths[0] == '':
            paths = paths[1:]
        if paths[-1] == '':
            paths = paths[:-1]
        return paths


print("==== test case 1 ====")
router = Router("root handler")
router.add_handler("/home/about", "about handler")

print(router.lookup("/"))                           # root handler
print(router.lookup("/home"))                       # None
print(router.lookup("/home/about"))                 # about handler
print(router.lookup("/home/about/"))                # about handler
print(router.lookup("/home/about/me"))              # None

print("==== test case 2 - edge case ====")
router = Router()
router.add_handler("/")

print(router.lookup("/"))                           # None
print(router.lookup("/home"))                       # None
print(router.lookup("/home/about/me"))              # None

print("==== test case 3 - edge case ====")
router = Router()
router.add_handler()
router.add_handler("/home/about/me", "me handler")

print(router.lookup("/"))                           # None
print(router.lookup("/home/about"))                 # None
print(router.lookup("/home/about/me"))              # me handler