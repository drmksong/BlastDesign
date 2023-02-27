
# charge concentration with respect to burden
# cc = (1.05-0.23)/(0.9-0.2)*b+0
def cc_b(b: float) -> float:
    return (1.05-0.23)/(0.9-0.2)*(b-0.2)+0.23

# charge concentration with respect to distance (C-C)
# cc = (0.96-0.21)/(0.45-0.1)*d+0.1


def cc_d(d: float) -> float:
    return (0.96-0.21)/(0.45-0.1)*(d-0.1)+0.21
