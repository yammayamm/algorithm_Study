def permutation(arr, r):
    arr = sorted(arr)
    use = [0 for _ in range(len(arr))]

    def generate(chosen, used):
        if len(chosen) == r:
            print(chosen)
            return

        for i in range(len(arr)):
            if not used[i]:
                chosen.append(arr[i])
                used[i] = 1
                generate(chosen, used)
                used[i] = 0
                chosen.pop()
    generate([], used)
