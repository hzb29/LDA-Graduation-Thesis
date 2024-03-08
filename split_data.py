import os

def split_file(input_file, output_dir, chunk_size):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    with open(input_file, 'r', encoding='utf-8') as f:
        chunk_number = 1
        while True:
            chunk = f.readlines(chunk_size)
            if not chunk:
                break

            output_file = os.path.join(output_dir, f'chunk_{chunk_number}.txt')
            with open(output_file, 'w', encoding='utf-8') as out:
                out.writelines(chunk)

            chunk_number += 1

    print('File split complete.')

# 示例用法
input_file = '/home/han/lda_model/weibo.txt'
output_dir = '/home/han/lda_model/split_data'
chunk_size = 1000000  # 每个分割文件的行数

split_file(input_file, output_dir, chunk_size)