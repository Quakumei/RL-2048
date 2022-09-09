import random

class Game2048:
    def __init__(self, board_width: int, board_height: int, max_tile: int=2048, tile_proba:dict[int, float]={2: 0.9, 4: 0.1}):
        self.board_width = board_width
        self.board_height = board_height
        self.max_tile = max_tile
        self.tile_proba = tile_proba

        self.board = [[0 for i in range(self.board_width)] for j in range(self.board_height)]
        self.score = 0
        self.add_tile()
        self.add_tile()

    def get_random_tile(self) -> tuple[int,int]:
        """
        Returns a random tile from the board

        Returns:
            tuple(int,int): indicies of a random tile from the board
        """
        tile = (random.randint(0, self.board_width-1), random.randint(0, self.board_height-1))
        return tile

    def get_empty_tiles(self) -> list[tuple[int,int]]:
        """
        Returns a list of empty tiles on the board

        Returns:
            list[tuple(int,int)]: list of empty tiles on the board
        """
        empty_tiles = []
        for i in range(self.board_height):
            for j in range(self.board_width):
                if self.board[i][j] == 0:
                    empty_tiles.append((i,j))
        return empty_tiles

    def add_tile(self) -> None:
        """
            Adds a tile to a random empty space on the board according to self.tile_proba
        """
        # 1. Get empty tiles
        empty_tiles = self.get_empty_tiles()

        # 2. Throw exception if there is no free space left on the board
        if empty_tiles == []:
            raise Exception("No free space left on the board")

        # 3. Get random tile
        tile = random.choice(empty_tiles)

        # 4. Fill it according to self.tile_proba
        tile_value = random.choices(list(self.tile_proba.keys()), weights=list(self.tile_proba.values()))[0]
        self.board[tile[0]][tile[1]] = tile_value


if __name__ == '__main__':

    game = Game2048(3,3)
    print(game.board)
    try:
        while True:
            game.add_tile()

    except Exception as e:
        print("Game board has been filled:")
        print(game.board)