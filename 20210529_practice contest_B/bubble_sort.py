import sys
import string

N, _ = [int(i) for i in sys.stdin.readline().rstrip().split()]
s = string.ascii_uppercase[:N]

cnt = 0

for i in range(N - 1):
  for j in range(N - 1 - cnt):
    print(f'? {s[j]} {s[j+1]}', flush=True)

    ans = sys.stdin.readline().rstrip()
    if ans == '>':
      s = s.replace(s[j], '-').replace(s[j+1], s[j]).replace('-', s[j+1])

  cnt += 1

print(f'! {s}', flush=True)
