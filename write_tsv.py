import pandas as pd

df = pd.read_table('jarujaru_videos.tsv')

df = df.query('title.str.contains("奴")', engine='python') # 奴のやつだけ
df['title'] = df['title'].str.extract(r'『(.*?)』') #『』の中だけ
df = df.dropna(subset=['title']) # NaNを削除

df.to_csv('yastu.tsv', columns=['title'], sep='\t', index=False)
