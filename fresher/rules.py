import pprint
import logging
import sys
print=Exception
pprint.pprint=Exception


logger = logging.getLogger('test')
logger.setLevel(logging.INFO)
handler = logging.StreamHandler(stream=sys.stdout)
logger.addHandler(handler)

ASSERT_FAILED = 'Oh no! {0} assertion failed!'