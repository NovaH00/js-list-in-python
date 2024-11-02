from dataclasses import dataclass
from typing import Callable, TypeVar, Union

T = TypeVar('T')  # Input type
R = TypeVar('R')  # Output type


class List:
    def __init__(self, data: Union[list, str, tuple]) -> None:
        self._lst: list
        if isinstance(data, (list, str, tuple)):
            self._lst = list(data)
        else:
            raise ValueError("data must be list, str or tuple")
    
    def __eq__(self, __value: object) -> bool:
        if isinstance(__value, self.__class__):
            return self._lst == __value._lst
        else:
            raise ValueError(f"The other type must be {self.__class__}")

    def __ne__(self, __value: object) -> bool:
        if isinstance(__value, self.__class__):
            return self._lst != __value._lst
        else:
            raise ValueError(f"The other type must be {self.__class__}")

    def __contains__(self, item) -> bool:
        for element in self._lst:
            if element == item:
                return True
        return False
    def __getitem__(self, index):
        return self._lst[index]
    
    def __len__(self):
        return len(self._lst)

    def __str__(self):
        return f"List({self._lst})"
    
    def extend(self, data: Union[list, str, tuple, "List"]):
        if isinstance(data, (list, str, tuple)):
            self._lst.extend(data)
        elif isinstance(data, self.__class__):
            self._lst.extend(data._lst)
        else:
            raise ValueError("The data type must be list, str, tuple or List")
    



    def map(self, map_fn: Callable[[T], R]):
        if not callable(map_fn):
            raise ValueError("map_fn must be a callable function")
        _new_lst = []
        for item in self._lst:
            _new_lst.append(map_fn(item))
        
        self._lst = _new_lst.copy()
        return self
        
    def filter(self, condition_fn: Callable[[T], R]):

        if not callable(condition_fn):
            raise ValueError("condition_fn must be a callable function")

        _new_lst = []
        for item in self._lst:
            if condition_fn(item):
                _new_lst.append(item)
        
        self._lst = _new_lst.copy()
        return self

    def sort(self, reverse=False):
        self._lst.sort(reverse=reverse)
        return self
    
    def forEach(self, fn: Callable[[T], R]):
        if not callable(fn):
            raise ValueError("fn must be a callable function")

        _new_lst = []
        for item in self._lst:
            res = fn(item)
            if res != None:
                _new_lst.append(res)
        
        self._lst = _new_lst.copy()
        return self
    
    def find(self, test_fn: Callable[[T], R]) -> Union[int, str]:
        if not callable(test_fn):
            raise ValueError("test_fn must be a callable function")

        for item in self._lst:
            if test_fn(item):
                return item
    
    def some(self, test_fn: Callable[[T], bool]) -> bool:
        if not callable(test_fn):
            raise ValueError("test_fn must be a callable function")
        
        for item in self._lst:
            if test_fn(item):
                return True
        
        return False

    def every(self, test_fn: Callable[[T], bool]) -> bool:
        if not callable(test_fn):
            raise ValueError("test_fn must be a callable function")

        for item in self._lst:
            if not test_fn(item):
                return False
        
        return True
