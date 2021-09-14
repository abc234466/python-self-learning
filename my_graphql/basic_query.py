from graphene import ObjectType, String, Schema


class Query(ObjectType):
    hello = String(name=String(default_value='stranger'))

    def resolve_hello(self, info, name):
        return f'Hello {name}!'

    def resolve_goodbye(root, info):
        return 'See ya!'


schema = Schema(query=Query)
basic_string = '{ hello }'
result = schema.execute(basic_string)  # Hello stranger!'
print(result.data['hello'])

query_with_argument = '{ hello(name: "Percy") } '
result = schema.execute(query_with_argument)
print(result.data['hello'])  # Hello Percy!
