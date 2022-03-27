'''
MIT License
Copyright (c) 2016-2021 The Algorithms
https://github.com/TheAlgorithms/Python/blob/master/LICENSE.md
'''

# for Testset1,2
def merge_sort(collection: list) -> list:
  def merge(left: list, right: list) -> list:
    def _merge():
      while left and right:
        print(f'? {left[0]} {right[0]}', flush=True)
        yield (left if input().rstrip() == '<' else right).pop(0)
      yield from left
      yield from right

    return list(_merge())

  if len(collection) <= 1:
    return collection
  mid = len(collection) // 2
  return merge(merge_sort(collection[:mid]), merge_sort(collection[mid:]))


# for Testset3
def merge_insertion_sort(collection: list) -> list:
  def binary_search_insertion(sorted_list, item):
    left = 0
    right = len(sorted_list) - 1
    while left <= right:
      middle = (left + right) // 2
      print(f'? {sorted_list[middle]} {item}', flush=True)
      if left == right:
        if input().rstrip() == '<':
          left = middle + 1
        break
      elif input().rstrip() == '<':
        left = middle + 1
      else:
        right = middle - 1
    sorted_list.insert(left, item)
    return sorted_list

  def sortlist_2d(list_2d):
    def merge(left, right):
      result = []
      while left and right:
        print(f'? {left[0][0]} {right[0][0]}', flush=True)
        if input().rstrip() == '<':
          result.append(left.pop(0))
        else:
          result.append(right.pop(0))
      return result + left + right

    length = len(list_2d)
    if length <= 1:
      return list_2d
    middle = length // 2
    return merge(sortlist_2d(list_2d[:middle]), sortlist_2d(list_2d[middle:]))

  if len(collection) <= 1:
    return collection

  two_paired_list = []
  has_last_odd_item = False
  for i in range(0, len(collection), 2):
    if i == len(collection) - 1:
      has_last_odd_item = True
    else:
      print(f'? {collection[i]} {collection[i + 1]}', flush=True)
      if input().rstrip() == '<':
        two_paired_list.append([collection[i], collection[i + 1]])
      else:
        two_paired_list.append([collection[i + 1], collection[i]])

  sorted_list_2d = sortlist_2d(two_paired_list)
  result = [i[0] for i in sorted_list_2d]
  result.append(sorted_list_2d[-1][1])

  if has_last_odd_item:
    pivot = collection[-1]
    result = binary_search_insertion(result, pivot)

  is_last_odd_item_inserted_before_this_index = False
  for i in range(len(sorted_list_2d) - 1):
    if result[i] == collection[-1]:
      is_last_odd_item_inserted_before_this_index = True
    pivot = sorted_list_2d[i][1]
    # If last_odd_item is inserted before the item's index,
    # you should forward index one more.
    if is_last_odd_item_inserted_before_this_index:
      result = result[: i + 2] + binary_search_insertion(result[i + 2 :], pivot)
    else:
      result = result[: i + 1] + binary_search_insertion(result[i + 1 :], pivot)

  return result


N, Q = map(int, input().split())
S = [chr(ord('A') + i) for i in range(N)]
if N == 5:
  print(f'! {"".join(merge_insertion_sort(S))}', flush=True)
else:
  print(f'! {"".join(merge_sort(S))}', flush=True)
