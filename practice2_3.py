print("2人の趣味をそれぞれ5つずつ入力してください。")
hobbies1 = set()
print("【1人目】")
hobbies1.add(input("1つ目の趣味を入力してください。"))
hobbies1.add(input("2つ目の趣味を入力してください。"))
hobbies1.add(input("3つ目の趣味を入力してください。"))
hobbies1.add(input("4つ目の趣味を入力してください。"))
hobbies1.add(input("5つ目の趣味を入力してください。"))

hobbies2 = set()
print("【2人目】")
hobbies2.add(input("1つ目の趣味を入力してください。"))
hobbies2.add(input("2つ目の趣味を入力してください。"))
hobbies2.add(input("3つ目の趣味を入力してください。"))
hobbies2.add(input("4つ目の趣味を入力してください。"))
hobbies2.add(input("5つ目の趣味を入力してください。"))

input("心の準備ができたらEnterキーを押してください。")

same = hobbies1 & hobbies2
total = hobbies1 | hobbies2
compatibillity = len(same) / len(total) * 100
print(f"相性度は{compatibillity}％でした！")


