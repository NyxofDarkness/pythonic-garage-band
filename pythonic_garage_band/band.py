class Musician:
    members = []

    def __init__(self, name, instrument="guitar"):
        self.name = name
        self.instrument = instrument
        self.solo = f"crazy {instrument} solo"

    def get_instrument(self):
        return self.instrument

    def play_solo(self):
        return self.solo

    def __str__(self):
        return f"My name is {self.name} and I play {self.instrument}"


    def __repr__(self):
        return f"{self.__class__.__name__} instance. Name = {self.name}"

class Band:
    instances = []

    def __init__(self, name, members=None):
        self.name = name
        self.members = members
        Band.instances.append(self.name)

    def __str__(self):
        return f"The band {self.name}"

    def __repr__(self):
        return f"Band instance. name={self.name}, members={self.members}"

    def play_solos(self):
        return [member.solo for member in self.members]

    @classmethod
    def to_list(cls):
        return cls.instances
        



class Guitarist(Musician):
    def __init__(self, name):
        super().__init__(name)
        self.instrument = 'guitar'
        self.solo = 'face melting guitar solo'

    # def __str__(self):
    #     return(f"My name is {self.name} and I play {self.instrument}")

class Bassist(Musician):
    def __init__(self, name):
        super().__init__(name)
        self.instrument = 'bass'
        self.solo = 'bom bom buh bom'

class Drummer(Musician):
    def __init__(self, name):
        super().__init__(name)
        self.instrument = 'drums'
        self.solo = 'rattle boom crash'

if __name__ == "__main__":
    bandz = []
    jessie = Band("timefortrouble")
    james = Band("makeitdouble")
    band.append(jessie)
    band.append(james)
    print(bandz)