def main():
    nums = [int(x) for x in input().split(",")]
    mem = {}
    turn = 1
    last_said = nums[-1]
    for i in range(len(nums) - 1):
        mem[nums[i]] = i
    for turn in range(len(nums) - 1, 29999999):
        if last_said in mem:
            temp = last_said
            last_said = turn - mem[last_said]
            mem[temp] = turn
        else:
            mem[last_said] = turn
            last_said = 0
    print(last_said)
            


if __name__ == "__main__":
    main()
