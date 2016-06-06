import logging
import logging.config
import codecs
import yaml

with codecs.open('./conf/logging.yaml', 'r', 'utf-8') as logging_file:
  logging.config.dictConfig(yaml.load(logging_file))

_logger = logging.getLogger(__name__)

_logger.info("dealing with disk on hosts")

