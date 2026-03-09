from datetime import datetime

now = datetime.now()
old = datetime(1970, 1, 1)
diff = now - old

print("Seconds since January 1, 1970:", end="")
print(f"{round(diff.total_seconds(), 4):,}", end="")
print("or %1.2E in scientific notation" % (diff.total_seconds()))
print(now.strftime("%b %d %Y"))
