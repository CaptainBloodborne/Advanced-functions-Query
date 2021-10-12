from ..main import query, select, field_filter


def test_query():
    friends = [
        {'name': 'Sam', 'gender': 'male', 'sport': 'Basketball'},
        {'name': 'Emily', 'gender': 'female', 'sport': 'Volleyball'},
        {'name': 'John', 'gender': 'male', 'sport': 'Volleyball'},
        {'name': 'Lily', 'gender': 'female', 'sport': 'Tennis'}
    ]
    value = query(
        friends,
        select(*('name', 'gender', 'sport')),
        field_filter(*('sport', *('Basketball', 'Volleyball'))),
        field_filter(*('gender', *('male',))),
    )
    assert [{'gender': 'male', 'name': 'Sam', 'sport': 'Basketball'},
            {'name': 'John', 'gender': 'male', 'sport': 'Volleyball'}
            ] == value


if __name__ == '__main__':
    test_query()
