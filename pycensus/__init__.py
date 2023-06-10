# type: ignore[attr-defined]
"""A Modern wrapper for the United States Census Bureau's API. With over 1,000 Census API endpoints, data sources include the Decennial Census, American Community Survey, Poverty Statistics, Population Estimates, and Census microdata. Incorporate ML and Big Data packages such Pandas, Numpy, and many more. """

import sys

if sys.version_info >= (3, 8):
    from importlib import metadata as importlib_metadata
else:
    import importlib_metadata


def get_version() -> str:
    try:
        return importlib_metadata.version(__name__)
    except importlib_metadata.PackageNotFoundError:  # pragma: no cover
        return "unknown"


version: str = get_version()
