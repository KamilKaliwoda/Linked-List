from LinkedList import LinkedList
import LinkedListAbstract as Linked
import unittest


class MyTestCase(unittest.TestCase):

    def test_linked_list(self):
        lst = [('AGH', 'Kraków', 1919), ('UJ', 'Kraków', 1364), ('PW', 'Warszawa', 1915), ('UW', 'Warszawa', 1915),
               ('UP', 'Poznań', 1919), ('PG', 'Gdańsk', 1945)]

        linked_list_1 = LinkedList()
        linked_list_2 = LinkedList()

        for el in lst:
            linked_list_1.add_to_end(el)
            linked_list_2.add(el)
        linked_list_2.remove()
        linked_list_2.reverse()
        linked_list_1.remove_from_end()

        self.assertEqual(linked_list_1.get(), linked_list_2.get())
        self.assertEqual(linked_list_1.head.next.data, linked_list_2.head.next.data)

        linked_list_1.add(('start',))
        linked_list_2.reverse()
        linked_list_2.add_to_end(('start',))
        linked_list_2.reverse()

        self.assertEqual(linked_list_1.get(), linked_list_2.get())
        self.assertEqual(linked_list_1.length(), 6)
        self.assertEqual(linked_list_1.length(), linked_list_2.length())

        linked_list_2.reverse()

        self.assertEqual(linked_list_1.take(1).get(), linked_list_2.drop(5).get())
        self.assertEqual(linked_list_1.is_empty(), False)
        linked_list_1.destroy()
        self.assertEqual(linked_list_1.is_empty(), True)
        linked_list_2.destroy()

    def test_linked_list_abstract(self):
        lst = [('AGH', 'Kraków', 1919), ('UJ', 'Kraków', 1364), ('PW', 'Warszawa', 1915), ('UW', 'Warszawa', 1915),
               ('UP', 'Poznań', 1919), ('PG', 'Gdańsk', 1945)]

        linked_list_1 = Linked.create()
        linked_list_2 = Linked.create()

        for el in lst:
            linked_list_1 = Linked.add_end(el, linked_list_1)
            linked_list_2 = Linked.add(el, linked_list_2)
        linked_list_2 = Linked.remove(linked_list_2)
        linked_list_2 = Linked.reverse(linked_list_2)
        linked_list_1 = Linked.remove_end(linked_list_1)

        self.assertEqual(Linked.get(linked_list_1), Linked.get(linked_list_2))
        self.assertEqual(linked_list_1.next.data, linked_list_2.next.data)

        linked_list_1 = Linked.add(('start',), linked_list_1)
        linked_list_2 = Linked.reverse(linked_list_2)
        linked_list_2 = Linked.add_end(('start',), linked_list_2)
        linked_list_2 = Linked.reverse(linked_list_2)

        self.assertEqual(Linked.get(linked_list_1), Linked.get(linked_list_2))
        self.assertEqual(Linked.length(linked_list_1), 6)
        self.assertEqual(Linked.length(linked_list_1), Linked.length(linked_list_2))

        linked_list_2 = Linked.reverse(linked_list_2)

        self.assertEqual(Linked.get(Linked.take(1, linked_list_1)), Linked.get(Linked.drop(5, linked_list_2)))
        self.assertEqual(Linked.is_empty(linked_list_1), False)
        linked_list_1 = Linked.destroy(linked_list_1)
        self.assertEqual(Linked.is_empty(linked_list_1), True)


if __name__ == '__main__':
    unittest.main()
