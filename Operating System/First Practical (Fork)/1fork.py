import os

print("Before fork process id =", os.getpid())

if hasattr(os, "fork"):   # Check if fork is available
    pid = os.fork()

    if pid == 0:
        print("After fork, Child process ID =", os.getpid())
    else:
        print("After fork, Parent process ID =", os.getpid())
else:
    print("Fork is not supported on this operating system.")