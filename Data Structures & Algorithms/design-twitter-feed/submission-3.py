class Twitter:

    def __init__(self):
        self.count = 0
        self.user_tweets_map = defaultdict(list)
        self.user_follow_map = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.user_tweets_map[userId].append((self.count, tweetId))
        self.count -= 1
        if len(self.user_tweets_map[userId]) > 10:
            self.user_tweets_map[userId].pop(0)

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        minheap = []
        self.user_follow_map[userId].add(userId)
        for user in self.user_follow_map[userId]:
            if user in self.user_tweets_map:
                i = len(self.user_tweets_map[user]) - 1 # next tweet index
                count, tweet = self.user_tweets_map[user][i] # latest tweet
                heapq.heappush(minheap, [count, tweet, user, i - 1])
        
        while minheap and len(res) < 10:
            count, tweet, user, i = heapq.heappop(minheap)
            res.append(tweet)
            if i >= 0: # index of next tweet
                next_count, next_tweet = self.user_tweets_map[user][i]
                heapq.heappush(minheap, [next_count, next_tweet, user, i-1]) # grab the next tweet and push in the heap
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId: return
        self.user_follow_map[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.user_follow_map[followerId].discard(followeeId)
