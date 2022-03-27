インタラクティブ形式の問題は、
標準入力にまとめて入力することでテストできる。

```
3 10
>
<
<
```

最初はバブルソートを試した。
比較回数は`n*(n-1)/2`で、n=26の場合に100回以内で一意に定めることができるは限らない。

次にマージソートを試した。
n=26の場合、比較回数は高々99回で、100回以内で一意に定めることができる。
n=5の場合、比較回数は高々8回で、7回以内で一意に定めることができるとは限らない。

Ford-Johnson Algorithm (merge insertion sort)というアルゴリズムがある。
n=11までならこちらの方が早いことが分かってるとのこと。

参考
* https://qiita.com/suecharo/items/30f5d817da4c948c3be6
* https://zenn.dev/ulwlu/articles/5590293df3b9dd
* https://github.com/TheAlgorithms/Python/blob/master/sorts/merge_sort.py
* https://github.com/TheAlgorithms/Python/blob/master/sorts/merge_insertion_sort.py
