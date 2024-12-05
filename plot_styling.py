import os
import matplotlib as mpl

# Add PATH directories to Matplotlib's style library paths
path_dirs = os.environ["PATH"].split(os.pathsep)
mpl.style.core.USER_LIBRARY_PATHS.extend(path_dirs)