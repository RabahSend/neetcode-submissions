class Solution {
    /**
     * @param {string} s
     * @return {boolean}
     */
    isValid(s) {
        const pairs = new Map([
            [")", "("],
            ["]", "["],
            ["}", "{"]
        ]);

        let stack = []

        for (let i = 0; i < s.length; ++i) {
            if (s[i] === "(" || s[i] === "[" || s[i] === "{") {
                stack.push(s[i])
            }
            else {
                if (stack.length === 0) return false

                if(pairs.get(s[i]) === stack.at(-1)) {
                    stack.pop()
                }
                else return false
            }
        }

        return stack.length === 0
    }
}
