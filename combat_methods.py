__author__ = 'Luis Fabregues de los Santos'
"""Helping methods to deal with combat damage and how two units (battlers or groups)
fight each other."""
from header_classes import Battler

# -----------------------------------------------------------------
# battle methods
# -----------------------------------------------------------------
# here we'll define the way two battlers fight
# this method will be used to perform the ranking via tournament
def battle(subject1, subject2, formula):
    if not isinstance(subject1, Battler) or not isinstance(subject2, Battler):
        print "PANIC: bad argument"+str(subject1)+" "+str(subject2)

    # the fastest attack first
    if subject1.V() > subject2.V():
        proxy1, proxy2 = subject1, subject2
    else:
        proxy1, proxy2 = subject2, subject1

    # while any of the battlers is dead
    while proxy1.HP > 0 and proxy2.HP > 0:
        #  check for proxy1 if is more physical or magical damage dealer
        if proxy1.PA() > proxy1.MA() or (proxy1.PA() == proxy1.MA() and proxy2.MD() >= proxy2.PD()):
            deal_pdamage(proxy1, proxy2, formula)
        else:
            deal_mdamage(proxy1, proxy2, formula)
        #  check the same for proxy2 if it's not dead
        if proxy2.HP > 0:
            if proxy2.PA() > proxy2.MA() or (proxy2.PA() == proxy2.MA() and proxy1.MD() >= proxy1.PD()):
                deal_pdamage(proxy2, proxy1, formula)
            else:
                deal_mdamage(proxy2, proxy1, formula)


def team_battle(subject1, subject2, formula):

    blockers = [0, 0]
    # this will set apart the teams
    for x in subject1:
        blockers[0] += 1-x.ROW()
    for x in subject2:
        x.team = 1
        blockers[1] += 1-x.ROW()


    # we'll add both lists together to determine the speed order
    btlfield = subject1 + subject2
    btlfield.sort(key=lambda btl: btl.V(), reverse=True)

    disTeam = [0, 0]

    while disTeam[0] < 5 and disTeam[1] < 5:
        i = 0
        while i < len(btlfield):
            j = 0
            while j < len(btlfield) and btlfield[i].HP > 0:
                if btlfield[i].team != btlfield[j].team and btlfield[j].HP > 0 and (btlfield[i].ROW() == 1 or
                                                            btlfield[j].ROW() == 0 or blockers[btlfield[j].team] == 0):
                    if btlfield[i].PA() > btlfield[i].MA() or (btlfield[i].PA() == btlfield[i].MA() and
                                                                   btlfield[j].MD() >= btlfield[j].PD()):
                        deal_pdamage(btlfield[i], btlfield[j], formula)
                    else:
                        deal_mdamage(btlfield[i], btlfield[j], formula)
                    if btlfield[j].HP <= 0:
                        disTeam[btlfield[j].team] += 1
                        if btlfield[j].ROW() == 0:
                            blockers[btlfield[j].team] -= 1
                    break
                j += 1

            if disTeam[0] < 5 and disTeam[1] < 5:
                i += 1
            else:
                break


    if disTeam[0] == 5:
        for x in subject1:
            x.team = -1
        for x in subject2:
            x.team = 0
            x.HP = x.maxHP()
    else:
        for x in subject2:
            x.team = -1
        for x in subject1:
            x.team = 0
            x.HP = x.maxHP()


# -----------------------------------------------------------------
# damage methods
# -----------------------------------------------------------------
# application of the physical formulas of damage
def deal_pdamage(attacker, defender, formula):
    if formula == 0:
        defender.HP -= int(max(0.8, float((1+attacker.PA())/(1.0+defender.PD())))*attacker.PA()*3.0)
    if formula == 1:
        base_damage = int(attacker.PA() + float((attacker.PA() + 99) / 32) * float((attacker.PA() * 99) / 32))
        defender.HP -= (attacker.PA() * (512 - defender.PD()) * base_damage) / (16 * 512)
    if formula == 2:
        defender.HP -= int(84*((1+attacker.PA())/(1.0+defender.PD()))+2)
    if formula == 3:
        defender.HP -= 100/(1+defender.PD())

# application of the magical formulas of damage
def deal_mdamage(attacker, defender, formula):
    if formula == 0:
        defender.HP -= int(max(0.8, float((1+attacker.MA())/(1+defender.MD())))*attacker.MA()*3.0)
    if formula == 1:
        base_damage = int(6 * (attacker.MA() + 99))
        defender.HP -= (attacker.MA() * (512 - defender.MD()) * base_damage) / (16 * 512)
    if formula == 2:
        defender.HP -= int(84*((1+attacker.PA())/(1.0+defender.PD()))+2)
    if formula == 3:
        defender.HP -= 100/(1+defender.MD())