"""[if文について]
もし〜だったら、こうして
"""

if 条件:
    実行するブロック

# 条件によって処理を適応したい場合
# 3000kmごとにオイル交換しないといけない
distance = 3403
if distance > 3000:
    print('オイル交換時期です')

# total = 123200
# average = total / 30
# print(average)
# if average > 3000:
#     print('オイル交換時期ですよ！')

# 文字列を比較する/リストを比較する
# if 'abc' == "ABC":
#     print('同類です')
# if 'CDE' == 'CDE':
#     print('同類です')
# if 'あいうえお' == 'あいうえお':
#     print('同類です')

# 文字列を検索する/リストの要素を検索する
# if 'abc' in "ABC":
#     print('ヒットしました！')
# if 'ドリフト' in '僕はドリフトが好きです':
#     print('ヒットしました！')
# if 'japan' in 'japanese domestic market vehicle':
#     print('ヒットしました！')

# else文

# elif文
