import pytest

import schemathesis


@pytest.fixture()
def graphql_schema(graphql_endpoint):
    return schemathesis.graphql.from_url(graphql_endpoint)


def test_raw_schema(graphql_schema):
    assert graphql_schema.raw_schema["__schema"]["types"][1] == {
        "kind": "OBJECT",
        "name": "Patron",
        "fields": [
            {
                "name": "id",
                "args": [],
                "type": {"kind": "SCALAR", "name": "ID", "ofType": None},
                "isDeprecated": False,
                "deprecationReason": None,
            },
            {
                "name": "name",
                "args": [],
                "type": {"kind": "SCALAR", "name": "String", "ofType": None},
                "isDeprecated": False,
                "deprecationReason": None,
            },
            {
                "name": "age",
                "args": [],
                "type": {"kind": "SCALAR", "name": "Int", "ofType": None},
                "isDeprecated": False,
                "deprecationReason": None,
            },
        ],
        "inputFields": None,
        "interfaces": [],
        "enumValues": None,
        "possibleTypes": None,
    }


def test_query_strategy(graphql_schema):
    graphql_schema.query.as_strategy()
