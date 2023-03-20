import os
import subprocess

# Create virtual environment if not exists
venv_name = 'venv'
if not os.path.exists(venv_name):
    subprocess.run(['python', '-m', 'venv', venv_name], check=True)

# Activate virtual environment
activate_this = os.path.join(venv_name, 'Scripts', 'activate')
subprocess.run(activate_this, shell=True, check=True)

# Install packages if not exists
packages = [
    'pandas', 'numpy', 'tqdm', 'scipy', 'matplotlib',
    'seaborn', 'plotly', 'scikit-learn', 'lightgbm',
    'xgboost[scikit-learn]', 'xgboost', 'sklearn', 'Jinja2', 'catboost', 'tabulate'
]

for package in packages:
    try:
        subprocess.run(['pip', 'show', package], check=True)
    except subprocess.CalledProcessError:
        subprocess.run(['pip', 'install', package], check=True)

# Run the app
subprocess.run(['python', 'app.py'], check=True)
