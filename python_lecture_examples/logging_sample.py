import time
import numpy as np
from loguru import logger

logger.add("./20240613.log")

while True:
	time.sleep(1)
	x = np.random.random(10)
	logger.debug(f"{x}")
	try:
		x[12] = 123
	except Exception as e:
		logger.exception(e)
	raise Exception("그냥 꺼졌어!")
