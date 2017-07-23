class Custom:
    # def __init__(self):
    #    self.x = 1
    #    print('Initialized')
    #       print(self.x)

    def __str__(self):
        return "Custom object"

    def __repr__(self):
        return "Custom()"

    def __enter__(self):
        print('Entered')

    def __exit__(self, a, b, c):
        print('Exit successful')


a = Custom()
with a as obj:
    print(str(a))

print('Finished')
