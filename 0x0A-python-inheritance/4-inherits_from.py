def inherits_from(obj, a_class):
    """ function inherits_from """
    return (isinstance(obj, a_class)) or issubclass(type(obj), a_class)

