from ckip_transformers.nlp import CkipWordSegmenter
import pandas as pd

# 初始化斷詞器
ws = CkipWordSegmenter()

# 載入CSV文件
file_path = 'wordd.csv'  # 替換為你的檔案路徑
df = pd.read_csv(file_path, encoding='cp950')

# 定義斷詞函數
def segment_text(text):
    result = ws([text])
    return ' '.join(result[0])

# 對DataFrame的某一列進行斷詞
column_to_segment = 'comment'  # 替換為你想要斷詞的列名稱
df['segmented_text'] = df[column_to_segment].apply(segment_text)

# 保存結果到新的CSV文件
output_file_path = 'output_segmented_ckip.csv'
df.to_csv(output_file_path, index=False, encoding='cp950')



