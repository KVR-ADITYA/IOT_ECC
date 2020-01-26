import os
import secrets
from tinyec import registry
from Tag import Tag


class Server:

    def __init__(self, curve='brainpoolP256r1'):
        self.C = registry.get_curve(curve)
        self.P = self.C.g  # P is Generator point

    def setLabels(self, tags):
        for tag in tags:
            temp_key = secrets.randbelow(1000)
            tag.setLabels(temp_key)
        self.labels = []
        for tag in tags:
            self.labels.append(tag.label)
        print(self.labels)
        return self.labels

    def returnTag(self, k):
        for tag in self.tags:
            if tag.label == k:
                return tag

    def setTags(self, public_key, k):
        self.tags = []
        for i in range(k):
            self.tags.append(Tag(f"Device {i}",self.P,public_key) )
        # = [Tag("Device 1", self.P, public_key), Tag("Device 2", self.P, public_key),
        #              Tag("Device 3", self.P, public_key), Tag("Device 4", self.P, public_key)]
