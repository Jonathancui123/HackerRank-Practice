def sumGlassAt (i, j, arr):
    #Find the sum of the hourglass with the top left corner at (i, j)
    curr_sum = sum(arr[j][i:i+3])
    curr_sum += arr[j+1][i+1]
    curr_sum += sum(arr[j+2][i:i+3])
    return curr_sum
def hourglassSum(arr):
    arrSums = [sumGlassAt(i, j, arr) for i in range(4) for j in range(4)]
    return max(arrSums)
