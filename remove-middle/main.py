# Remove the middle element from a list and returns the new list, if list is an even amount of items, don't remove anything.
def remove_middle(arr: list) -> list | None:
    if len(arr) % 2 == 0:
        return arr
    arr.pop(len(arr) // 2)
    return arr
