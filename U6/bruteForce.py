import subprocess
a = 355991552
e = 356057087
c = 0


for i in range(a, e+1):
    p = subprocess.run(["./scriptV6", "3673526"], capture_output=True, text=True)
    print(int(p.stdout))