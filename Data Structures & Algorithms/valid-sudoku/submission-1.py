class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for l in board:
            seen=set()
            for i in l:
                if i==".":
                    continue
                if i in seen:
                    return False
                    break;
                else:
                    seen.add(i)

        for l in range(9):
            seen=set()
            for i in range(9):
                if board[i][l]==".":
                    continue
                if board[i][l] in seen:
                    return False
                    break;
                else:
                    seen.add(board[i][l])

        for m in range(0,9,3):
            for k in range(0,9,3):
                seen=set()
                for j in range(m,m+3):
                    for i in range(k,k+3):
                        if board[j][i]==".":
                            continue
                        if board[j][i] in seen:
                            return False
                            break;
                        else:
                            seen.add(board[j][i])

        return True

        