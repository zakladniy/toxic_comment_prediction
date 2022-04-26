"""Module with API config."""
from loguru import logger

# Logs configuration
logger.add(
    "info_api.log",
    format="{time} {level} {message}",
    level="INFO",
    rotation="100 KB",
    compression="zip",
)

api_desc = """<h2>API for predict probability of toxicity russian comment</h2>
<br>by Zakladniy Anton"""

api_title = "Web application for predict probability " \
            "of toxicity russian comments"
