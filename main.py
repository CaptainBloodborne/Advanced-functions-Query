from typing import List, Dict, Any


def select(*field_names: str):
    pass


def field_filter(field_name: str, *values):
    pass


def query(data: List[Dict[str, Any]], selection, *filters: callable) -> List[Dict[str, Any]]:
    pass
