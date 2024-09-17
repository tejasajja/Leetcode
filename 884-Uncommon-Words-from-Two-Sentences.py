class Solution(object):
    def uncommonFromSentences(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: List[str]
        """
        cnt = Counter(s1.split()) + Counter(s2.split())
        # Step 3 and 4: combine counts and filter uncommon words
        return [word for word, count in cnt.items() if count == 1]
        