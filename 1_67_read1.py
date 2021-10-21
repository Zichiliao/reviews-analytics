"""
1. 解釋程式目標
2. 寫出基本架構
3. 解釋字典架構
4. 解答字典關鍵用法
5. 用for loop來印字典
6. 讓使用者查字
7. 解釋為什麼用有空字串在排行
8. 先檢查字有沒有在字典裡，避免當掉
9. 建立版本上傳
10. 結語

"""
data = []
count = 0
with open('reviews.txt','r') as f:
	for line in f:
		data.append(line)
		count += 1
		if count % 1000 == 0:
			print(len(data))

print('檔案讀取完了，總共有', len(data), '筆資料') 
print(data[0])

wc = {} # word_count
for d in data:
	words = d.strip().split( ) # 使用' '切割，如果文檔裡面使用多個空白键分隔，則多出來的空白键會被選入檔案，用python預設split( )則會避開此問題
	for word in words:
		if word in wc:
			wc[word] += 1
		else:
			wc[word] = 1 # 新增新的key進wc字典
for word in wc:
	if wc[word] > 1000000:
		print(word, wc[word])

print(len(wc))

while True:
	word = input('請問你想查甚麼字: ')
	if word == 'q':
		break
	if word in wc:
		print(word, '出現過的次數為: ', wc[word])
	else:
		print('這個字沒有出現過喔!')
print('感謝使用本查詢功能')


