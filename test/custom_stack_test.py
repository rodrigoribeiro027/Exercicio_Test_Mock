import pytest
from custom_stack.custom_stack_class import CustomStack, StackEmptyException, StackFullException ,NumberAscOrder

def test_push_pop():
    stack = CustomStack(3)
    stack.push(1)
    stack.push(2)
    assert stack.pop() == 2
    assert stack.pop() == 1

def test_push_full():
    stack = CustomStack(2)
    stack.push(1)
    stack.push(2)
    with pytest.raises(StackFullException):
        stack.push(3)

def test_pop_empty():
    stack = CustomStack(3)
    with pytest.raises(StackEmptyException):
        stack.pop()

def test_top():
    stack = CustomStack(3)
    stack.push(1)
    stack.push(2)
    assert stack.top() == 2
    stack.pop()
    assert stack.top() == 1

def test_isEmpty():
    stack = CustomStack(3)
    assert stack.isEmpty() == True
    stack.push(1)
    assert stack.isEmpty() == False

def test_size():
    stack = CustomStack(3)
    assert stack.size() == 0
    stack.push(1)
    assert stack.size() == 1
    stack.push(2)
    assert stack.size() == 2

def test_sort_with_empty_stack(mocker):
    stack = CustomStack(6)
    mocker.patch.object(NumberAscOrder, 'sort', return_value=[])
    sorted_numbers = NumberAscOrder.sort(stack)
    assert sorted_numbers == []

def test_sort_with_six_numbers(mocker):
    stack = CustomStack(6)
    for num in [15, 7, 23, 40, 10, 3]:
        stack.push(num)
    mocker.patch.object(NumberAscOrder, 'sort', return_value=[3, 7, 10, 15, 23, 40])
    sorted_numbers = NumberAscOrder.sort(stack)
    assert sorted_numbers == [3, 7, 10, 15, 23, 40]

def test_sort_with_sorted_numbers(mocker):
    stack = CustomStack(6)
    for num in [1, 2, 3, 4, 5, 6]:
        stack.push(num)
    mocker.patch.object(NumberAscOrder, 'sort', return_value=[1, 2, 3, 4, 5, 6])
    sorted_numbers = NumberAscOrder.sort(stack)
    assert sorted_numbers == [1, 2, 3, 4, 5, 6]

def test_sort_with_reverse_sorted_numbers(mocker):
    stack = CustomStack(6)
    for num in [6, 5, 4, 3, 2, 1]:
        stack.push(num)
    mocker.patch.object(NumberAscOrder, 'sort', return_value=[1, 2, 3, 4, 5, 6])
    sorted_numbers = NumberAscOrder.sort(stack)
    assert sorted_numbers == [1, 2, 3, 4, 5, 6]

def test_sort_with_duplicate_numbers(mocker):
    stack = CustomStack(6)
    for num in [3, 7, 23, 7, 10, 3]:
        stack.push(num)
    mocker.patch.object(NumberAscOrder, 'sort', return_value=[3, 3, 7, 7, 10, 23])
    sorted_numbers = NumberAscOrder.sort(stack)
    assert sorted_numbers == [3, 3, 7, 7, 10, 23]
