import logging

try:
    from heudiconv._version import __version__
except ImportError:
    # Fallback for development installs
    try:
        from importlib.metadata import version, PackageNotFoundError
        try:
            __version__ = version("heudiconv")
        except PackageNotFoundError:
            __version__ = "unknown"
    except ImportError:
        __version__ = "unknown"

from .info import __packagename__

__all__ = ["__packagename__", "__version__"]

lgr = logging.getLogger(__name__)
lgr.debug("Starting the abomination")  # just to "run-test" logging
