from typing import List
class Solution:
    def findNumOfValidWords_dict_hash(self, words: List[str], puzzles: List[str]) -> List[int]:
        word_hash = []
        for word in words:
            tmp_struct = {}
            for character in word:
                if character not in tmp_struct.keys():
                    tmp_struct[character] = 1
            word_hash.append(tmp_struct)
        res = []
        for puzzle in puzzles:
            tmp = 0
            puzzle_hash = {}
            first_character = puzzle[0]
            puzzle_struct = {}
            for character in puzzle:
                if character not in puzzle_struct.keys():
                    puzzle_struct[character] = 1
            for ans in word_hash:
                if first_character not in ans.keys():
                    continue
                flag = True
                for key in ans.keys():
                    if key not in puzzle_struct.keys():
                        flag = False
                        break
                if flag:
                    tmp += 1
            res.append(tmp)
        return res
    def findNumOfValidWords_bitOP(self, words: List[str], puzzles: List[str]) -> List[int]:
        word_hash = []
        for word in words:
            tmp_struct = 0
            for character in word:
                tmp_struct |= (1 << ord(character)-ord('a'))
            word_hash.append(tmp_struct)
        res = []
        for puzzle in puzzles:
            tmp = 0
            first_character = ( 1 << ord(puzzle[0]) - ord('a') )
            puzzle_struct = 0
            for character in puzzle:
                puzzle_struct |= (1 << ord(character) - ord('a'))
            for ans in word_hash:
                if ans & first_character != first_character:
                    continue
                if ans & puzzle_struct == ans:
                    tmp += 1
            res.append(tmp)
        return res
    def findNumOfValidWords_subset(self, words: List[str], puzzles: List[str]) -> List[int]:
        word_hash = {}
        for word in words:
            tmp_struct = 0
            for character in word:
                tmp_struct |= (1 << ord(character)-ord('a'))
            if tmp_struct in word_hash.keys():
                word_hash[tmp_struct] += 1
            else:
                word_hash[tmp_struct] = 1
        res = []
        for puzzle in puzzles:
            tmp = 0
            first_character = ( 1 << ord(puzzle[0]) - ord('a') )
            puzzle_struct = 0
            for i in range(1,len(puzzle)):
                puzzle_struct |= (1 << ord(puzzle[i]) - ord('a'))
            subset = puzzle_struct
            # print(bin(subset))
            # print(bin((subset -1)&puzzle_struct))
            # print(bin(puzzle_struct))
            while subset:
            #     # print(bin(subset))
                s = subset | first_character
                if s in word_hash.keys():
                    tmp += word_hash[s]
                subset = (subset - 1) & puzzle_struct
            #     print(subset)
            if first_character in word_hash.keys():
                tmp += word_hash[first_character] 
            res.append(tmp)
        return res
