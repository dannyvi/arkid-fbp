from arkfbp.node import FunctionNode


# Editor your node here.
class Node1(FunctionNode):

    def run(self, *args, **kwargs):
        print(f'hi, Hello, Admin Permission Check Done!')
        return True
