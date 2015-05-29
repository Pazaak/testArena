__author__ = 'Luis Fabregues de los Santos'

# A simple class that holds
class Battler:
    # Row indicates the placement of the battler in the team for use in gnt_teams
    def __init__(self, hp, pa, pd, ma, md, v, row=0, name="Battler"):
        if pd < 0 or hp < 0 or pa < 0 or ma < 0 or md < 0 or v < 0:
            print "Error: negative values", hp, pa, pd, ma, md, v
        self.maxHP = hp
        self.HP = hp
        self.PA = pa
        self.PD = pd
        self.MA = ma
        self.MD = md
        self.V = v
        self.ROW = row
        self.NAME = name

    def __str__(self):
        return self.NAME

    def tostring(self):
        return "HP: "+str(self.HP)+" PA: "+str(self.PA)+" PD: "+str(self.PD)+" MA: "+str(self.MA)+" MD: "+str(self.MD)\
               +" V: "+str(self.V)

    def maxHP(self):
        return self.maxHP

    def PA(self):
        return self.PA

    def PD(self):
        return self.PD

    def MA(self):
        return self.MA

    def MD(self):
        return self.MD

    def V(self):
        return self.V


class proxyBattler:

    def __init__(self, job_):
        if not isinstance(job_, Battler):
            print "PANIC: bad reference to object"
        self.job = job_
        self.HP = self.job.maxHP
        self.team = 0

    def __str__(self):
        return self.job.NAME

    def tostring(self):
        return self.job.tostring()

    def maxHP(self):
        return self.job.maxHP

    def PA(self):
        return self.job.PA

    def PD(self):
        return self.job.PD

    def MA(self):
        return self.job.MA

    def MD(self):
        return self.job.MD

    def V(self):
        return self.job.V

    def ROW(self):
        return self.job.ROW