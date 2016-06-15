import yaml
import logging
import logging.config
import codecs

with codecs.open('./conf/logging.yaml', 'r', 'utf-8') as logging_file:
    logging.config.dictConfig(yaml.load(logging_file))

_logger = logging.getLogger(__name__)
_logger.info("1122323232")

#只有第一层解析From To Subject
def parse_s():
    _logger.info("str(content_type)")

if __name__ == '__main__':
    parse_s()
