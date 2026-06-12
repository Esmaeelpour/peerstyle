import os
import sys
from pathlib import Path

# Add src to sys.path for testing without installation
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

import matplotlib.pyplot as plt
import peerstyle

def test_style_application():
    print("Testing style application...")
    try:
        peerstyle.use_style("custom_style")
        print("Successfully applied 'custom_style'")
        
        # Check if some parameters are set as expected
        # axes.labelsize: 8 in custom_style.mplstyle
        assert plt.rcParams['axes.labelsize'] == 8
        print("Verified axes.labelsize == 8")
        
    except Exception as e:
        print(f"Failed to apply style: {e}")
        exit(1)

def test_style_path_exists():
    path = peerstyle.get_style_path("custom_style")
    print(f"Checking style path: {path}")
    assert path.exists()
    print("Style path exists.")

if __name__ == "__main__":
    test_style_path_exists()
    test_style_application()
    print("All tests passed!")
