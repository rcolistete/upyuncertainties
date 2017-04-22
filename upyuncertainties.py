import math

class ufloat:
    nominal_value = 0.0
    std_dev = 0.0

    def __init__(self, nominal_value=0.0, std_dev=0.0):
        self.nominal_value = nominal_value
        self.std_dev = abs(float(std_dev))

    # Operator overloads :

    def __str__(self):
        return '%r+/-%r' % (self.nominal_value, self.std_dev)

    __repr__ = __str__

    def __pos__(self):
        return self

    def __neg__(self):
        return ufloat(-self.nominal_value, self.std_dev)

    def __eq__(self, v):
        print("eq rodou")
        if type(v) == ufloat:
            return (self.nominal_value == v.nominal_value) and (self.std_dev == v.std_dev)
        return False

    def __add__(self, v):
        if type(v) == ufloat:
            return ufloat(self.nominal_value + v.nominal_value, (self.std_dev**2 + v.std_dev**2)**0.5)
        try:
            c = float(v)
        except:
            return NotImplemented
        return ufloat(self.nominal_value + v, self.std_dev)

    def __sub__(self, v):
        return self + (-v)

    def __mul__(self, v):
        if type(v) == ufloat:
            f = self.nominal_value*v.nominal_value
            return ufloat(f, f*((self.std_dev/self.nominal_value)**2 + (v.std_dev/v.nominal_value)**2)**0.5)
        try:
            c = float(v)
        except:
            return NotImplemented
        return ufloat(self.nominal_value*v, self.std_dev*v)

    def __truediv__(self, v):
        if type(v) == ufloat:
            return self.__mul__(v.reciprocal())
        try:
            c = float(v)
        except:
            return NotImplemented
        return ufloat(self.nominal_value/v, self.std_dev/v)

    __div__ = __truediv__

    # Methods :

    def reciprocal(self):
        return ufloat(1./self.nominal_value, self.std_dev/(self.nominal_value**2))

    def abs(self):
        return ufloat(abs(self.nominal_value), self.std_dev)

    def pow(self, n):
        if type(n) == ufloat:
            return NotImplemented
        try:
            c = float(n)
        except:
            return NotImplemented
        f = self.nominal_value**n
        return ufloat(f, f*n*(self.std_dev/self.nominal_value)) 

    def sqrt(self):
        return self.pow(0.5)

    def exp(self):
        f = math.exp(self.nominal_value)
        return ufloat(f, f*self.std_dev) 

    def powbase(self, base):
        if type(base) == ufloat:
            return NotImplemented
        try:
            c = float(base)
        except:
            return NotImplemented
        v = self*math.log(base)
        return v.exp()

    def log2(self):
        return ufloat(math.log2(self.nominal_value), self.std_dev/self.nominal_value*math.log(2)) 

    def log10(self):
         return ufloat(math.log10(self.nominal_value), self.std_dev/(self.nominal_value*math.log(10))) 

    def log(self,base=None):
        if base == None:
            return ufloat(math.log(self.nominal_value), self.std_dev/self.nominal_value) 
        if type(n) == ufloat:
            return NotImplemented
        try:
            c = float(base)
        except:
            return NotImplemented
        return ufloat(math.log(self.nominal_value,base), self.std_dev/(self.nominal_value*math.log(base))) 

    def sin(self):
        return ufloat(math.sin(self.nominal_value), math.cos(self.nominal_value)*self.std_dev) 

    def cos(self):
        return ufloat(math.cos(self.nominal_value), math.sin(self.nominal_value)*self.std_dev)

    def tan(self):
        return ufloat(math.tan(self.nominal_value), (1/math.cos(self.nominal_value)**2)*self.std_dev) 

