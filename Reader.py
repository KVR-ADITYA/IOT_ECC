import secrets
import os
from tinyec import registry
from tqdm import tqdm


class Reader:

    def __init__(self, G, curve='brainpoolP256r1'):
        self.private_key = secrets.randbelow(1000)
        self.public_key = G*self.private_key
        self.P = G
        self.auth = False

    def sendMsg(self):
        print("Hello sent to tag")
        return True

    def inverse(self, b, a):
        for i in tqdm(range(0, 1000)):
            if b == a*i:
                return(i)

    def recieve(self, T2R):
        self.RT = T2R[3] - (T2R[4]*self.P+T2R[1])
        self.rT = self.inverse(self.RT, self.P)
        print("Reader: Authenticating.....")
        # print(self.rT)
        # self.rT = self.rT
        # self.rtd = T2R[0] * (self.private_key + self.rT + T2R[4])
        self.rtd = self.inverse(T2R[0], T2R[3].x*self.P)
        # print(self.rtd)
        # self.rtd = self.rtd/(self.private_key + self.rT + T2R[4])
        # print(self.rtd)
        if self.rtd == self.rT:
            self.auth = True

        self.X2 = T2R[2] + T2R[3] + self.public_key
        # print(self.X2)
        self.r2 = (self.inverse(T2R[2], self.P))
        # print(self.r2)
        self.a2 = self.private_key * ((self.r2)*self.RT)
        # print(self.a2)

        return (self.X2, self.a2)
