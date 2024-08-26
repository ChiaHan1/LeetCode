class Solution:
    def numberOfAlternatingGroups(self, colors: List[int]) -> int:
        n = len(colors)
        count = 0
        for i in range(n - 2):
            if colors[i] == colors[i + 2] and colors[i] != colors[i + 1]:
                count += 1

        count += colors[n - 2] == colors[0] and colors[n - 2] != colors[n - 1]
        count += colors[n - 1] == colors[1] and colors[n - 1] != colors[0]

        return count