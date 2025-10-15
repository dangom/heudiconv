import logging

try:
    from heudiconv._version import __version__
except ImportError:
    # Version file not generated yet (e.g., in development without build)
    __version__ = "unknown"

__packagename__ = "heudiconv"

__all__ = ["__packagename__", "__version__"]

lgr = logging.getLogger(__name__)
lgr.debug("Starting the abomination")  # just to "run-test" logging
