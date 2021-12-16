class Container():
    def __init__(self, id, position, content):
        self.id = id
        self.position = position
        self.content = content


class ContainerManagment():
    def __init__(self):
        self.containerList = {}

    def add(self, container):
        if not(isinstance(container, Container)):
            raise TypeError("Container type error")
        self.containerList.update({container.id: container})

    # def delete(self, id):
    #     if id not in self.containerList.keys():
    #         raise KeyError("id not found")
    #     elif not isinstance(id, int):
    #         raise TypeError("id not int")
    #     self.containerList.pop(id)

    # def getContainerList(self):
    #     return self.containerList


# storage = ContainerManagment()
# # print(storage.getContainerList())
# cont1 = Container(1, [1, 1, 1], "bike")
# storage.add(cont1)
# print(storage.getContainerList()[1].content)
# storage.delete(cont1.id)
# print(storage.getContainerList())