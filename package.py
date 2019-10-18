name = "git"

version = "2.23.0"

authors = [
    "Linus Torvalds"
]

description = \
    """
    Git is a fast, scalable, distributed revision control system with an unusually rich command set that provides
    both high-level operations and full access to internals.
    """

requires = [
    "cmake-3+",
    "curl-7+",
    "gcc-6+",
    "python-2.7+",
    "zlib-1.2+"
]

variants = [
    ["platform-linux"]
]

tools = [
    ""
]

build_system = "cmake"

with scope("config") as config:
    config.build_thread_count = "logical_cores"

uuid = "git-{version}".format(version=str(version))

def commands():
    env.PATH.prepend("{root}/bin")
    env.LD_LIBRARY_PATH.prepend("{root}/lib")

    # Helper environment variables.
    env.GIT_BINARY_PATH.set("{root}/bin")
    env.GIT_INCLUDE_PATH.set("{root}/include")
    env.GIT_LIBRARY_PATH.set("{root}/lib")
