def sinTheta(opp: float, hyp: float) -> float:
    if hyp == 0 or (opp == 0 and hyp == 0) :
        raise ValueError("Values can't be null!")
    return opp/hyp

def cosTheta(adj: float, hyp: float) -> float:
    if hyp == 0 or (adj == 0 and hyp == 0) :
        raise ValueError("Values can't be null!")
    return adj/hyp
