import pandas as pd

class Statistics:

    def calculate_basic_stats(self, df, variables):

# Detta beräknar statistiken för de valda variablerna. Hämtar från datasetet variablerna och analyserar sedan de.

        stats = pd.DataFrame({
        "mean": df[variables].mean(),
        "median": df[variables].median(),
        "min": df[variables].min(),
        "max": df[variables].max()
    })

        return stats