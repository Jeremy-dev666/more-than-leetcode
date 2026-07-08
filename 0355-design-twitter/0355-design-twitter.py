from typing import List, Dict, Set, Optional
import heapq


class Twitter:

    class Tweet:
        def __init__(self, tweetId: int, time: int):
            self.id: int = tweetId
            self.time: int = time
            self.next: Optional["Twitter.Tweet"] = None


    class User:
        def __init__(self, userId: int):
            self.id: int = userId

            # 我关注的人
            self.followed: Set[int] = set()

            # 我的tweet链表头（最新tweet）
            self.head: Optional["Twitter.Tweet"] = None

            # 默认关注自己
            self.follow(userId)


        def follow(self, userId: int) -> None:
            self.followed.add(userId)


        def unfollow(self, userId: int) -> None:
            # 不能取消关注自己
            if userId != self.id:
                self.followed.discard(userId)


        def post(self, tweetId: int, timestamp: int) -> None:

            tweet = Twitter.Tweet(
                tweetId,
                timestamp
            )

            # 头插法，新tweet放最前面
            tweet.next = self.head
            self.head = tweet



    def __init__(self):

        # userId -> User
        self.users: Dict[int, Twitter.User] = {}

        # 全局递增时间
        self.timestamp: int = 0



    def _getUser(self, userId: int) -> "Twitter.User":

        """
        获取用户，如果不存在则创建
        用于写操作:
        post / follow
        """

        if userId not in self.users:
            self.users[userId] = Twitter.User(userId)

        return self.users[userId]



    def postTweet(self, userId: int, tweetId: int) -> None:

        user = self._getUser(userId)

        user.post(
            tweetId,
            self.timestamp
        )

        self.timestamp += 1



    def getNewsFeed(self, userId: int) -> List[int]:

        # 查询操作，不创建用户
        if userId not in self.users:
            return []


        user = self.users[userId]

        result: List[int] = []


        # Python heap 默认小根堆
        # (-time, tweetId, tweet)
        heap = []


        # 将所有关注者最新tweet加入heap
        for followeeId in user.followed:

            tweet = self.users[followeeId].head

            if tweet:

                heapq.heappush(
                    heap,
                    (-tweet.time, tweet.id, tweet)
                )


        # K路归并
        while heap and len(result) < 10:

            _, _, tweet = heapq.heappop(heap)

            result.append(tweet.id)


            # 当前用户还有下一条旧tweet
            if tweet.next:

                heapq.heappush(
                    heap,
                    (
                        -tweet.next.time,
                        tweet.next.id,
                        tweet.next
                    )
                )


        return result



    def follow(
        self,
        followerId: int,
        followeeId: int
    ) -> None:

        follower = self._getUser(followerId)

        # 确保被关注者存在
        self._getUser(followeeId)

        follower.follow(followeeId)



    def unfollow(
        self,
        followerId: int,
        followeeId: int
    ) -> None:

        if followerId in self.users:

            self.users[followerId].unfollow(
                followeeId
            )