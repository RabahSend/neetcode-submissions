class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * @return {number[]}
     */
    twoSum(nums, target) {
        const map = new Map();

        for (let i = 0; i < nums.length; ++i) {
            map[nums[i]] = i
        }

        for (let i = 0; i < nums.length; ++i) {
            let j = map[target - nums[i]]
            if (j && j != i) {
                return [i, j]
            }
        }

        return [0, 0]
    }
}
