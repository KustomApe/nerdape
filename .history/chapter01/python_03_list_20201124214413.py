"""[リストについて]
リストの構文とリストの使い方について
配列とリストは同じ意味
"""
# リストの定義
['apple', 'banana', 'orange']
[1, 2, 3, 4, 5]

# リストを変数に代入
fruits = ['apple', 'banana', 'orange']
numbers = [1, 2, 3, 4, 5]

# インデックスとを指定して要素を取り出す
# 一番最初0はじまり
print(fruits[0])

# リストの最後を指定する -1
print(numbers[-1])

# 昨日と今日の気温差をリストを使って計算してみる
weather = [13, 15, 18, 13, 16]
# 昨日の気温は13度でした
# 今日の天気は15度です
diff_temp = weather[0] - weather[1]
print(diff_temp)

# リストの連結
japan_cars = ['スカイライン', 'シビック']
euro_cars = ['フェラーリ', 'ランボルギーニ']

all_cars = japan_cars + euro_cars
print(all_cars)

# 要素の置き換え、削除 del文
all_cars[1] = 'ポルシェ'
print(all_cars)

del all_cars[0]
print(all_cars)

# スライスを使って複数の要素を取り出す [1:3]
students = ['山田', '鈴木', '本田', '豊田', '中山']
students[1:4]

# 二次元配列

# リストの合計、最大値、最小値 組み込み関数sum(),max(), min()


# リストの長さを調べる 組み込み関数len()
