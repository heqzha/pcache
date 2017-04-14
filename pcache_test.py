import pcache
import time

cache = pcache.load("test.db", True)

cache.set("number", 100, 3)

print cache.get("number")

time.sleep(5)

print cache.get("number")