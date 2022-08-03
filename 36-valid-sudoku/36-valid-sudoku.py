class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # rows
        for r in board:
            hashmap = {}
            for x in r:
                if x == ".": continue
                elif x in hashmap: return False
                else: hashmap[x] = 1
                    
        # cols
        for c in range(len(board)):
            hashmap = {}
            for r in board:
                if r[c] == ".": 
                    continue
                elif r[c] in hashmap: 
                    return False
                else: 
                    hashmap[r[c]] = 1
                    
            
            
        # boxes
        boxes = collections.defaultdict(set)
        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                elif board[r][c] in boxes[r//3, c//3]:
                    return False
                else:
                    boxes[(r//3, c//3)].add(board[r][c])
                
            
        return True