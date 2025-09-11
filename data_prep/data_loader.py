import os
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import pandas as pd

# For reproducibility
np.random.seed(42)

# Matplotlib styles
mpl.rc('axes', labelsize=14)
mpl.rc('xtick', labelsize=12)
mpl.rc('ytick', labelsize=12)

# Save figure setup
CURRENT_DIR = os.path.dirname(__file__)
PROJECT_ROOT_DIR = os.path.abspath(os.path.join(CURRENT_DIR, "..", ".."))
CHAPTER_ID = "credit_risk_scoring"
IMAGES_PATH = os.path.join(PROJECT_ROOT_DIR, "images", CHAPTER_ID)
os.makedirs(IMAGES_PATH, exist_ok=True)

def save_fig(fig_id, tight_layout=True, fig_extension="png", resolution=300):
    """Saves a matplotlib figure to the project's images directory."""
    path = os.path.join(IMAGES_PATH, fig_id + "." + fig_extension)
    print(f"Saving figure: {path}")
    if tight_layout:
        plt.tight_layout()
    plt.savefig(path, format=fig_extension, dpi=resolution)


def load_loan_data() -> pd.DataFrame:
    # Get current file directory
    current_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Construct path to data folder relative to this file
    data_path = os.path.join(current_dir, "..", "data", "loan.csv")
    data_path = os.path.abspath(data_path)
    
    if not os.path.exists(data_path):
        raise FileNotFoundError(f"Data file not found at: {data_path}")
    
    return pd.read_csv(data_path)
