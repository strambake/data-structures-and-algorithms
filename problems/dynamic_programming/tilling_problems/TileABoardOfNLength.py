# How many ways we can tile a board of length n with red tile of length p and blue tile of length q
# Assume we have infinite amount of red & blue tile

from unittest import TestCase


class Solution():
    def __init__(self) -> None:
        self.__dp = None
        self.__tile1Length = 0
        self.__tile2Length = 0


    def tileBoardTopDown(self, boardLength: int, tile1Length: int, tile2Length: int):
        """
        Using top-down approach, 
        1. Add a either of tile on a board 
        2. Recusively add all possible tile and find way to tile a board
        i.e Let f(n) is a function to calulate the number of ways to tile a board
        then f(n) = f(n-tile1) + f(n-tile2)
        e.g. boardLength=5, tile1Length=1 and tile2Length=2
                            f(5)
                f(4)                    f(3)
            f(3)    f(2)            f(2)    f(1)
        f(2)            f(0)     f(1)           f(0)   
        """
        self.__tile1Length = tile1Length
        self.__tile2Length = tile2Length       
        self.__dp = [None] * (boardLength+1) 
        return self.__tileBoardTopDown(boardLength)

    
    def __tileBoardTopDown(self, boardLength: int):
        # If board length is in negative means last added tile doesn't complete the board
        # Return 0 i.e. no possible tilling 
        if boardLength < 0:
            # If board 
            return 0

        # If board length is 0 means after adding last tile the board is complete
        # Return 1 i.e. board is complete
        if boardLength == 0:
            return 1

        # See if we already calculated # of possible ways to complete board of length <boardLength>
        # If found return possible ways
        if self.__dp[boardLength]:
            return self.__dp[boardLength]

        # Find a possible ways for all possible combination
        self.__dp[boardLength] = self.__tileBoardTopDown(boardLength-self.__tile1Length) + self.__tileBoardTopDown(boardLength-self.__tile2Length)
        return self.__dp[boardLength]


    def tileBoardBottomUp(self, boardLength: int, tile1Length: int, tile2Length: int):
        if boardLength == 0 or boardLength == 1:
            return 1

        dp = [0] * (boardLength+1)
        dp[0] = 1
        dp[1] = 1
        for i in range(2, boardLength+1):
            dp[i] = dp[i-1] + dp[i-2]

        return dp[boardLength]


class TestCalculateTotalWaysToCompleteABoard(TestCase):
    def testTopDown(self):
        sol = Solution()
        self.assertEqual(8, sol.tileBoardTopDown(5, 1, 2))

    
    def testBottomUp(self):
        sol = Solution()
        self.assertEqual(8, sol.tileBoardBottomUp(5, 1, 2))
