# statistics.py

import pandas as pd

def statistical_analysis(df):

    print("\n📊 Statistical Analysis")

    mean_values = df.mean(numeric_only=True)
    print("\nMean Values:\n", mean_values)

    median_values = df.median(numeric_only=True)
    print("\nMedian Values:\n", median_values)

    mode_values = df.mode(numeric_only=True).iloc[0]
    print("\nMode Values:\n", mode_values)

    std_values = df.std(numeric_only=True)
    print("\nStandard Deviation:\n", std_values)

    var_values = df.var(numeric_only=True)
    print("\nVariance:\n", var_values)

    corr_matrix = df.corr(numeric_only=True)
    print("\nCorrelation Matrix:\n", corr_matrix)

    stats_report = pd.DataFrame({
        "Mean": mean_values,
        "Median": median_values,
        "Mode": mode_values,
        "Std Dev": std_values,
        "Variance": var_values
    })

    stats_report.to_csv("output/statistics_report.csv")
    corr_matrix.to_csv("output/correlation_matrix.csv")

    print("\n✅ Statistical Analysis Files Saved Successfully!")

    return {
        "Mean": mean_values,
        "Median": median_values,
        "Mode": mode_values,
        "Std Dev": std_values,
        "Variance": var_values,
        "Correlation Matrix": corr_matrix
    }
