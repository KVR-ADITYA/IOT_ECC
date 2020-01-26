from Server import Server
from Reader import Reader
from Tag import Tag
from tinyec import ec
import numpy as np
import time
import pickle


curve_list = ["brainpoolP192r1", "brainpoolP160r1", "brainpoolP224r1",  "brainpoolP256r1", "brainpoolP320r1",
              "brainpoolP384r1", "brainpoolP512r1", "secp192r1", "secp224r1", "secp256r1", "secp384r1", "secp521r1"]
for i in curve_list:
    for j in range(20):
        curve = i
        s = Server(curve=curve)
        print(s.P)

        r = Reader(s.P, curve=curve)
        m = s.C.field.p

        start_time = time.time()

        s.setTags(r.public_key, (j+1)*1000)

        def startSession():

            t_list = s.setLabels(s.tags)
            pause = time.time()
            k = t_list[2]  # take temporary key as input
            resume = time.time()
            msg_r = r.sendMsg()
            tag = s.returnTag(int(k))
            if(tag):
                print("Send Success Message")

            else:
                print("Send Abort Message")
                return
            if(msg_r):
                T2R = tag.calculate()
                # print(T2R)
            else:
                print("Message not recieving unsuccessful")
                return

            R2T = r.recieve(T2R)
            tag.recieve(R2T)
            if r.auth:
                print("Authentication from Reader Successful")
                if tag.auth:
                    print("Authentication Successful")
                else:
                    print("Tag Error : Authentication Failed")
            else:
                print("Reader Error : Authentication Failed")

            time_taken = (time.time() - start_time - resume + pause)
            print("--- %s seconds ---" % time_taken)

            return time_taken

        time_taken = startSession()

        # try:
        #     time_lst = pickle.load(open(f'./{curve}.pickle','rb'))
        # except:
        #     time_lst = []
        # time_lst.append(time_taken)

        # pickle.dump(time_lst, open(f'./{curve}.pickle','wb'))
