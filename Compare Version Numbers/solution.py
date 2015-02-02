class Solution:
    # @param version1, a string
    # @param version2, a string
    # @return an integer
    def compareVersion(self, version1, version2):
        version1_arr = version1.split('.')
        version2_arr = version2.split('.')
        count = 0
        for index in range(0, len(version1_arr)):
            num1 = int(version1_arr[index])
            if index >= len(version2_arr) and num1 == 0:
                return 0
            if index >= len(version2_arr):
                return 1
            num2 = int(version2_arr[index])
            if num1 > num2:
                return 1
            elif num1 < num2:
                return -1
            count = count + 1
            if count < len(version2_arr) and version2_arr[count] == "0":
                return 0
            if count < len(version2_arr):
                return -1
        return 0
        