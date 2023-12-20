import logging
import sys

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s %(name)-12s %(levelname)-8s %(module)-25s %(message)s',
    handlers=[
        # logging.FileHandler(),
        logging.StreamHandler(sys.stdout)
    ]
)


logger = logging.getLogger("CollectMetaDataLogger")

