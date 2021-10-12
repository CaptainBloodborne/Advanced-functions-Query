from typing import Dict, Any, Callable, Iterable

DataType = Iterable[Dict[str, Any]]
ModifierFunc = Callable[[DataType], DataType]


def query(data: DataType, selector: ModifierFunc,
          *filters: ModifierFunc) -> DataType:
    """
    Query data with column selection and filters

    :param data: List of dictionaries with columns and values
    :param selector: result of `select` function call
    :param filters: Any number of results of `field_filter` function calls
    :return: Filtered data
    """
    field = selector(data)
    for row in filters:
        row(field)
    return field


def select(*columns: str) -> ModifierFunc:
    """Return function that selects only specific columns from dataset"""
    def selector(collection):
        lst = []
        for i in collection:
            some_dict = {}
            for j in columns:
                some_dict.update({j: i[j]})
            lst.append(some_dict)
        return lst
    return selector


def field_filter(column: str, *values: Any) -> ModifierFunc:
    """Return function that filters specific column to be one of `values`"""
    def remover(collection):
        for row in collection:
            if row[column] not in values:
                collection.remove(row)
        return collection
    return remover
