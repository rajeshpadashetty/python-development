import profile
import pstats


def test():
    for i in range(100000):
        pass

profile.run("test()","profile_output.txt")

state=pstats.Stats("profile_output.txt")
state.print_stats()