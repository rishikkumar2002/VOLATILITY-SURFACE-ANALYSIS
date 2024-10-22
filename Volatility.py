# -*- coding: utf-8 -*-
"""Untitled9.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1f94j9_bvrQeOzykG-TmD8IIZJneF0drC
"""

from google.colab import drive
import pandas as pd
drive.mount('/content/drive') #load data through google drive
data1 = pd.read_csv('/content/drive/My Drive/synthetic-dataset1.csv')
data2 = pd.read_csv('/content/drive/My Drive/synthetic-dataset2.csv')

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

def polynomial_fit(x, a, b, c):
    return a * x**2 + b * x + c

def fit_surface(data):
    coef, _ = curve_fit(polynomial_fit, data['STRIKE'], data['IMPLIED_VOL'])
    return coef

coeffs1 = fit_surface(data1)
coeffs2 = fit_surface(data2)

def plot_surface(data, coeffs):
    plt.scatter(data['STRIKE'], data['IMPLIED_VOL'], label='Data Points')
    x_values = np.linspace(min(data['STRIKE']), max(data['STRIKE']), 100)
    y_values = polynomial_fit(x_values, *coeffs)
    plt.plot(x_values, y_values, color='red', label='Fitted')
    plt.xlabel('Strike Price')
    plt.ylabel('Implied Volatility')
    plt.title('Implied Volatility vs Strike')
    plt.legend()
    plt.show()

plot_surface(data1, coeffs1)
plot_surface(data2, coeffs2)

from mpl_toolkits.mplot3d import Axes3D
def surface_fit(data):
    def poly(xy, a, b, c, d, e, f):
        x, y = xy[:, 0], xy[:, 1]
        return a * x**2 + b * y**2 + c * x * y + d * x + e * y + f
    xy_data = np.column_stack((data['STRIKE'], data['YEARS_TO_EXPIRY']))

    z_data = data['IMPLIED_VOL']

    coef, _ = curve_fit(poly, xy_data, z_data)
    return coef

surface_coeffs1 = surface_fit(data1)
surface_coeffs2 = surface_fit(data2)

def surface_function(xy, a, b, c, d, e, f):
        x, y = xy
        return a * x**2 + b * y**2 + c * x * y + d * x + e * y + f
        xy_data = np.column_stack((data['STRIKE'], data['YEARS_TO_EXPIRY']))
        z_data = data['IMPLIED_VOL']

        coef, _ = curve_fit(surface_function, xy_data, z_data)
        return coef

def plot_surface(data, coeffs):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    x_values = np.linspace(min(data['STRIKE']), max(data['STRIKE']), 100)
    y_values = np.linspace(min(data['YEARS_TO_EXPIRY']), max(data['YEARS_TO_EXPIRY']), 100)
    x_mesh, y_mesh = np.meshgrid(x_values, y_values)

    xy_mesh = np.column_stack((x_mesh.flatten(), y_mesh.flatten()))
    z_values = surface_function((x_mesh, y_mesh), *coeffs)

    ax.scatter(data['STRIKE'], data['YEARS_TO_EXPIRY'], data['IMPLIED_VOL'], label='Data Points')
    ax.plot_surface(x_mesh, y_mesh, z_values, alpha=0.5,cmap = 'viridis', label='Fitted Surface')

    ax.set_xlabel('Strike Price')
    ax.set_ylabel('Years to Expiry')
    ax.set_zlabel('Implied Volatility')
    ax.set_title('Implied Volatility Surface')

    plt.show()

surface_coeffs1

plot_surface(data1, surface_coeffs1)

plot_surface(data2,surface_coeffs2)

def get_implied_volatility(strike, years_to_expiry, coeffs):
    implied_vol = surface_function((strike, years_to_expiry), *coeffs)
    return implied_vol

strike = 126
years_to_expiry = 0.122
implied_volatility = get_implied_volatility(strike, years_to_expiry, surface_coeffs1)
print("Implied Volatility:", implied_volatility)

import numpy as np
import plotly.graph_objects as go
from scipy.optimize import curve_fit

def surface_fit(data):
    def poly(xy, a, b, c, d, e, f,g,h):
        x, y = xy[:, 0], xy[:, 1]
        return a * x**2 + b * y**2 + c * x * y + d * x + e * y + f + g*x**3 + h*x**4

    xy_data = np.column_stack((data['STRIKE'], data['YEARS_TO_EXPIRY']))
    z_data = data['IMPLIED_VOL']

    coef, _ = curve_fit(poly, xy_data, z_data)
    return coef

surface_coeffs1 = surface_fit(data1)
surface_coeffs2 = surface_fit(data2)

def surface_function(xy, a, b, c, d, e, f,g,h):
    x, y = xy
    return a * x**2 + b * y**2 + c * x * y + d * x + e * y + f + g*x**3 + h*x**4

def plot_surface(data, coeffs):
    x_values = np.linspace(min(data['STRIKE']), max(data['STRIKE']), 100)
    y_values = np.linspace(min(data['YEARS_TO_EXPIRY']), max(data['YEARS_TO_EXPIRY']), 100)
    x_mesh, y_mesh = np.meshgrid(x_values, y_values)

    z_values = surface_function((x_mesh, y_mesh), *coeffs)

    fig = go.Figure(data=[
        go.Scatter3d(x=data['STRIKE'], y=data['YEARS_TO_EXPIRY'], z=data['IMPLIED_VOL'], mode='markers', name='Data Points'),
        go.Surface(x=x_mesh, y=y_mesh, z=z_values, opacity=0.8, colorscale='plasma', name='Fitted Surface')
    ])
    fig.update_layout(scene=dict(
        xaxis_title='Strike',
        yaxis_title='Years to Expiry',
        zaxis_title='Implied Volatility'
    ))


    fig.show()


plot_surface(data1, surface_coeffs1)

plot_surface(data2, surface_coeffs2)

import numpy as np
import plotly.graph_objects as go
from scipy.optimize import curve_fit

def surface_fit(data):
    def poly(xy, a, b, c, d, e):
        x, y = xy[:, 0], xy[:, 1]
        return a + b*x + c*x**2 + d*y + e*y**2

    xy_data = np.column_stack((data['STRIKE'], data['YEARS_TO_EXPIRY']))
    z_data = data['IMPLIED_VOL']

    coef, _ = curve_fit(poly, xy_data, z_data)
    return coef

surface_coeffs1 = surface_fit(data1)
surface_coeffs2 = surface_fit(data2)

def surface_function(xy, a, b, c, d, e):
    x, y = xy
    return a + b*x + c*x**2 + d*y + e*y**2

def plot_surface(data, coeffs):
    x_values = np.linspace(min(data['STRIKE']), max(data['STRIKE']), 100)
    y_values = np.linspace(min(data['YEARS_TO_EXPIRY']), max(data['YEARS_TO_EXPIRY']), 100)
    x_mesh, y_mesh = np.meshgrid(x_values, y_values)

    z_values = surface_function((x_mesh, y_mesh), *coeffs)

    fig = go.Figure(data=[
        go.Scatter3d(x=data['STRIKE'], y=data['YEARS_TO_EXPIRY'], z=data['IMPLIED_VOL'], mode='markers', name='Data Points'),
        go.Surface(x=x_mesh, y=y_mesh, z=z_values, opacity=0.8, colorscale='viridis', name='Fitted Surface')
    ])
    fig.update_layout(scene=dict(
        xaxis_title='Strike',
        yaxis_title='Years to Expiry',
        zaxis_title='Implied Volatility'
    ))


    fig.show()


plot_surface(data1, surface_coeffs1)

plot_surface(data2, surface_coeffs2)

import numpy as np
import pandas as pd
from sklearn.decomposition import PCA
from scipy.interpolate import griddata
import plotly.graph_objects as go

# Load the data from CSV file


# Step 1: Data Preparation
# Separate features (IV, strike, expiry) and standardize them
X = data1[['IMPLIED_VOL', 'STRIKE', 'YEARS_TO_EXPIRY']].values
X_standardized = (X - np.mean(X, axis=0)) / np.std(X, axis=0)

# Step 2: PCA
# Assuming you want to keep all principal components
pca = PCA()
pca.fit(X_standardized)

# Step 3: Select Components
# Determine how many components to keep based on explained variance
cumulative_variance_ratio = np.cumsum(pca.explained_variance_ratio_)
num_components = np.argmax(cumulative_variance_ratio >= 0.95) + 1  # Keep components explaining at least 95% variance

# Re-run PCA with selected number of components
pca = PCA(n_components=num_components)
pca.fit(X_standardized)

# Step 4: Surface Reconstruction
# Transform data into principal component space
X_pca = pca.transform(X_standardized)

# Transform back to the original space
X_reconstructed = pca.inverse_transform(X_pca)

# Step 5: Interpolation/Extrapolation
# Perform interpolation/extrapolation to fill in missing values and create a smooth surface
iv_reconstructed = X_reconstructed[:, 0]
strike_reconstructed = X_reconstructed[:, 1]
expiry_reconstructed = X_reconstructed[:, 2]

# Create a meshgrid for strike and expiry
strike_min, strike_max = np.min(strike_reconstructed), np.max(strike_reconstructed)
expiry_min, expiry_max = np.min(expiry_reconstructed), np.max(expiry_reconstructed)
strike_grid, expiry_grid = np.linspace(strike_min, strike_max, 100), np.linspace(expiry_min, expiry_max, 100)
strike_mesh, expiry_mesh = np.meshgrid(strike_grid, expiry_grid)

# Interpolate IV values
iv_surface = griddata((strike_reconstructed, expiry_reconstructed), iv_reconstructed, (strike_mesh, expiry_mesh), method='cubic')

# Create an interactive 3D plot
fig = go.Figure(data=[go.Surface(x=strike_mesh, y=expiry_mesh, z=iv_surface)])
fig.update_layout(title='Volatility Surface', scene=dict(xaxis_title='Strike', yaxis_title='Expiry', zaxis_title='IV'))
fig.show()

import numpy as np
from scipy.optimize import minimize
import pandas as pd



# SVI model function
def svi_model(params, strike, t):
    a, b, rho = params
    return a + b * (rho * (np.log(strike) + np.sqrt(np.log(strike) ** 2 + 1)))

# Objective function to minimize
def objective_function(params, data):
    errors = []
    for i, row in data.iterrows():
        implied_vol = row['IMPLIED_VOL']
        strike = row['STRIKE']
        t = row['YEARS_TO_EXPIRY']
        model_vol = svi_model(params, strike, t)
        errors.append((implied_vol - model_vol) ** 2)
    return np.mean(errors)

# Initial guess for SVI parameters
initial_guess = [0.2, 0.5, -0.5]

# Minimize the objective function to fit the SVI parameters
result = minimize(objective_function, initial_guess, args=(data1,), method='Nelder-Mead')

# Extract fitted SVI parameters
fitted_params = result.x
print("Fitted SVI parameters:", fitted_params)

import numpy as np

# Sample volatility skew data
theta_values = data1['YEARS_TO_EXPIRY']  # Sample values of theta
vol_skew_values = data1['IMPLIED_VOL']

# Calculate the derivative of the volatility skew with respect to theta
vol_skew_derivative = np.gradient(vol_skew_values, theta_values)

# Check conditions from Theorem 4.2
condition_1 = theta_values * vol_skew_derivative * (1 + np.abs(0.5)) < 4
condition_2 = 0.5 * theta_values * vol_skew_derivative * (1 + np.abs(0.5)) <= 4

# Check if conditions are satisfied for all positive values of theta
if np.all(condition_1) and np.all(condition_2):
    print("The volatility surface is free of butterfly arbitrage.")
else:
    print("The volatility surface may contain butterfly arbitrage.")

import numpy as np
from scipy.interpolate import griddata
import matplotlib.pyplot as plt

# Assuming you have loaded your dataset into arrays implied_vol, strike, and years_to_expiry
strike = data2['STRIKE']
years_to_expiry = data2['YEARS_TO_EXPIRY']
implied_vol = data2['IMPLIED_VOL']
# Define the grid for interpolation
strike_grid = np.linspace(min(strike), max(strike), 100)  # adjust 100 as needed
years_to_expiry_grid = np.linspace(min(years_to_expiry), max(years_to_expiry), 100)  # adjust 100 as needed
strike_grid, years_to_expiry_grid = np.meshgrid(strike_grid, years_to_expiry_grid)

# Perform cubic spline interpolation
implied_vol_surface = griddata((strike, years_to_expiry), implied_vol, (strike_grid, years_to_expiry_grid), method='cubic')

# Plot the interpolated surface
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(strike_grid, years_to_expiry_grid, implied_vol_surface, cmap='viridis')
ax.set_xlabel('Strike')
ax.set_ylabel('Years to Expiry')
ax.set_zlabel('Implied Volatility')
plt.title('Implied Volatility Surface')
plt.show()

import numpy as np
from scipy.interpolate import Rbf
import matplotlib.pyplot as plt

# Assuming you have loaded your dataset into arrays implied_vol, strike, and years_to_expiry
strike = data1['STRIKE']
years_to_expiry = data1['YEARS_TO_EXPIRY']
implied_vol = data1['IMPLIED_VOL']

# Define the grid for interpolation
strike_grid = np.linspace(min(strike), max(strike), 100)  # adjust 100 as needed
years_to_expiry_grid = np.linspace(min(years_to_expiry), max(years_to_expiry), 100)  # adjust 100 as needed
strike_grid, years_to_expiry_grid = np.meshgrid(strike_grid, years_to_expiry_grid)

# Perform RBF interpolation
rbf = Rbf(strike, years_to_expiry, implied_vol, function='cubic')
implied_vol_surface = rbf(strike_grid, years_to_expiry_grid)

# Plot the interpolated surface
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(strike_grid, years_to_expiry_grid, implied_vol_surface, cmap='viridis')
ax.set_xlabel('Strike')
ax.set_ylabel('Years to Expiry')
ax.set_zlabel('Implied Volatility')
plt.title('Implied Volatility Surface')
plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Sample data (replace with your fitted SVI parameters)
fitted_params = [1.386939,    0.0602554 , -2.12345343]

# Define grid of strike prices and time to expiry values
strike_range = data1['STRIKE'] # Adjust as needed
expiry_range = data1['YEARS_TO_EXPIRY']  # Adjust as needed

# Function to calculate implied volatility surface
def svi_surface(params, strikes, expiries):
    surface = np.zeros((len(strikes), len(expiries)))
    for i, strike in enumerate(strikes):
        for j, expiry in enumerate(expiries):
            surface[i, j] = svi_model(params, strike, expiry)
    return surface

# Calculate implied volatility surface
implied_vol_surface = svi_surface(fitted_params, strike_range, expiry_range)

# Plot implied volatility surface
strike_grid, expiry_grid = np.meshgrid(strike_range, expiry_range)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(strike_grid, expiry_grid, implied_vol_surface.T, cmap='viridis')
ax.set_xlabel('Strike Price')
ax.set_ylabel('Years to Expiry')
ax.set_zlabel('Implied Volatility')
ax.set_title('Implied Volatility Surface')
plt.show()

import numpy as np
from scipy.interpolate import griddata

strike = data1['STRIKE']
mat = data1['YEARS_TO_EXPIRY'].values
iv = data1['IMPLIED_VOL'].values

s, m = np.meshgrid(np.linspace(min(strike), max(strike), 100), np.linspace(min(mat), max(mat), 100))

interpol = griddata((strike, mat), iv, (s, m), method='linear')

fig = go.Figure(data=[go.Surface(z=interpol, x=s, y=m)])
fig.update_layout(title='Interpolated Surface Plot',scene=dict(xaxis_title='Strike',yaxis_title='Years to Expiry',zaxis_title='Implied Volatility'))

fig.add_scatter3d(x=data1['STRIKE'], y=data1['YEARS_TO_EXPIRY'], z=data1['IMPLIED_VOL'], mode='markers')

fig.show()

import numpy as np
from scipy.interpolate import griddata
import plotly.graph_objects as go

remove = [0, 3, 4]

mask = np.ones(len(strike), dtype=bool)
mask[remove] = False

filtered_strike = data1['STRIKE'][mask]
filtered_iv = data1['IMPLIED_VOL'][mask]
filtered_mat = data1['YEARS_TO_EXPIRY'][mask]

s2, m2 = np.meshgrid(np.linspace(min(filtered_strike), max(filtered_strike), 25),
                     np.linspace(min(filtered_mat), max(filtered_mat), 25))

interpol = griddata((filtered_strike, filtered_mat), filtered_iv, (s2, m2), method='cubic')

fig = go.Figure(data=[go.Surface(z=interpol, x=s2, y=m2)])
fig.update_layout(title='Interpolated Surface Plot',scene=dict(xaxis_title='Strike',yaxis_title='Years to Expiry',zaxis_title='Implied Volatility'))


fig.add_scatter3d(x=filtered_strike, y=filtered_mat, z=filtered_iv, mode='markers')

fig.show()