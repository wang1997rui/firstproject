print('Hello World!')
print("wangwangbranch")


def find_threedigit(arr, target):
    arr.sort()
    result = []
    for i in range(len(arr) - 1):
        if arr[0] > target:
            return -1

        for j in range(i + 1, len(arr)):
            temp = arr[i] + arr[j]
            if temp <= target and ((target - temp) in arr[j::]):
                print(result.append([arr[i], arr[j], target - temp]))

    return result


if __name__ == "__main__":
    arr = list(map(int, input().split()))
    target = int(input())  # 测试输入的时候，写的是12，下面的结果为12 的结果
    print(find_threedigit(arr, target))