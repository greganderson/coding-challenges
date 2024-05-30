def test_count_duplicates():
    
    list1 = [1, 2, 3, 4, 5]
    list2 = [3, 4, 5, 6, 7]
    assert count_duplicates(list1, list2) == 3

    
    list1 = [1, 2, 3]
    list2 = [4, 5, 6]
    assert count_duplicates(list1, list2) == 0  
