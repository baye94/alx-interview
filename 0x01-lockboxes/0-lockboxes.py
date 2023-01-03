#!/usr/bin/python3
"""
You have n number of locked boxes.
Each box is numbered sequentially from 0 to n - 1
and each box may contain keys to the other boxes.
"""


def canUnlockAll(boxes):
    """
    method that determines if all the boxes can be opened.
    """

    if boxes is None or len(boxes) == 0:
        return False

    status = ["T"]

    for box in range(1, len(boxes)):
        status.append("F")

    for box in range(0, len(boxes)):
        if (status[box] == "T" or box == 0):
            for key in boxes[box]:
                if int(key) < len(boxes) and status[key] == "F":
                    for k in boxes[key]:
                        if k < len(boxes):
                            status[k] = "T"
                if key < len(boxes):
                    status[key] = "T"

    if "F" in status:
        return False
    return True
