"""Utility for fetching alpha data from the WQBrain platform."""

import logging
import os
from typing import Dict, List

try:
    import requests
except ImportError:  # requests may not be installed
    requests = None
    logging.warning("requests library is missing; fetch_alpha will not work")


def fetch_alpha() -> List[Dict[str, float]]:
    """Fetch alpha data from the configured WQBrain API.

    The URL is read from ``WQBRAIN_API_URL``. If the API call fails or the
    ``requests`` library is missing, an empty list is returned.
    """

    if requests is None:
        logging.error("requests library not installed")
        return []

    url = os.getenv("WQBRAIN_API_URL")
    if not url:
        logging.warning("WQBRAIN_API_URL is not set; returning empty data")
        return []

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
    except Exception as exc:  # broad catch to keep the sample simple
        logging.error("Failed to fetch alpha data: %s", exc)
        return []

    if not response.content:
        return []

    try:
        return response.json()
    except ValueError:
        logging.error("Response was not valid JSON")
        return []
