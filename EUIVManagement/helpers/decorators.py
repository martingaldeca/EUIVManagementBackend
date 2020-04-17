import time
from logging import getLogger

logger = getLogger(__name__)


def timeit(method):
    """
    Decorator to time the execution of a function
    :param method:
    :return:
    """

    def timed(*args, **kw):
        start_time = time.time()
        result = method(*args, **kw)
        end_time = time.time()

        # Log the execution time
        logger.info(f"{method.__name__} lasts {round(end_time - start_time, 4)} seconds.")
        return result

    return timed
