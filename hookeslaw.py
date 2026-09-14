
def force_N(spring_constant_Nm: float, extension_m: float) -> float:

    k = spring_constant_Nm
    e = extension_m

    return k * e


def extension_m(force_N: float, spring_constant_Nm: float) -> float:

    F = force_N
    k = spring_constant_Nm

    return F / k


def spring_constant_Nm(force_N: float, extension_m: float) -> float:

    F = force_N
    e = extension_m

    return F / e