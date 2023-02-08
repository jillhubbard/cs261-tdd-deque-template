# DO NOT MODIFY THIS FILE
# Run me via: python3 -m unittest test_deque

import unittest
import time
from deque import Deque

# Hint: Once test_has_doubly_linked_list_internal passes, uncomment this line.
#from llist import dllist
# Note: If you're having trouble installing llist, use pyllist instead
#from pyllist import sllist


class TestDeque(unittest.TestCase):

    """
    Initialization
    """

    def test_instantiation(self):
        """
        Test 1: A Deque exists.
        """
        try:
            Deque()
        except NameError:
            self.fail("Could not instantiate Deque.")

    # def test_initial_size(self):
    #     """
    #     Test 2: A deque size is initially zero
    #     """
    #     q = Deque()
    #     self.assertEqual(0,q.items)

    # """
    # Guiding enqueuing and dequeuing with internal storage
    # """

    # def test_has_doubly_linked_list_internal(self):
    #     """
    #     Test 3: A deque has a data member, which is a dllist.
    #     """
    #     from llist import dllist # Hint: pip3 install llist
    #     d = Deque()
    #     self.assertEqual(dllist, type(d.data))

    # # Hint: Once test_has_doubly_linked_list_internal passes, uncomment the import at
    # #       the top of this file.

    # def test_enqueue_left_one_internal(self):
    #     """
    #     Test 4: Enqueueing a 'left' value adds it to the beginning of the internal dllist.
    #     """
    #     d = Deque()
    #     d.enqueue_left('fee')
    #     self.assertEqual('fee', d.data.first.value)

    # def test_enqueue_left_two_internal(self):
    #     """
    #     Test 5: Enqueueing two values to the left results in the first enqueued value
    #     being the second one in the list, and the second value being the first
    #     one in the list.
    #     """
    #     d = Deque()
    #     d.enqueue_left('fee')
    #     d.enqueue_left('fi')
    #     self.assertEqual('fee', d.data.last.value)
    #     self.assertEqual('fi', d.data.first.value)

    # def test_enqueue_left_three_internal(self):
    #     """
    #     Test 6: Enqueueing three values results in the first enqueued value being the
    #     last one in the list, and the third value being the first one in the list.
    #     """
    #     d = Deque()
    #     d.enqueue_left('fee')
    #     d.enqueue_left('fi')
    #     d.enqueue_left('fo')
    #     self.assertEqual('fee', d.data.last.value)
    #     self.assertEqual('fo', d.data.first.value)

    # def test_enqueue_right_one_internal(self):
    #     """
    #     Test 7: Enqueueing a 'right' value adds it to the beginning of the internal dllist.
    #     """
    #     d = Deque()
    #     d.enqueue_right('fee')
    #     self.assertEqual('fee', d.data.first.value)

    # def test_enqueue_right_two_internal(self):
    #     """
    #     Test 8: Enqueueing two values to the right results in the first enqueued value
    #     being the first one in the list, and the second value being the last
    #     one in the list.
    #     """
    #     d = Deque()
    #     d.enqueue_right('fee')
    #     d.enqueue_right('fi')
    #     self.assertEqual('fee', d.data.first.value)
    #     self.assertEqual('fi', d.data.last.value)

    # def test_enqueue_right_three_internal(self):
    #     """
    #     Test 9: Enqueueing three values results in the first enqueued value being the
    #     first one in the list, and the third value being the last one in the list.
    #     """
    #     d = Deque()
    #     d.enqueue_right('fee')
    #     d.enqueue_right('fi')
    #     d.enqueue_right('fo')
    #     self.assertEqual('fee', d.data.first.value)
    #     self.assertEqual('fo', d.data.last.value)

    # def test_dequeue_left_one(self):
    #     """
    #     Test 10: Dequeuing from the left of a single-element deque returns the single value.
    #     """
    #     d = Deque()
    #     d.enqueue_left('fee')
    #     self.assertEqual('fee', d.dequeue_left())
    #     d.enqueue_right('fee')
    #     self.assertEqual('fee', d.dequeue_left())

    # def test_dequeue_left_one_internal(self):
    #     """
    #     Test 11: Dequeuing from the left of a single-element deque removes it from the
    #     internal dllist.
    #     """
    #     d = Deque()
    #     d.enqueue_left('fee')
    #     self.assertEqual(1, d.size())
    #     _ = d.dequeue_left()
    #     self.assertEqual(0, d.size())

    # def test_dequeue_left_two(self):
    #     """
    #     Test 12: Dequeuing from the left of a two-element deque returns the last
    #     left-enqueued value.
    #     """
    #     d = Deque()
    #     d.enqueue_left('fee')
    #     d.enqueue_left('fi')
    #     self.assertEqual('fi', d.dequeue_left())

    # def test_dequeue_left_two_internal(self):
    #     """
    #     Test 13: Dequeuing from the left of a two-element deque removes the last
    #     left-enqueued value from the dllist.
    #     """
    #     d = Deque()
    #     d.enqueue_left('fee')
    #     d.enqueue_left('fi')
    #     _ = d.dequeue_left()
    #     self.assertEqual('fee', d.data.first.value)

    # def test_dequeue_left_three(self):
    #     """
    #     Test 14: Dequeuing from the left of a three-element deque returns each enqueued
    #     value in FIFO order.
    #     """
    #     d = Deque()
    #     d.enqueue_left('fee')
    #     d.enqueue_left('fi')
    #     d.enqueue_left('fo')
    #     self.assertEqual('fo', d.dequeue_left())
    #     self.assertEqual('fi', d.dequeue_left())
    #     self.assertEqual('fee', d.dequeue_left())

    # def test_dequeue_left_three_internal(self):
    #     """
    #     Test 15: Dequeuing from the left of a three-element deque removes each dequeued
    #     value from the internal dllist, in FIFO order.
    #     """
    #     d = Deque()
    #     d.enqueue_left('fee')
    #     d.enqueue_left('fi')
    #     d.enqueue_left('fo')
    #     _ = d.dequeue_left()
    #     self.assertEqual('fi', d.data.first.value)
    #     _ = d.dequeue_left()
    #     self.assertEqual('fee', d.data.first.value)

    # def test_dequeue_right_one(self):
    #     """
    #     Test 16: Dequeuing from the right of a single-element deque returns the single value.
    #     """
    #     d = Deque()
    #     d.enqueue_right('fee')
    #     self.assertEqual('fee', d.dequeue_right())
    #     d.enqueue_left('fee')
    #     self.assertEqual('fee', d.dequeue_right())

    # def test_dequeue_right_one_internal(self):
    #     """
    #     Test 17: Dequeuing from the right of a single-element deque removes it from the
    #     internal dllist.
    #     """
    #     d = Deque()
    #     d.enqueue_right('fee')
    #     self.assertEqual(1, d.size())
    #     _ = d.dequeue_right()
    #     self.assertEqual(0, d.size())

    # def test_dequeue_right_two(self):
    #     """
    #     Test 18: Dequeuing from the right of a two-element deque returns the last
    #     right-enqueued value.
    #     """
    #     d = Deque()
    #     d.enqueue_right('fee')
    #     d.enqueue_right('fi')
    #     self.assertEqual('fi', d.dequeue_right())

    # def test_dequeue_right_two_internal(self):
    #     """
    #     Test 19: Dequeuing from the right of a two-element deque removes the last
    #     right-enqueued value from the dllist.
    #     """
    #     d = Deque()
    #     d.enqueue_right('fee')
    #     d.enqueue_right('fi')
    #     _ = d.dequeue_right()
    #     self.assertEqual('fee', d.data.first.value)

    # def test_dequeue_right_three(self):
    #     """
    #     Test 20: Dequeuing from the right of a three-element deque returns each enqueued
    #     value in LIFO order.
    #     """
    #     d = Deque()
    #     d.enqueue_right('fee')
    #     d.enqueue_right('fi')
    #     d.enqueue_right('fo')
    #     self.assertEqual('fo', d.dequeue_right())
    #     self.assertEqual('fi', d.dequeue_right())
    #     self.assertEqual('fee', d.dequeue_right())

    # def test_dequeue_right_three_internal(self):
    #     """
    #     Test 21: Dequeuing from the right of a three-element deque removes each dequeued
    #     value from the internal dllist, in LIFO order.
    #     """
    #     d = Deque()
    #     d.enqueue_right('fee')
    #     d.enqueue_right('fi')
    #     d.enqueue_right('fo')
    #     _ = d.dequeue_right()
    #     self.assertEqual('fee', d.data.first.value)
    #     _ = d.dequeue_right()
    #     self.assertEqual('fee', d.data.first.value)

    # def test_enqueue_left_dequeue_right(self):
    #     """
    #     Test 22: Dequeuing from the right of a three-element deque returns each
    #     left-enqueued value in FIFO order.
    #     """
    #     d = Deque()
    #     d.enqueue_left('fee')
    #     d.enqueue_left('fi')
    #     d.enqueue_left('fo')
    #     self.assertEqual('fee', d.dequeue_right())
    #     self.assertEqual('fi', d.dequeue_right())
    #     self.assertEqual('fo', d.dequeue_right())

    # def test_enqueue_right_dequeue_left(self):
    #     """
    #     Test 23: Dequeuing from the right of a three-element deque returns each
    #     left-enqueued value in FIFO order.
    #     """
    #     d = Deque()
    #     d.enqueue_right('fee')
    #     d.enqueue_right('fi')
    #     d.enqueue_right('fo')
    #     self.assertEqual('fee', d.dequeue_left())
    #     self.assertEqual('fi', d.dequeue_left())
    #     self.assertEqual('fo', d.dequeue_left())


    # """
    # Emptiness
    # """

    # def test_empty(self):
    #     """
    #     Test 24: A deque is initially empty.
    #     """
    #     d = Deque()
    #     self.assertTrue(d.is_empty())

    # def test_not_empty_left(self):
    #     """
    #     Test 25: A deque with one left-enqueued value is not empty.
    #     """
    #     d = Deque()
    #     d.enqueue_left('fee')
    #     self.assertFalse(d.is_empty())

    # def test_not_empty_right(self):
    #     """
    #     Test 26: A deque with one right-enqueued value is not empty.
    #     """
    #     d = Deque()
    #     d.enqueue_right('fee')
    #     self.assertFalse(d.is_empty())

    # def test_empty_after_dequeue_left(self):
    #     """
    #     Test 27: A deque with one enqueued value is empty after left-dequeuing.
    #     """
    #     d = Deque()
    #     d.enqueue_left('fee')
    #     _ = d.dequeue_left()
    #     self.assertTrue(d.is_empty())

    # def test_empty_after_dequeue_right(self):
    #     """
    #     Test 28: A deque with one enqueued value is empty after right-dequeuing.
    #     """
    #     d = Deque()
    #     d.enqueue_left('fee')
    #     _ = d.dequeue_right()
    #     self.assertTrue(d.is_empty())

    # def test_not_empty_multiple_left(self):
    #     """
    #     Test 29: A deque with two enqueued values is not empty after dequeuing only one
    #     from the left.
    #     """
    #     d = Deque()
    #     d.enqueue_left('fee')
    #     d.enqueue_left('fi')
    #     _ = d.dequeue_left()
    #     self.assertFalse(d.is_empty())

    # def test_not_empty_multiple_right(self):
    #     """
    #     Test 30: A deque with two enqueued values is not empty after dequeuing only one
    #     from the right.
    #     """
    #     d = Deque()
    #     d.enqueue_left('fee')
    #     d.enqueue_left('fi')
    #     _ = d.dequeue_right()
    #     self.assertFalse(d.is_empty())

    #  # """
    # # Size
    # # """


    # def test_dequeue_right_from_an_empty_deque(self):  
    #     """
    #     Test 31: Dequeueing from an empty deque raises ValueError. The size of the queue 
    #     remains 0
    #     """
    #     q = Deque()
    #     try:
    #         q.dequeue_right()
    #         self.fail("Did not raise an Exception")
    #     except ValueError:
    #         self.assertEqual(0, q.size())

    # def test_dequeue_left_from_an_empty_deque(self):  
    #     """
    #     Test 32: Dequeueing from an empty deque raises ValueError. The size of the queue 
    #     remains 0
    #     """
    #     q = Deque()
    #     try:
    #         q.dequeue_left()
    #         self.fail("Did not raise an Exception")
    #     except ValueError:
    #         self.assertEqual(0, q.size())

    # def test_size_after_enqueue_right(self):
    #     """
    #     Test 33: Enqueueing a values increases the number of items in the deque.
    #     """
    #     q = Deque()
    #     q.enqueue_right('fee')
    #     self.assertEqual(1, q.size())

    # def test_size_after_enqueue_left(self):
    #     """
    #     Test 34: Enqueueing a values increases the number of items in the deque.
    #     """
    #     q = Deque()
    #     q.enqueue_left('fi')
    #     self.assertEqual(1, q.size())

    # def test_size_after_dequeue_right(self):
    #     """
    #     Test 35: Dequeueing decreases the number of items in the deque.
    #     """
    #     q = Deque()
    #     q.enqueue_right('fee')
    #     q.enqueue_right('fi')
    #     q.enqueue_right('fo')
    #     q.enqueue_right('fum')
    #     self.assertEqual(4, q.size())
    #     q.dequeue_right()
    #     self.assertEqual(3, q.size())

    # def test_size_after_dequeue_left(self):
    #     """
    #     Test 36: Dequeueing decreases the number of items in the deque.
    #     """
    #     q = Deque()
    #     q.enqueue_left('fee')
    #     q.enqueue_left('fi')
    #     q.enqueue_left('fo')
    #     q.enqueue_left('fum')
    #     self.assertEqual(4, q.size())
    #     q.dequeue_left()
    #     self.assertEqual(3, q.size())

    # def test_size_after_dequeue_right_or_left(self):
    #     """
    #     Test 37: Dequeueing decreases the number of items in the deque.
    #     """
    #     q = Deque()
    #     q.enqueue_left('fee')
    #     q.enqueue_right('fi')
    #     q.enqueue_left('fo')
    #     q.enqueue_right('fum')
    #     self.assertEqual(4, q.size())
    #     q.dequeue_left()
    #     self.assertEqual(3, q.size())
    #     q.dequeue_right()
    #     self.assertEqual(2, q.size())

    
    # """
    # Algorithmic complexity
    # """

    # def test_enqueue_left_vs_right_efficiency(self):
    #     """
    #     Test 38: Enqueing a value is always O(1).
    #     """
    #     time_samples = []
    #     for _ in range(0, 1000):
    #         d = Deque()
    #         start_time = time.time()
    #         d.enqueue_left('fake')
    #         end_time = time.time()
    #         time_samples.append(end_time - start_time)
    #     small_average_enqueue_time = sum(time_samples) / float(len(time_samples))
    #     # Engueue Left
    #     large_deque = Deque()
    #     for _ in range(0, 1000000):
    #         large_deque.enqueue_left('fake')
    #     large_time_samples = []
    #     for _ in range(0, 1000):
    #         start_time = time.time()
    #         large_deque.enqueue_left('fake')
    #         end_time = time.time()
    #         large_time_samples.append(end_time - start_time)
    #     large_average_enqueue_time = sum(large_time_samples) / float(len(large_time_samples))
    #     self.assertAlmostEqual(small_average_enqueue_time, large_average_enqueue_time, delta=small_average_enqueue_time)
    #     # Enqueue Right
    #     large_deque = Deque()
    #     for _ in range(0, 1000000):
    #         large_deque.enqueue_right('fake')
    #     large_time_samples = []
    #     for _ in range(0, 1000):
    #         start_time = time.time()
    #         large_deque.enqueue_right('fake')
    #         end_time = time.time()
    #         large_time_samples.append(end_time - start_time)
    #     large_average_enqueue_time = sum(large_time_samples) / float(len(large_time_samples))
    #     self.assertAlmostEqual(small_average_enqueue_time, large_average_enqueue_time, delta=small_average_enqueue_time)

    # def test_dequeue_left_vs_right_efficiency(self):
    #     """
    #     Test 39: Dequeuing a value is always O(1).
    #     """
    #     time_samples = []
    #     for _ in range(0, 1000):
    #         d = Deque()
    #         d.enqueue_left('fake')
    #         start_time = time.time()
    #         d.dequeue_left()
    #         end_time = time.time()
    #         time_samples.append(end_time - start_time)
    #     small_average_dequeue_time = sum(time_samples) / float(len(time_samples))
    #     # Dequeue Left
    #     large_queue = Deque()
    #     for _ in range(0, 1000000):
    #         large_queue.enqueue_left('fake')
    #     large_time_samples = []
    #     for _ in range(0, 1000):
    #         start_time = time.time()
    #         large_queue.dequeue_left()
    #         end_time = time.time()
    #         large_time_samples.append(end_time - start_time)
    #     large_average_dequeue_time = sum(large_time_samples) / float(len(large_time_samples))
    #     self.assertAlmostEqual(small_average_dequeue_time, large_average_dequeue_time, delta=small_average_dequeue_time)
    #     # Dequeue Right
    #     large_queue = Deque()
    #     for _ in range(0, 1000000):
    #         large_queue.enqueue_left('fake')
    #     large_time_samples = []
    #     for _ in range(0, 1000):
    #         start_time = time.time()
    #         large_queue.dequeue_right()
    #         end_time = time.time()
    #         large_time_samples.append(end_time - start_time)
    #     large_average_dequeue_time = sum(large_time_samples) / float(len(large_time_samples))
    #     self.assertAlmostEqual(small_average_dequeue_time, large_average_dequeue_time, delta=small_average_dequeue_time)


def fake_value():
    return f"FAKE {time.time()}"

if __name__ == '__main__':
    unittest.main()
