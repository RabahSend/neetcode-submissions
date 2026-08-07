class Twitter:

    def __init__(self):
        self.tweets = {}
        self.followers = {}
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.tweets:
            self.tweets[userId] = []
        
        if tweetId not in self.tweets[userId]:
            self.time += 1
            self.tweets[userId].append([self.time, tweetId])

    def getNewsFeed(self, userId: int) -> List[int]:
        news = []
        last_tweets = []

        users = [userId] + self.followers.get(userId, [])

        for user in users:
            for time, tweetId in self.tweets.get(user, []):
                heapq.heappush(last_tweets, [-time, tweetId])

        for _ in range(10):
            if not last_tweets:
                break
            news.append(heapq.heappop(last_tweets)[1])

        return news


    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.followers:
            self.followers[followerId] = []

        if followeeId not in self.followers[followerId] and followeeId != followerId:
            self.followers[followerId].append(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.followers:
            self.followers[followerId] = []

        if followeeId in self.followers[followerId]:
            self.followers[followerId].remove(followeeId)
