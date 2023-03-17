class Wine():
    def __init__(self, fixed_acidity=0, volatile_acidity=0, citric_acid=0, residual_sugar=0, chlorides=0, free_sulfur_dioxide=0, total_sulfur_dioxide=0, density=0, pH=0, sulphates=0, alcohol=0):
        self.fixed_acidity = fixed_acidity
        self.volatile_acidity = volatile_acidity
        self.citric_acid = citric_acid
        self.residual_sugar = residual_sugar
        self.chlorides = chlorides
        self.free_sulfur_dioxide = free_sulfur_dioxide
        self.total_sulfur_dioxide = total_sulfur_dioxide
        self.density = density
        self.pH = pH
        self.sulphates = sulphates
        self.alcohol = alcohol

   # Getters methods

    def get_fixed_acidity(self):
        return self.fixed_acidity

    def get_volatile_acidity(self):
        return self.volatile_acidity

    def get_citric_acid(self):
        return self.citric_acid

    def get_residual_sugar(self):
        return self.residual_sugar

    def get_chlorides(self):
        return self.chlorides

    def get_free_sulfur_dioxide(self):
        return self.free_sulfur_dioxide

    def get_total_sulfur_dioxide(self):
        return self.total_sulfur_dioxide

    def get_density(self):
        return self.density

    def get_pH(self):
        return self.pH

    def get_sulphates(self):
        return self.sulphates

    def get_alcohol(self):
        return self.alcohol

    # Setters methods
    def set_fixed_acidity(self, fixed_acidity):
        self.fixed_acidity = fixed_acidity

    def set_volatile_acidity(self, volatile_acidity):
        self.volatile_acidity = volatile_acidity

    def set_citric_acid(self, citric_acid):
        self.citric_acid = citric_acid

    def set_residual_sugar(self, residual_sugar):
        self.residual_sugar = residual_sugar

    def set_chlorides(self, chlorides):
        self.chlorides = chlorides

    def set_free_sulfur_dioxide(self, free_sulfur_dioxide):
        self.free_sulfur_dioxide = free_sulfur_dioxide

    def set_total_sulfur_dioxide(self, total_sulfur_dioxide):
        self.total_sulfur_dioxide = total_sulfur_dioxide

    def set_density(self, density):
        self.density = density

    def set_pH(self, pH):
        self.pH = pH

    def set_sulphates(self, sulphates):
        self.sulphates = sulphates

    def set_alcohol(self, alcohol):
        self.alcohol = alcohol

    def print_wine_attributes(self):
        print("\n\033[1mHere are the summary of entered inputs:\033[0m\n")
        print("\033[31mFixed Acidity:\033[0m", self.fixed_acidity)
        print("\033[31mVolatile Acidity:\033[0m", self.volatile_acidity)
        print("\033[31mCitric Acid:\033[0m", self.citric_acid)
        print("\033[31mResidual Sugar:\033[0m", self.residual_sugar)
        print("\033[31mChlorides:\033[0m", self.chlorides)
        print("\033[31mFree Sulfur Dioxide:\033[0m", self.free_sulfur_dioxide)
        print("\033[31mTotal Sulfur Dioxide:\033[0m",
              self.total_sulfur_dioxide)
        print("\033[31mDensity:\033[0m", self.density)
        print("\033[31mpH:\033[0m", self.pH)
        print("\033[31mSulphates:\033[0m", self.sulphates)
        print("\033[31mAlcohol:\033[0m", self.alcohol)
        print("\n")
