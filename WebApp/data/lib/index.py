from random import randint, choice, randrange
from collections import Counter
from json import loads, dumps
from browser import document, html, alert

class Simulation():
    def __init__(self):
        self.PO = 2
        self.TIMES = 100
        self.min = 0

        self.PO_v2 = [0, 1]
        self.SIMS = 10
        self.BASE_SIZE = 10

        self.string_result = {}
        self.int_result = {}
        self.raw_result = {}
        self.simple_result = {}

    def run(self):
        sim = []
        for i in range(self.TIMES):
            sim.append(randint(self.min, self.PO))

        choices = {}
        for i in range(self.PO):
            choices[i] = []

        for i in sim:
            if i in choices:
                for o in choices:
                    if o == i:
                        choices[o].append(i)
                    else:
                        pass

        try:
            for i in choices:
                l = len(choices[i])
                self.string_result[str(i)] = str(l)
            
            for i in choices:
                l = len(choices[i])
                self.int_result[i] = l
            
            return True

        except Exception as e:
            return e
    
    def run_v2(self):
        sim = []
        
        for _ in range(self.TIMES):
            this_sim = []
            for _ in range(self.SIMS):
                go_random = randrange(0, self.BASE_SIZE)
                if go_random in self.PO_v2:
                    this_sim.append(go_random)
                else:
                    pass
            sim.append(this_sim)

        times_in_favor = {}
        for i in self.PO_v2:
            times_in_favor[i] = []

        for i in sim:
            for o in times_in_favor:
                p = i.count(o)
                times_in_favor[o].append(p)

        self.raw_result = times_in_favor

        string_result = {}
        for i in times_in_favor:
            string_result[str(i)] = times_in_favor[i]
        
        self.string_result = string_result

    def extra(self):
        
        final = {}

        for i in self.raw_result:
            final[i] = sum(self.raw_result[i])
        
        self.simple_result = final
    
def getAndSet(self):
    s = Simulation()

    PO = document["PO"].value
    PO = "[" + PO + "]"

    s.PO_v2 = loads(PO)

    s.BASE_SIZE = int(document["BASE"].value)
    s.TIMES = int(document["TIMES"].value)
    s.SIMS = int(document["SIMS"].value)
    typeOfResult = document["Type of Result"]
    option = typeOfResult.options[typeOfResult.selectedIndex].value

    s.run_v2()

    document["RESULT"].clear()

    if option == "SimpleResult":
        s.extra()
        document["RESULT"] <= (dumps(s.simple_result))
    else:
        document["RESULT"] <= (dumps(s.raw_result))

document["RUN"].bind("click", getAndSet)