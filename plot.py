import matplotlib.pyplot as plt
import numpy as np
import redis
import random

redis_db = redis.StrictRedis(host='localhost', port=6379)

y_axis = []
x_ticks = []

keys = redis_db.keys('so:*')

job_tags = {key: int(redis_db.get(key)) for key in keys}

sorted_tags = sorted(job_tags.items(), key=lambda x: x[1], reverse=True)[:20]
# random.shuffle(sorted_tags)
for (job_tag, count) in sorted_tags:
    y_axis.append(int(count))
    x_ticks.append(job_tag[3:])

x_axis = [i+1 for i in range(len(y_axis))]

plt.xticks(x_axis, x_ticks)
plt.plot(x_axis, y_axis, '-bo')
plt.show()
