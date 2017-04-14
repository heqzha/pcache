import pcache
import time

cache = pcache.pcache("test.db", False)

cache.set("number", 100, 3)

print cache.get("number")

time.sleep(5)

print cache.get("number")