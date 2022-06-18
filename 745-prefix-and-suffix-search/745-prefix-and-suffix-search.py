class WordFilter:

    def __init__(self, words: List[str]):
        self.suffix=defaultdict(set)
        self.prefix=defaultdict(set)
        self.index={}
        
        for j in range(len(words)):
            for i in range(len(words[j])):
                self.suffix[words[j][i:]].add(words[j])
                self.prefix[words[j][:i+1]].add(words[j])
            self.index[words[j]]=j

            
    def f(self, prefix: str, suffix: str) -> int:
        prefix_set=set()
        suffix_set=set()

        if prefix in self.prefix:
            prefix_set=self.prefix[prefix]
        
        if suffix in self.suffix:
            suffix_set=self.suffix[suffix]
        
        intersection=prefix_set.intersection(suffix_set)
        
        maximum=-1

        for word in intersection:
            
            if self.index[word] > maximum:
                maximum=self.index[word]
        
        return maximum


# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(prefix,suffix)