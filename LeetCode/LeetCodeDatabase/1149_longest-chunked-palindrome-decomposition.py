class Solution:
    def longestDecomposition(self, text: str) -> int:
        res = 1

        while True:

            print(f"curr string: {text}")

            if len(text) <= 1:
                return res
            match = 0
            for i in range(len(text) // 2):

                if text[i] == text[-1] and text[:i + 1] == text[-i - 1:]:
                    match = 1
                    print(f"{text} --> SEGMENT: {text[:i + 1]}, {text[i + 1:-i - 1]}, {text[-i - 1:]}")
                    text = text[i + 1:-i - 1]

                    res += 2 if len(text) else 1

                    break

            if not match:
                break

            print(f"NEXT: {text}")
        return res


if __name__ == "__main__":
    data = "ghiabcdefhelloadamhelloabcdefghi"
    res = Solution().longestDecomposition(data)
    print(res)