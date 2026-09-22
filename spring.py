
class Spring(object):

    def __init__(self, 
                 radius_m=0.1, 
                 turns=8, 
                 rest_length_m=0.25, 
                 spring_constant_Nm=0.0):

        super().__init__()

        self._radius_m = radius_m
        self._turns = turns
        self._rest_length_m = rest_length_m
        self._length_m = rest_length_m

        self._spring_constant_Nm = spring_constant_Nm

        self._force_N = 0.0
        self._extension_m = 0.0


    # getters only

    @property
    def radius_m(self):
        return self._radius_m
    
    @property
    def turns(self):
        return self._turns
    
    @property
    def rest_length_m(self):
        return self._rest_length_m
    
    @property
    def length_m(self):
        return self._length_mnt_Nm
    
    # getters and setters

    @property
    def force_N(self):
        return self._force_N
    
    @force_N.setter 
    def force_N(self, force_N):
            self._force_N = force_N
    
    @property
    def extension_m(self):
        return self._extension_m
        
    @extension_m.setter 
    def extension_m(self, extension_m):
            self._extension_m = extension_m
            self.calc_length()

    @property
    def spring_constant_Nm(self):
        return self._spring_constant_Nm
    
    @spring_constant_Nm.setter 
    def spring_constant_Nm(self, spring_constant_Nm):
            self._spring_constant_Nm = spring_constant_Nm


    def __str__(self):

        str = []

        str.append(f"radius           {self.radius_m}m\n")
        str.append(f"rest length      {self._rest_length_m}m\n")
        str.append(f"turns            {self._turns}\n\n")

        str.append(f"force            {self.force_N}N\n")
        str.append(f"extension        {self._extension_m}m\n")
        str.append(f"spring constant  {self._spring_constant_Nm}Nm\n\n")

        str.append(f"length           {self._length_m}m")

        return "".join(str)
    
    
    # methods
    
    def calc_force_N(self) -> None:

        if self._spring_constant_Nm > 0 and self._extension_m > 0:
            self._force_N =  self._spring_constant_Nm * self._extension_m
        else:             
             raise ValueError("spring_constant_Nm and extension_m must be more than 0")


    def calc_extension_m(self) -> None:

        if self._force_N > 0 and self._spring_constant_Nm > 0:        
            self._extension_m = self._force_N / self._spring_constant_Nm
            self.calc_length()
        else:             
             raise ValueError("force_N and spring_constant_Nm must be more than 0")


    def calc_spring_constant_Nm(self) -> None:

        if self._force_N > 0 and self._extension_m > 0:
            self._spring_constant_Nm = self._force_N / self._extension_m
        else:
             raise ValueError("force_N and extension_m must be more than 0")
    

    def calc_length(self):

        if self._rest_length_m > 0 and self._extension_m > 0:
            self._length_m = self._rest_length_m + self._extension_m
        else:
             raise ValueError("rest_length_m and extension_m must be more than 0")