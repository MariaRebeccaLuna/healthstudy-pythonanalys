import matplotlib.pyplot as plt
#import numpy as np
from sklearn.linear_model import LinearRegression

class HealthAnalyzer:

    def __init__(self, df):
        self.df = df

    def plot_bp_distribution(self):

        plt.figure()

        plt.hist(
            self.df["systolic_bp"],
            bins=15,
            edgecolor="black",
            rwidth=0.9
        )

        plt.xlabel("Systolic BP")
        plt.ylabel("Antalet personer (st)")
        plt.title("Fördelning av Systolic BP")

        plt.show()

    def plot_bp_vs_age(self):

        plt.figure()

        plt.scatter(
            self.df["age"],
            self.df["systolic_bp"],
            alpha=0.7
        )

        plt.xlabel("Ålder")
        plt.ylabel("Systolic BP")
        plt.title("Sambandet mellan ålder och systolic bp")

        plt.show()

    def linear_regression_bp(self):

        x = self.df[["age", "weight"]].values
        y = self.df["systolic_bp"].values

        model = LinearRegression()
        model.fit(x, y)

        print("Regressionskoefficienter:", model.coef_)
        print("Intercept:", model.intercept_)

        return model