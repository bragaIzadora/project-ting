import pytest
from ting_file_management.priority_queue import PriorityQueue


def test_basic_priority_queueing():
    priority_queue = PriorityQueue()

    priority_queue.enqueue({"qtd_linhas": 8})
    priority_queue.enqueue({"qtd_linhas": 2})
    priority_queue.enqueue({"qtd_linhas": 6})

    assert len(priority_queue) == 3

    assert priority_queue.search(0)["qtd_linhas"] == 2
    assert priority_queue.search(1)["qtd_linhas"] == 8
    assert priority_queue.search(2)["qtd_linhas"] == 6

    priority_queue.dequeue()
    assert len(priority_queue) == 2

    assert priority_queue.search(0)["qtd_linhas"] == 8
    assert priority_queue.search(1)["qtd_linhas"] == 6

    with pytest.raises(IndexError):
        priority_queue.search(100)
