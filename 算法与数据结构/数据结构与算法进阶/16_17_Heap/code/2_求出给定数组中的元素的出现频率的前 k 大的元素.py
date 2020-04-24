
import collections
import heapq
import functools
import heapq
import functools

@functools.total_ordering
class Element:
    def __init__(self, count, word):
        self.count = count
        self.word = word
    
    def __lt__(self, other):
        if self.count == other.count:
            return self.word < other.word
        return self.count < other.count

    def __eq__(self, other):
        return self.count==other.count and self.word==other.word


def topKFrequent(words, k):
    counts = collections.Counter(words)     # 统计每个 word 出现的个数
    # print(counts)
    freqs = []
    heapq.heapify(freqs)
    for word, count in counts.items():
        item = (Element(count, word), word) # 如果没有指定，默认是用元祖的第一个元素来判断大小
        heapq.heappush(freqs, item)
        if len(freqs) > k:
            heapq.heappop(freqs)

    res = []
    for _ in range(k):
        word = heapq.heappop(freqs)[1]
        res.append(word)
    return res[::-1]

# ---------------------------------------------------------
words = ["i", "love", "you", "i", "love", "coding","i","like","sports","i","love","travel","coding","is","fun"]
k = 4
ret = topKFrequent(words, k)
print(ret)
