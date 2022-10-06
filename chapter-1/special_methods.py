from typing import Iterable, Any



class SpecialMethods:


    '''String/Bytes Represenation'''
    
    def __repr__(self):
        '''Represent object as string'''
    
    def __str__(self):
        '''Represent readable obj in strings'''
    
    def __format__(self):
        '''Format objects in strings'''
    
    def __bytes__(self):
        '''Bytes representation of objects'''
    
    def __fspath__(self):
        '''File Path Representation'''

    
    '''Conversion to Number'''
    def __int__(self):
        '''Convert a value to a int'''
    
    def __float__(self):
        '''Convert to float'''
    
    def __hash__(self):
        ...
    
    def __complex__(self):
        ...
    
    def __index__(self):
        ...
    
    def __bool__(self):
        ...
    

    '''Emulating Collections'''
    def __len__(self):
        ...

    def __getitem__(self):
        ...

    def __setitem__(self):
        ...

    def __delitem__(self):
        ...

    def __contains__(self):
        ...

    '''Iteration'''

    def __iter__(self):
        ...

    def __aiter__(self):
        ...

    def __next__(self):
        ...

    def __anext__(self):
        ...

    def __reversed__(self):
        ...



    '''Callable or Coroutine Execution'''

    def __call__(self):
        ...

    def __await__(self):
        ...


    '''Context Management'''

    def __enter__(self):
        ...
    
    def __exit__(self):
        ...
    
    def __aenter__(self):
        ...
    
    def __aexit__(self):
        ...

    
    '''Instance Creation and Destruction'''

    def __new__(self):
        ...
    
    def __init__(self):
        ...
    
    def __del__(self):
        ...

    '''Attribute management'''

    def __getattr__(self):
        ...
    
    def __getattribute__(self):
        ...
    
    def __setattr__(self, __name: str, __value: Any) -> None:
        pass

    def __delattr__(self, __name: str) -> None:
        pass
    
    def __dir__(self) -> Iterable[str]:
        pass

    
    '''Attribute Descriptors'''

    def __get__(self):
        ...
    
    def __set__(self):
        ...
    
    def __delete__(self):
        ...
    
    def __set_name__(self):
        ...
    

    '''Abstract Base Class'''

    def __instancecheck__(self, __instance: Any) -> bool:
        pass

    def __subclasscheck__(self, __subclass: type) -> bool:
        pass

    '''Class MetaProgramming'''

    def __prepare__(self):
        ...
    
    def __init_subclass__(cls) -> None:
        pass

    def __class_getitem__(self):
        ...

    def __mro_entries__(self):
        ...

