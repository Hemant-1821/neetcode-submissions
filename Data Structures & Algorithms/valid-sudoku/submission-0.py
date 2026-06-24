class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_obj = {}
        col_obj = {}
        sqaure_obj = {}

        # iterate through the rows
        for row_index, row in enumerate(board):
            # interate each row
            for col_index, ele in enumerate(board[row_index]):
                if(ele == '.'):
                    continue
                row, col = row_index, col_index
                # check if this number is already present in row
                if(row_obj.get(row_index)):
                    if(row_obj[row_index].get(ele)):
                        return False # duplicate element in a row
                    else:
                        row_obj[row_index][ele] = True
                else:
                    row_obj[row_index] = { ele: True }
                # check if this number is already present in column
                if(col_obj.get(col_index)):
                    if(col_obj[col_index].get(ele)):
                        return False # duplicate element in a column
                    else:
                        col_obj[col_index][ele] = True
                else:
                    col_obj[col_index] = { ele: True }
                # check if this number is already present in square
                
                # find minimised sqaure coordinate
                s_row, s_col = row//3, col//3
                # finding the sqaure number, 2D -> 1D cordinate
                s_num = s_row*3 + s_col
                # checking if ele is present for this square
                if(sqaure_obj.get(s_num)):
                    if(sqaure_obj[s_num].get(ele)):
                        return False # duplicate element in a column
                    else:
                        sqaure_obj[s_num][ele] = True
                else:
                    sqaure_obj[s_num] = {ele: True}
        
        # return true if all checks passed
        return True
