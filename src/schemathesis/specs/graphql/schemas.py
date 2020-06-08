from functools import partial

import attr
import graphql
import requests
from hypothesis import strategies as st
from hypothesis_graphql import strategies as gql_st

from ...schemas import BaseSchema


@attr.s()
class GraphQLCase:
    path: str = attr.ib()
    data: str = attr.ib()

    def call(self) -> requests.Response:
        return requests.post(self.path, json={"query": self.data})


@attr.s(slots=True)
class GraphQLQuery:
    path: str = attr.ib()
    schema: graphql.GraphQLSchema = attr.ib()

    def as_strategy(self) -> st.SearchStrategy[GraphQLCase]:
        constructor = partial(GraphQLCase, path=self.path)
        return st.builds(constructor, data=gql_st.query(self.schema))


@attr.s()
class GraphQLSchema(BaseSchema):
    schema: graphql.GraphQLSchema = attr.ib(init=False)

    def __attrs_post_init__(self) -> None:
        self.schema = graphql.build_client_schema(self.raw_schema)

    @property  # pragma: no mutate
    def verbose_name(self) -> str:
        return "GraphQL"

    @property
    def query(self) -> GraphQLQuery:
        return GraphQLQuery(path=self.location or "", schema=self.schema)
