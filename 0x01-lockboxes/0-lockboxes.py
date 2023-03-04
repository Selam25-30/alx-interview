#!/usr/bin/python3
'''
Problem Statement: You have n number of locked boxes in front of you.
Each box is numbered sequentially from 0 to n - 1 and each box may
contain keys to the other boxes.

Write a method that determines if all the boxes can be opened.

    Prototype: def canUnlockAll(boxes)
    boxes is a list of lists
    A key with the same number as a box opens that box
    You can assume all keys will be positive integers
        There can be keys that do not have boxes
    The first box boxes[0] is unlocked
    Return True if all boxes can be opened, else return False
'''


def canUnlockAll(boxes):
    '''Determines if all the boxes can be opened'''
    unlocked = [0]
    for box_id, box in enumerate(boxes):
        if not box:
            continue
        for key in box:
            if key < len(boxes) and key not in unlocked and key != box_id:
                unlocked.append(key)
    if len(unlocked) == len(boxes):
        return True
    return False

# def canUnlockAll(boxes):
#
#     def updater(seq, box): return seq.extend([key for key in box
#                                               if (0 < key < len(boxes))
#                                               and key not in seq])
#     valid_keys = []
#     count = 1

#     updater(valid_keys, boxes[0])
#     for key in valid_keys:
#         updater(valid_keys, boxes[key])
#         count += 1

#     return True if count == len(boxes) else False
