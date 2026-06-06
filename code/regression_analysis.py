import pandas as pd
import statsmodels.api as sm
import matplotlib.pyplot as plt

# -----------------------------
# Load Dataset
# -----------------------------
df = pd.read_csv(r"E:/SwiggybSJames.csv")

# Remove unwanted spaces from column names
df.columns = df.columns.str.strip()

# -----------------------------
# Define Target Variable
# -----------------------------
y = df["TotalAssets"]

# -----------------------------
# Define Predictor Variables
# -----------------------------
X = df[[
    "EquityCapital",
    "Reserves",
    "Borrowings",
    "OtherLiabilities",
    "Deposits",
    "CWIP",
    "Investments",
    "OtherAssets",
    "TAD"
]]

# Add Intercept
X = sm.add_constant(X)

# -----------------------------
# Build OLS Regression Model
# -----------------------------
model = sm.OLS(y, X).fit()

# -----------------------------
# Model Summary
# -----------------------------
print("=" * 60)
print("OLS REGRESSION SUMMARY")
print("=" * 60)

print(model.summary())

print("\n")

print("=" * 60)
print("KEY MODEL METRICS")
print("=" * 60)

print(f"R² Score           : {model.rsquared:.4f}")
print(f"Adjusted R²        : {model.rsquared_adj:.4f}")
print(f"F Statistic        : {model.fvalue:.4f}")
print(f"Prob (F Statistic) : {model.f_pvalue:.6f}")

print("\n")

# -----------------------------
# Regression Coefficients
# -----------------------------
coef = model.params.drop("const", errors="ignore")

# Sort for better visualization
coef = coef.sort_values()

# Print coefficients
print("=" * 60)
print("REGRESSION COEFFICIENTS")
print("=" * 60)

print(coef)

# -----------------------------
# Visualization
# -----------------------------
plt.figure(figsize=(10,6))

plt.barh(
    coef.index,
    coef.values
)

plt.title(
    "Regression Coefficients - Swiggy Financial Statement Analysis",
    fontsize=14
)

plt.xlabel(
    "Coefficient Value",
    fontsize=12
)

plt.ylabel(
    "Financial Variables",
    fontsize=12
)

plt.grid(
    axis="x",
    linestyle="--",
    alpha=0.4
)

plt.tight_layout()

plt.savefig(
    "regression_coefficients.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()

# -----------------------------
# Actual vs Predicted Plot
# -----------------------------

predictions = model.predict(X)

plt.figure(figsize=(7,7))

plt.scatter(
    y,
    predictions
)

plt.plot(
    [y.min(), y.max()],
    [y.min(), y.max()],
    'r--'
)

plt.xlabel("Actual Total Assets")

plt.ylabel("Predicted Total Assets")

plt.title("Actual vs Predicted Values")

plt.grid(alpha=0.3)

plt.tight_layout()

plt.savefig(
    "actual_vs_predicted.png",
    dpi=300
)

plt.show()
