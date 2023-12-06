"""
    python 递归
"""
import os


# def test_os():
    # os模块的3个基础方法
    # print(os.listdir("E:/Code/Python/Test"))  # 列出路径下的文件夹
    # print(os.path.isdir("E:/Code/Python/Test"))  # 判断指定路径是不是文件夹
    # print(os.path.exists("E:/Code/Python/Test"))  # 判断指定路径是否存在


def get_files_recursion_from_dir(path):
    """
    从指定的文件夹中使用递归的方式 获取全部的文件列表
    :param path: 被判断的文件夹
    :return: 包含全部的文件 如果目录不存在或者无文件 返回一个空list
    """
    print(f"当前判断的文件夹是：{path}")
    file_list = []
    if os.path.exists(path):
        for f in os.listdir(path):
            newPath = path + "/" + f
            if os.path.isdir(newPath):
                # 进入这里 表明这个目录是文件夹
                file_list += get_files_recursion_from_dir(newPath)
            else:
                file_list.append(newPath)
    else:
        print(f"指定的目录{path} 不存在")
        return []
    return file_list


if __name__ == '__main__':
    print(get_files_recursion_from_dir("E:/Code/Python/Test"))
