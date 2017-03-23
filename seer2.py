#   seer2.py
#   python 3.5

#   Simple demo of super-basic neural-network weather prediction.
#   This version is re-written and very cleaned-up.

#   Chris Bugg
#   Created: 2/1/15
#   Updated: 3/23/17

#   TODO: Add other things to track
#   TODO: Add API to fetch WX data
#   TODO: Create dynamic version

import random


class Seer:

    # Multiplier models
    rawlins_model = [.1]
    laramie_model = [.1]
    cheyenne_model = [.1]

    # Training conditions
    training_conditions_rawlins = [80]
    training_conditions_laramie = [70]
    training_conditions_cheyenne = [60]

    # Training actual forecast
    training_forecast = [75.0]

    # Validation conditions
    validation_conditions_rawlins = [60]
    validation_conditions_laramie = [50]
    validation_conditions_cheyenne = [40]

    # Validation actual forecast
    validation_forecast = [55.0]

    # Predicted forecast
    predicted_forecast = [10.0]

    # Low chances, used to help randomness
    low_chance = [0, 0, 0, 0.0001, -0.0001]

    # Constructor
    def __init__(self):

        # Initial
        self.initial()

        # Training
        self.training()

        # Validation
        self.validation()

    # Update model values based on actual forecast
    def update_model(self):

        # If our prediction was too low, bump up model weights
        if self.training_forecast[0] > self.predicted_forecast[0]:

            self.rawlins_model[0] = self.rawlins_model[0] * 1.01 + random.choice(self.low_chance)
            self.laramie_model[0] = self.laramie_model[0] * 1.01 + random.choice(self.low_chance)
            self.cheyenne_model[0] = self.cheyenne_model[0] * 1.01 + random.choice(self.low_chance)

        # If our prediction was too high, bump down model weights
        elif self.training_forecast[0] < self.predicted_forecast[0]:

            self.rawlins_model[0] = self.rawlins_model[0] * 0.99 + random.choice(self.low_chance)
            self.laramie_model[0] = self.laramie_model[0] * 0.99 + random.choice(self.low_chance)
            self.cheyenne_model[0] = self.cheyenne_model[0] * 0.99 + random.choice(self.low_chance)

    # Make prediction based on model values
    def training_predict(self):

        self.predicted_forecast[0] = self.training_conditions_rawlins[0] * self.rawlins_model[0] + \
                                    self.training_conditions_laramie[0] * self.laramie_model[0] + \
                                    self.training_conditions_cheyenne[0] * self.cheyenne_model[0]

    # Make prediction based on model values
    def validation_predict(self):
        self.predicted_forecast[0] = self.validation_conditions_rawlins[0] * self.rawlins_model[0] + \
                                     self.validation_conditions_laramie[0] * self.laramie_model[0] + \
                                     self.validation_conditions_cheyenne[0] * self.cheyenne_model[0]

    # Make initial prediction based on initial values
    def initial(self):

        print("--Initial Run--")

        # Print Current Conditions
        print("Current Conditions: ")
        print("Rawlins: " + str(self.training_conditions_rawlins))
        print("Laramie: " + str(self.training_conditions_laramie))
        print("Cheyenne: " + str(self.training_conditions_cheyenne))

        # Print Predicted Forecast
        print("Predicted Forecast Laramie: " + str(self.predicted_forecast))

        # Print Actual Forecast
        print("Actual Forecast Laramie: " + str(self.training_forecast))

    # Train model based on training data
    def training(self):

        # Training
        print("--Training...")

        # Number times to train
        iterations = 2000000

        # Loop x times and train the model
        for x in range(0, iterations):

            # Updated model based on actual forecast
            self.update_model()

            # Update prediction values based on updated model
            self.training_predict()

        print("--Training Run--")

        # Print Current Conditions
        print("Current Conditions: ")
        print("Rawlins: " + str(self.training_conditions_rawlins))
        print("Laramie: " + str(self.training_conditions_laramie))
        print("Cheyenne: " + str(self.training_conditions_cheyenne))

        # Print Predicted Forecast
        print("Predicted Forecast Laramie: " + str(self.predicted_forecast))

        # Print Actual Forecast
        print("Actual Forecast Laramie: " + str(self.training_forecast))

    # Test models' behavior on new data
    def validation(self):

        # Perform Prediction based on trained model
        self.validation_predict()

        print("--Validation Run--")

        # Print Current Conditions
        print("Current Conditions: ")
        print("Rawlins: " + str(self.validation_conditions_rawlins))
        print("Laramie: " + str(self.validation_conditions_laramie))
        print("Cheyenne: " + str(self.validation_conditions_cheyenne))

        # Print Predicted Forecast
        print("Predicted Forecast Laramie: " + str(self.predicted_forecast))

        # Print Actual Forecast
        print("Actual Forecast Laramie: " + str(self.validation_forecast))

Seer()
