from multiprocessing import Process

def process_data(filelist):
    for filepath in filelist:
        print('Process {} ...'.format(filepath))
        # 处理数据
        pass
        
def main():
    # freeze_support()  # windows下需要加上此函数
    
    n_total = len(full_list)
    n_processes = 32
    
    # 每段子列表的平均长度
    length = float(n_total) / float(n_processes)
    
    # 计算每段子列表在full_list里的下标
    indices = [int(round(i*length)) for i in range(n_processes+1)]
    
    # 生成每个进程要处理的子文件列表
    sublists = [full_list[indices[i]:indices[i+1]] for i in range(n_processes)]
    
    # 生成进程
    processes = [Process(target=process_data, args=(x,)) for x in sublists]
    
    # 并行处理
    for p in processes:
        p.start()
    for p in processes:
        p.join()
        
if __name__ == '__main__':
    main()