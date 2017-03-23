#   seer.py
#   python 3.5

#   Simple demo of super-basic neural-network weather prediction

#   Chris Bugg
#   Created: 2/1/15
#   Updated: 3/23/17

import random


class Seer:

    # [Temp, Pressure (hPa), Wind Speed, Temp Multiplier, Precip Multiplier, Clouds Multiplier]
    rawlins = [65, .5, .75, .3, .3, .3]
    laramie = [75, .2, .5, .3, .3, .3]
    cheyenne = [80, .1, .25, .3, .3, .3]

    # Default values
    predicted_laramie = [75, .2, .5]

    low_chance = [0, 0, 0, .0001, -0.0001]

    def __init__(self):

        #2/24/15 noon - 4pm
        self.rawlins[0] = 36
        self.rawlins[1] = 1024.7
        self.rawlins[2] = 13

        self.laramie[0] = 28
        self.laramie[1] = 1025.4
        self.laramie[2] = 4

        self.cheyenne[0] = 39
        self.cheyenne[1] = 1019
        self.cheyenne[2] = 10

        actual_laramie = [38, 1019, 11]

        #actual_laramie = [65, .5, .75]

        print("Sample Laramie:")
        print(actual_laramie)

        self.predict()

        print("First Prediction:")
        print(self.predicted_laramie)

        iterations = 2000000

        for x in range(0, iterations):

            self.update_model(actual_laramie[0], actual_laramie[1], actual_laramie[2])

            self.predict()

            #print x, "th Prediction:"
            #print self.predicted_laramie

        print(str(iterations) + " Prediction:")
        print(self.predicted_laramie)

        # TRY FOR THE FUTURE!

        #updated_laramie = [75, .2, .5]
        updated_laramie = [15, 1028.8, 4]

        print("Actual Laramie:")
        print(updated_laramie)

        #print "Updated Others:"
        #2/23/15 noon - 4pm
        self.rawlins[0] = 11
        self.rawlins[1] = 1031.5
        self.rawlins[2] = 5

        self.laramie[0] = 10
        self.laramie[1] = 1029
        self.laramie[2] = 5

        self.cheyenne[0] = 14
        self.cheyenne[1] = 1029
        self.cheyenne[2] = 5

        print(self.rawlins)
        print(self.laramie)
        print(self.cheyenne)

        self.predict()

        print("Actual Forecast:")
        print(self.predicted_laramie)

    def update_model(self, currentTemp, currentPressure, currentWind):

        if currentTemp > self.predicted_laramie[0]:

            self.rawlins[3] = self.rawlins[3] * 1.01 + random.choice(self.low_chance)
            self.laramie[3] = self.laramie[3] * 1.01 + random.choice(self.low_chance)
            self.cheyenne[3] = self.cheyenne[3] * 1.01 + random.choice(self.low_chance)

        elif currentTemp < self.predicted_laramie[0]:

            self.rawlins[3] = self.rawlins[3] * 0.99 + random.choice(self.low_chance)
            self.laramie[3] = self.laramie[3] * 0.99 + random.choice(self.low_chance)
            self.cheyenne[3] = self.cheyenne[3] * 0.99 + random.choice(self.low_chance)

        if currentPressure > self.predicted_laramie[1]:

            self.rawlins[4] = self.rawlins[4] * 1.001 + random.choice(self.low_chance)
            self.laramie[4] = self.laramie[4] * 1.001 + random.choice(self.low_chance)
            self.cheyenne[4] = self.cheyenne[4] * 1.001 + random.choice(self.low_chance)

        elif currentPressure < self.predicted_laramie[1]:

            self.rawlins[4] = self.rawlins[4] * 0.999 + random.choice(self.low_chance)
            self.laramie[4] = self.laramie[4] * 0.999 + random.choice(self.low_chance)
            self.cheyenne[4] = self.cheyenne[4] * 0.999 + random.choice(self.low_chance)

        if currentWind > self.predicted_laramie[2]:

            self.rawlins[5] = self.rawlins[5] * 1.01 + random.choice(self.low_chance)
            self.laramie[5] = self.laramie[5] * 1.01 + random.choice(self.low_chance)
            self.cheyenne[5] = self.cheyenne[5] * 1.01 + random.choice(self.low_chance)

        elif currentWind < self.predicted_laramie[2]:

            self.rawlins[5] = self.rawlins[5] * 0.99 + random.choice(self.low_chance)
            self.laramie[5] = self.laramie[5] * 0.99 + random.choice(self.low_chance)
            self.cheyenne[5] = self.cheyenne[5] * 0.99 + random.choice(self.low_chance)

    def predict(self):

        self.predicted_laramie[0] = self.rawlins[0] * self.rawlins[3] + self.laramie[0] * self.laramie[3] + self.cheyenne[0] * self.cheyenne[3]

        self.predicted_laramie[1] = self.rawlins[1] * self.rawlins[4] + self.laramie[1] * self.laramie[4] + self.cheyenne[1] * self.cheyenne[4]

        self.predicted_laramie[2] = self.rawlins[2] * self.rawlins[5] + self.laramie[2] * self.laramie[5] + self.cheyenne[2] * self.cheyenne[5]

Seer()
