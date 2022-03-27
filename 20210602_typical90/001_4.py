import sys

N, L = map(int, sys.stdin.readline().rstrip().split())
K = int(sys.stdin.readline().rstrip())
A = [int(a) for a in sys.stdin.readline().rstrip().split()]
print(f'N={N} L={L}')
print(f'K={K}')
print(f'A={A}')

def get_min_len(L, A, idxA):
  if len(idxA) == 1:
    l1 = A[idxA[0]]
    l2 = L - A[idxA[0]]
    ls = [l1, l2]
    min_l = min(ls)
  else:
    l1 = A[idxA[0]]
    l2 = [A[idxA[i+1]] - A[idxA[i]] for i in range(len(idxA) - 1)]
    l3 = L - A[idxA[-1]]
    ls = [l1] + l2 + [l3]
    min_l = min(ls)

  return min_l, ls

cnt = 0
max_l = 0

while True:
  idxA = [i + cnt for i in range(K)]

  # K=1
  if K == 1:
    min_l, ls = get_min_len(L, A, idxA)
    if min_l > max_l:
      max_l = min_l
    print(f'A={[A[i] for i in idxA]}, l={ls}, min_l={min_l}, max_l={max_l}')

  # K>=2
  # selectedAを後方から走査
  for k in range(K - 1, 0, -1):
    while True:
      min_l, ls = get_min_len(L, A, idxA)
      if min_l > max_l:
        max_l = min_l
      if A[idxA[0]]==233 and A[idxA[3]]==954:
#      if A[idxA[0]]==233 and A[idxA[1]]==350:
        print(f'A={[A[i] for i in idxA]}, l={ls}, min_l={min_l}, max_l={max_l}')
      # 限界まで到達していたら終了
      if idxA[k] >= (N - K + k): 
        print('break')
        break
      idxA[k] += 1

  # selectedAの1つ目が限界まで到達していたら終了
  if idxA[0] == (N - K): break
  cnt += 1

#print(idxA)
print(max_l)
