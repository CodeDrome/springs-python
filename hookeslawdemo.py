import hookeslaw


def main():
    
    print("Force from spring constant and extension\nF=k*e")
    
    spring_constant_Nm = 26
    extension_m = .022
    force_N = hookeslaw.force_N(spring_constant_Nm, extension_m)

    print(f"Spring constant k {spring_constant_Nm}N/m")
    print(f"Extension e       {extension_m}m")
    print(f"Force F           {force_N}N")

    print()

    print("Extension from force and spring constant\ne=F/k")
    force_N = 1.1
    spring_constant_Nm = 32
    extension_m = hookeslaw.extension_m(force_N, spring_constant_Nm)

    print(f"Force F           {force_N}N")
    print(f"Spring constant k {spring_constant_Nm}N/m")
    print(f"Extension e       {extension_m}m")

    print()

    print("Spring constant from force and extension\nk=F/e")
    force_N = 1.8
    extension_m = 0.3
    spring_constant_Nm = hookeslaw.spring_constant_Nm(force_N, extension_m)

    print(f"Force F           {force_N}N")
    print(f"Extension e       {extension_m}m")
    print(f"Spring constant k {spring_constant_Nm}N/m")


if __name__ == "__main__":

    main()