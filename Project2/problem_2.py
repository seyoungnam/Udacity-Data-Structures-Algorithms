import os

def find_files(suffix, path):
    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Args:
      suffix(str): suffix if the file name to be found
      path(str): path of the file system

    Returns:
       a list of paths
    """
    if path is '':
        return None
    
    target_files = []
    dirs = [path,]

    while dirs:
        cur_dir = dirs.pop(0)
        eles = os.listdir(cur_dir)

        for ele in eles:
            ele_path = os.path.join(cur_dir, ele)
            # print("ele_path = ", ele_path)
            if os.path.isfile(ele_path) and ele_path.endswith(suffix):
                target_files.append(ele_path)
            elif os.path.isdir(ele_path):
                # print("flag", ele_path)
                dirs.append(ele_path)
    return target_files

# test case 1
print(find_files(".c", "./testdir"))                # ['./testdir/t1.c', './testdir/subdir5/a.c', './testdir/subdir1/a.c', './testdir/subdir3/subsubdir1/b.c']
print(find_files('.h', './testdir'))                # ['./testdir/t1.h', './testdir/subdir5/a.h', './testdir/subdir1/a.h', './testdir/subdir3/subsubdir1/b.h']
print(find_files('.c', './testdir/subdir5'))        # ['./testdir/subdir5/a.c']
# test case 2 - edge case - path is not given
print(find_files('.c', ''))                         # None (because path is not given)
# test case 3 - edge case - suffix is given empty string ''
print(find_files('', "./testdir"))                  # All files under the testdir directory (because all the file ends with '')

