def show(func):
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        print(res)
        return res

    return wrapper


@show
def test(nums):
    res = []

    def backtrace(nums, path):

        if len(path) == len(nums):
            res.append(path.copy())
            return

        for val in nums:
            if val in path:
                continue
            path.append(val)
            backtrace(nums, path)
            path.pop()

    backtrace(nums, [])
    return res


@show
def test2(nums):
    res = set()
    nums.sort()
    checked = [0] * len(nums)

    def backtrace(nums, path):

        if len(path) == len(nums):
            res.add(tuple(path.copy()))
            return

        for index, val in enumerate(nums):
            if checked[index]:
                continue
            path.append(val)
            checked[index] = 1
            backtrace(nums, path)
            path.pop()
            checked[index] = 0

    backtrace(nums, [])
    return list(map(lambda item: list(item), res))


test2([1, 1, 3])
