class Auto(object): pass
class FMixIn(object): pass
class RMixIn(object): pass
class AMixIn(object): pass


class ICE(Auto): pass
class MOTOR(Auto): pass


class F_ICE(ICE, FMixIn): pass
class R_ICE(ICE, RMixIn): pass
class A_ICE(ICE, AMixIn):
    def __repr__(self):
        return f"this is A_ICE"

class F_MOTOR(MOTOR, FMixIn): pass
class R_MOTOR(MOTOR, RMixIn): pass
class A_MOTOR(MOTOR, AMixIn): pass

sti = A_ICE()
print(type(sti))


