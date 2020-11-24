from arkfbp.flow import Flow
from arkfbp.node import StartNode, StopNode


# Editor your flow here.
from account.flows.admin.nodes.node1 import Node1


class Main(Flow):

    def create_nodes(self):
        return [
            {
                'cls': StartNode,
                'id': 'start',
                'next': 'node1',
                'x': 0.0,
                'y': 0.0
            },
            {
                'cls': Node1,
                'id': 'node1',
                'next': 'stop',
                'x': 0.0,
                'y': 0.0
            },
            {
                'cls': StopNode,
                'id': 'stop',
                'next': None,
                'x': 0.0,
                'y': 0.0
            }
        ]
