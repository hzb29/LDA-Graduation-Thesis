import os
import re 
import csv

output_dir = '/home/han/lda_model/split_data_commet'
input_dir = '/home/han/lda_model/split_data'


def process_file(filename):

  with open(os.path.join(input_dir, filename), 'r', encoding='utf-8') as f:
    text = f.read()

  lines = text.split('\n')

  for line in lines:

    # 只匹配数字开头,可能是用户id
    line = re.sub(r"^(\d+)", r"\1-", line)  

    # 只匹配时间格式字符串
    line = re.sub(r"\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}", "", line)
    
    # 只匹配完整网址
    line = re.sub(r"http://\S+", "", line)
    
    # delete label which start with <a
    line = re.sub(r'<a href="\S+"?\s+rel="\w+">', '', line)
    outfile = get_outfile(filename)

    with open(outfile, 'a', encoding='utf-8') as f:
      f.write(line + '\n')
      
def get_outfile(filename):
  name = filename.replace('.txt', '_comment.csv')
  return os.path.join(output_dir, name)

if __name__ == '__main__':

  files = os.listdir(input_dir)

  for file in files:
    if file.startswith('chunk_'):
      process_file(file)

  print('完成文件处理')