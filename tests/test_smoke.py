"""Smoke tests: confirm the package and core dependencies import correctly."""


def test_package_imports():
    import anomaly_tracker
    from anomaly_tracker import config
    from anomaly_tracker.detectors import DETECTORS

    assert anomaly_tracker.__version__
    assert config.DATA_DIR.name == "data"
    assert isinstance(DETECTORS, list)


def test_dependencies_import():
    import numpy
    import pandas
    import plotly
    import streamlit

    assert pandas.__version__ and numpy.__version__
    assert plotly.__version__ and streamlit.__version__
