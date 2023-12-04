#!/usr/bin/python3
"""A method that determines if all boxes can be opened
"""

def canUnlockAll(boxes):
    """A function that returns True of all box in
    boxes can be opened
    """
    if not boxes or not boxes[0]:
        return False

    num_boxes = len(boxes)
    unlocked = set([0])
    keys = set(boxes[0])

    while keys:
        box_to_open = keys.pop()

        if box_to_open < num_boxes and box_to_open not in unlocked:
            unlocked.add(box_to_open)
            keys.update(boxes[box_to_open])

    return len(unlocked) == num_boxes

if __name__ == "__main__":
    boxes1 = [[1], [2], [3], [4], []]
    print(canUnlockAll(boxes1))  # Output: True

    boxes2 = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
    print(canUnlockAll(boxes2))  # Output: True

    boxes3 = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
    print(canUnlockAll(boxes3))  # Output: False
