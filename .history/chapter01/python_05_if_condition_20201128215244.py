"""[if文について]
もし〜だったら、こうして
"""

# if 条件:
#     実行するブロック

# 条件によって処理を適応したい場合
# 3000kmごとにオイル交換しないといけない
distance = 3403
if distance > 3000:
    print('オイル交換時期です')

# 文字列を比較する/リストを比較する
if 'abc' == 'ABC':
    print('1同類です')
if 'CDE' == 'CDE':
    print('2同類です')
if 'あいうえお' == 'あいうえお':
    print('3同類です')

if ['apple', 'banana'] == ['apple', 'banana']:
    print('1リスト同類')
if ['apple', 'banana'] == ['APPLE', 'BANANA']:
    print('2リスト土塁')

# 文字列を検索する/リストの要素を検索する
# if 'abc' in "ABC":
#     print('ヒットしました！')
# if 'ドリフト' in '僕はドリフトが好きです':
#     print('ヒットしました！')
# if 'japan' in 'japanese domestic market vehicle':
#     print('ヒットしました！')

# else文

# elif文

