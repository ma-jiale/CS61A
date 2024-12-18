def height(t):
    """Return the height of a tree.

    >>> t = tree(3, [tree(5, [tree(1)]), tree(2)])
    >>> height(t)
    2
    """
    if is_leaf(t):
        return 0
    max = 0
    for b in branches(t):
        if height(b) + 1 > max:
            max = height(b) + 1
    return max

def max_path_sum(t):
    """Return the maximum path sum of the tree.
    
    >>> t = tree(1, [tree(5, [tree(1), tree(3)]), tree(10)])
    >>> max_path_sum(t)
    11
    """
    if is_leaf(t):
        return label(t)
    max = 0
    for b in branches(t):
        if max_path_sum(b) + label(t) > max:
            max = max_path_sum(b) + label(t)
    return max


def square_tree(t):
    """Return a treewiththesquareofeveryelementint

    >>> numbers =tree(1,
    ...              [tree(2,
    ...                    [tree(3),
    ...                    tree(4)]),
    ...               tree(5,
    ...                    [tree(6,
    ...                          [tree(7)]),
    ...                     tree(8)])])
    >>> print_tree(square_tree(numbers))
    1
      4
        9
        16
      25
        36
          49
        64
    """
    assert is_tree(t), "input is not a tree"
    if is_leaf(t):
        return tree(label(t)**2)
    else:
        sub_square_trees = [square_tree(b) for b in branches(t)]
        return tree(label(t)**2, sub_square_trees)
    
def find_path(t, x):
    """ takes in a tree and a value x and returns a list
 containing the nodes along the path required to get from the root of the tree to a
 node containing x.

    >>> t = tree(2, [tree(7, [tree(3), tree(6, [tree(5), tree(11)])] ), tree(15)])
    >>> find_path(t, 5)
    [2, 7, 6, 5]
    >>> find_path(t, 10) # returns None
    """
    if label(t) == x:
        return [label(t)]
    for b in branches(t):
        sub_path = find_path(b, x)
        if sub_path:
            return [label(t)] + sub_path


def prune_binary(t, nums):
    """
    
    >>> t = tree('1', [tree('0', [tree('0'),tree('1')]),tree('1',[tree('0')])])
    >>> t
    ['1', ['0', ['0'], ['1']], ['1', ['0']]]
    >>> prune_binary(t, ['01', '110', '100'])
    ['1', ['0', ['0']], ['1', ['0']]]
    """
    if is_leaf(t):
        if label(t) in nums:
            return t
        return None
    else:
        next_valid_nums = [num[1:] for num in nums if num[0] == label(t)]
        new_branches = []
    for b in branches(t):
        pruned_branch = prune_binary(b, next_valid_nums)
        if pruned_branch is not None:
            new_branches = new_branches + [pruned_branch]
        if not new_branches:
            return None
    return tree(label(t), new_branches)  






    # Tree Data Abstraction

def tree(label, branches=[]):
    """Construct a tree with the given label value and a list of branches."""
    for branch in branches:
        assert is_tree(branch), 'branches must be trees'
    return [label] + list(branches)

def label(tree):
    """Return the label value of a tree."""
    return tree[0]

def branches(tree):
    """Return the list of branches of the given tree."""
    return tree[1:]

def is_tree(tree):
    """Returns True if the given tree is a tree, and False otherwise."""
    if type(tree) != list or len(tree) < 1:
        return False
    for branch in branches(tree):
        if not is_tree(branch):
            return False
    return True

def is_leaf(tree):
    """Returns True if the given tree's list of branches is empty, and False
    otherwise.
    """
    return not branches(tree)

def print_tree(t, indent=0):
    """Print a representation of this tree in which each node is
    indented by two spaces times its depth from the root.

    >>> print_tree(tree(1))
    1
    >>> print_tree(tree(1, [tree(2)]))
    1
      2
    >>> numbers = tree(1, [tree(2), tree(3, [tree(4), tree(5)]), tree(6, [tree(7)])])
    >>> print_tree(numbers)
    1
      2
      3
        4
        5
      6
        7
    """
    print('  ' * indent + str(label(t)))
    for b in branches(t):
        print_tree(b, indent + 1)

def copy_tree(t):
    """Returns a copy of t. Only for testing purposes.

    >>> t = tree(5)
    >>> copy = copy_tree(t)
    >>> t = tree(6)
    >>> print_tree(copy)
    5
    """
    return tree(label(t), [copy_tree(b) for b in branches(t)])