import logging
import os

from set_envs import DD_API_KEY, DD_SITE
os.environ['DD_API_KEY'] = DD_API_KEY
os.environ["DD_SITE"] = DD_SITE

from datadog_custom_logger import DatadogCustomLogHandler

tags = "env:local,app:azf"
datadog_custom_handler = DatadogCustomLogHandler(tags=tags, level=logging.INFO)
logging.basicConfig()
logger = logging.getLogger()
logger.addHandler(datadog_custom_handler)
logging.getLogger().setLevel(logging.INFO)
logging.info("INFO  --- Log")