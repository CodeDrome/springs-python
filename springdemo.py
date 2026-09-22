import spring


def main():

    print("default Spring instance")
    print("-----------------------")
    s1 = spring.Spring()
    print(s1)

    print()

    # length
    print("setting e, calculating length")
    print("-----------------------------")
    s2 = spring.Spring(rest_length_m=0.38)
    s2.extension_m = 0.09
    s2.calc_length()
    print(s2)

    print()

    # force
    print("setting e, calculating F")
    print("------------------------")
    s3 = spring.Spring(spring_constant_Nm=4)
    s3.extension_m = 0.1
    s3.calc_force_N()
    print(s3)

    print()

    # spring constant
    print("setting e and F, calculating k")
    print("------------------------------")
    s4 = spring.Spring()
    s4.extension_m = 0.22
    s4.force_N = 0.66
    s4.calc_spring_constant_Nm()
    print(s4)

    print()

    # extension
    s5 = spring.Spring(spring_constant_Nm=3.2)
    print("setting F, calculating e")
    print("------------------------")
    s5.force_N = 0.4
    s5.calc_extension_m()
    print(s5)


if __name__ == "__main__":

    main()