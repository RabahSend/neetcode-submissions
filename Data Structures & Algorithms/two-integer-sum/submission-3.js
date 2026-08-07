class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * @return {number[]}
     */
    twoSum(nums, target) {
        const map = new Map();

        for (let i = 0; i < nums.length; ++i) {
            map.set(nums[i], i);
        }

        for (let i = 0; i < nums.length; ++i) {
            const complement = target - nums[i];

            if (map.has(complement)) {
                const j = map.get(complement);

                if (j !== i) {
                    return [i, j];
                }
            }
        }

        return [0, 0]
    }
}
