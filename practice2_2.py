nationalLanguage_score = int(input("国語の点数を入力してください。＞＞"))
arithmetic_score = int(input("算数の点数を入力してください。＞＞"))
science_score = int(input("理科の点数を入力してください。＞＞"))
society_score = int(input("社会の点数を入力してください。＞＞"))
english_score = int(input("英語の点数を入力してください。＞＞"))

subject = [nationalLanguage_score,arithmetic_score,science_score,society_score,english_score]
total = sum(subject)
avg = total / len(subject)
print(f"合計{total}点、平均{avg}点")

