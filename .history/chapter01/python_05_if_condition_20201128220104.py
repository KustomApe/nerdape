"""[if文について]
もし〜だったら、こうして
"""

# if 条件:
#     実行するブロック

# 条件によって処理を適応したい場合
# 3000kmごとにオイル交換しないといけない
distance = 3403
# if distance > 3000:
    # print('オイル交換時期です')

# 文字列を比較する/リストを比較する
# if 'abc' == 'ABC':
#     print('1同類です')
# if 'CDE' == 'CDE':
#     print('2同類です')
# if 'あいうえお' == 'あいうえお':
#     print('3同類です')

# if ['apple', 'banana'] == ['apple', 'banana']:
#     print('1リスト同類')
# if ['apple', 'banana'] == ['APPLE', 'BANANA']:
#     print('2リスト同類')
# if [1, 2, 3] == ['1', '2', '3']:
#     print('3リスト同類')
# if [1, 2, 3] == [1, 2, 3]:
#     print('4リスト同類')

# 文字列を検索する/リストの要素を検索する
if 'abc' in 'ABC':
    print('1ヒットしました！')
if 'ドリフト' in '僕はドリフトが好きです':
    print('2ヒットしました！')
if 'japan' in 'japanese domestic market vehicle':
    print('3ヒットしました！')

if 12 in [12, 3, 4]:
    print('1あります！')
if 345 in [3, 4, 5]:
    print('2あります！')
if [1, 2] in [1, 2, 3]:
    print('出る')
if [1, 2] in [3, [1, 2], 5, 7]:
    print('出力されます！')
    
# else文

# elif文

