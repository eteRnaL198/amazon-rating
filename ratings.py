import csv

dictionaries = {} # ユーザー毎に、全itemのレビューを持つ
items = set() # 重複無いようにsetにする
ratings = [] # [[user1, item1, item2],[user2, item1, item2], ...]
with open('./Magazine_Subscriptions.csv') as f:
  reader = csv.reader(f)
  for row in reader:
    dictionaries[row[1]] = {}
    # dictionaries = {'user1': {}, 'user2': {}}
    items.add(row[0])
    # items = {'item1', 'item2', 'item3'}

  for user in dictionaries:
      for item in items:
          dictionaries[user][item] = 0 # すべてのitemのレビューを0に初期化
          # dictionaries = {'user1': {'a': 0, 'b': 0}, 'user2': {'a': 0, 'b': 0}}

with open('./Magazine_Subscriptions.csv') as f: # もう一回読み込む
  reader = csv.reader(f)
  for row in reader:
    dictionaries[row[1]][row[0]] = row[2] # レビューの値を代入
    # dictionaries = {'user1': {'a': 5, 'b': 4}, 'user2': {'a': 0, 'b': 5}}

  # 辞書→リストに変換
  i = 0
  for user in dictionaries:
      rating = [i] # ユーザーの番号を代入しておく [[0], [1], [2], ...]
      for item in dictionaries[user].values():
        rating.append(float(item))
      ratings.append(rating)
      i += 1
    # ratings = [[0, 5, 4], [1, 0, 5]]

# for rating in ratings:
#   print(rating)
