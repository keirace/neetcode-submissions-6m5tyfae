class Twitter:

    def __init__(self):
        self.time = 0
        self.user_tweets_map = defaultdict(list)
        self.user_follow_map = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.user_tweets_map[userId].append((self.time, tweetId))
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        res = self.user_tweets_map[userId][:]
        # Tweets IDs should be ordered from most recent to least recent
        for user in self.user_follow_map[userId]:
            res.extend(self.user_tweets_map[user])
        res.sort(key=lambda x: -x[0])
        return [tweet for _, tweet in res[:10]]

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId: return
        self.user_follow_map[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.user_follow_map[followerId].discard(followeeId)
