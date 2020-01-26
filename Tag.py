import secrets
from tqdm import tqdm


class Tag:
    def __init__(self, tag_name, G, reader_public_key):
        self.private_key = secrets.randbelow(1000)
        self.public_key = G*self.private_key
        self.name = tag_name
        self.auth = False
        self.reader_public_key = reader_public_key
        self.P = G

    def setLabels(self, temp_key):
        self.label = temp_key

    def calculate(self):
        self.r1 = secrets.randbelow(1000)
        self.r2 = secrets.randbelow(1000)
        self.R1 = self.r1 * self.P
        self.R2 = self.r2 * self.P
        self.X1 = self.label*self.P + self.R1 + self.public_key
        self.A1 = self.private_key * self.X1.x * self.P
        return (self.A1, self.R1, self.R2, self.X1, self.label)

    def inverse(self, b, a):
        for i in tqdm(range(0, 1000)):
            if b == a*i:
                return(i)

    def recieve(self, R2T):
        self.Rrd = R2T[0] - (self.R2+self.X1)
        self.rr = self.inverse(self.Rrd, self.P)
        # print(self.rr)
        self.rrd = self.inverse(R2T[1], self.private_key*self.R2)
        # print(self.rrd)
        if(self.rrd == self.rr):
            self.auth = True
