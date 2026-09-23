import collections
import heapq

class Twitter:
    def __init__(self):
        # Global counter to act as a timestamp for chronological ordering
        self.timestamp = 0
        # Maps userId -> set of followeeIds
        self.followees = collections.defaultdict(set)
        # Maps userId -> list of pairs (timestamp, tweetId)
        self.tweets = collections.defaultdict(list)

    def postTweet(self, userId: int, tweetId: int) -> None:
        # Decrement timestamp so smaller numbers represent more recent tweets
        # (handy for Python's min-heap which acts like a max-heap this way)
        self.tweets[userId].append((self.timestamp, tweetId))
        self.timestamp -= 1

    def getNewsFeed(self, userId: int) -> list[int]:
        res = []
        heap = []
        
        # Include the user's own timeline along with their followees
        user_list = list(self.followees[userId])
        user_list.append(userId)
        
        for u in user_list:
            if u in self.tweets:
                # Target the index of the latest tweet
                index = len(self.tweets[u]) - 1
                time, tweetId = self.tweets[u][index]
                # Push elements: (timestamp, tweetId, user_id, index_of_previous_tweet)
                heapq.heappush(heap, (time, tweetId, u, index - 1))
                
        # Pop the 10 most recent tweets using k-way merge
        while heap and len(res) < 10:
            time, tweetId, u, idx = heapq.heappop(heap)
            res.append(tweetId)
            if idx >= 0:
                next_time, next_tweetId = self.tweets[u][idx]
                heapq.heappush(heap, (next_time, next_tweetId, u, idx - 1))
                
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.followees[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.followees[followerId].discard(followeeId)