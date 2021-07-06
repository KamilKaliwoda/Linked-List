# This version of the linked list is based on the abstract class interface.
from copy import deepcopy


class Element:
    def __init__(self, data):
        self.data = data
        self.next = None


def nil() -> Element:
    return Element(None)


def cons(el, lst: Element) -> Element:
    if lst.data is None:
        lst.data = el
        return lst
    else:
        copy = deepcopy(lst)
        lst.data = el
        lst.next = copy
        return lst


def first(lst: Element) -> [Element, None]:
    if lst.data is None:
        raise ValueError("List is empty.")
    else:
        return lst.data


def rest(lst: Element) -> [Element, None]:
    if lst.data is None:
        raise ValueError("List is empty.")
    elif lst.next is None:
        return nil()
    else:
        copy = deepcopy(lst.next)
        lst = copy
        return lst


def create() -> Element:
    return nil()


def destroy(lst: Element) -> Element:
    lst = nil()
    return lst


def add(el, lst: Element) -> Element:
    lst = cons(el, lst)
    return lst


def remove(lst: Element) -> Element:
    lst = rest(lst)
    return lst


def is_empty(lst: Element) -> bool:
    try:
        one = first(lst)
    except ValueError:
        return True
    else:
        return False


def get(lst: Element) -> Element:
    return first(lst)


def length(lst: Element) -> int:
    try:
        one = first(lst)
    except ValueError:
        return 0
    else:
        rst = rest(lst)
        return 1 + length(rst)


def display(lst: Element) -> None:
    copy = lst
    string = "["

    def disp(lst: Element):
        try:
            frst = first(lst)
        except ValueError:
            return "]"
        else:
            if length(lst) == 1:
                string = str(first(lst))
            else:
                string = str(first(lst)) + ", "
            return string + disp(rest(lst))
    string += disp(copy)
    print(string)
    return


def add_end(el, lst: Element) -> Element:
    if is_empty(lst):
        return cons(el, lst)
    else:
        first_el = first(lst)
        rest_lst = rest(lst)
        return cons(first_el, add_end(el, rest_lst))


def remove_end(lst: Element) -> Element:
    if length(lst) == 2:
        first_el = first(lst)
        new_list = nil()
        return cons(first_el, new_list)
    else:
        first_el = first(lst)
        rest_lst = rest(lst)
        return cons(first_el, remove_end(rest_lst))


def reverse(lst: Element) -> Element:
    new_list = nil()

    def true_reverse(lst: Element, new_list = None) -> Element:
         if is_empty(lst):
             return new_list
         else:
             new_list = cons(first(lst), new_list)
             return true_reverse(rest(lst), new_list)
    return true_reverse(lst, new_list)


def take(n: int, lst: Element) -> Element:

    def true_take(n: int, lst: Element, new_list = nil()) -> Element:
        if is_empty(lst) or n == 0:
            return new_list
        else:
            new_list = cons(first(lst), new_list)
            return true_take(n - 1, rest(lst), new_list)

    return reverse(true_take(n, lst))


def drop(n: int, lst: Element) -> Element:
    if is_empty(lst) or n == 0:
        return lst
    else:
        return drop(n - 1, rest(lst))






