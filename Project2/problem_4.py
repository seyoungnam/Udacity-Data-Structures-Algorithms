class Group(object):
    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.users = []

    def add_group(self, group):
        self.groups.append(group)

    def add_user(self, user):
        self.users.append(user)

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name


def is_user_in_group(user, group):
    """
    Return True if user is in the group, False otherwise.

    Args:
      user(str): user name/id
      group(class:Group): group to check user membership against
    """
    group_ls = [group,]
    while group_ls:
        cur_group = group_ls.pop(0)
        if user in cur_group.users:
            return True
        group_ls += cur_group.groups
    return False

parent = Group("parent")
parent_friend = Group("parent_friend")
child = Group("child")
sub_child = Group("subchild")

sub_child_user = "sub_child_user"
sub_child.add_user(sub_child_user)

parent_friend_user = "parent_friend_user"
parent_friend.add_user(parent_friend_user)

child.add_group(sub_child)
parent.add_group(child)
parent.add_group(parent_friend)

print(is_user_in_group(parent_friend_user, child)) # return False
print(is_user_in_group(parent_friend_user, parent)) # return True
print(is_user_in_group(sub_child_user, parent)) # return True