"""Central configuration: file paths and reproducibility settings.

Detection thresholds will be added here as detectors are implemented.
"""

from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[2]
DATA_DIR = PROJECT_ROOT / "data"
DB_PATH = DATA_DIR / "anomaly_tracker.db"

RANDOM_SEED = 42
