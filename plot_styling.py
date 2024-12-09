import os
import matplotlib as mpl

# Add PATH directories to Matplotlib's style library paths
effective_path = os.environ["PATH"]

# Split into individual directories
path_dirs = effective_path.split(os.pathsep)
mpl.style.core.USER_LIBRARY_PATHS.extend(path_dirs)
