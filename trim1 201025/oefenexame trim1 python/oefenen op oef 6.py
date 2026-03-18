def monotone_reeks():
    invoer = input("geef de getallen in gescheiden door een komma: ")
    nums = [float(x) for x in invoer.split(",")]
    print(nums)

    stijgend = True
    dalend = True
    
    for i in range(len(nums) - 1):
        if nums[i+1] < nums[i]:
            stijgend = False
        if nums[i+1] > nums[i]:
            dalend = False
    
    if stijgend:
        print("Stijgende reeks")
    elif dalend:
        print("Dalende reeks")
    else:
        print("Niet monotoon")

monotone_reeks()
