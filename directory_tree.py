import os

def print_directory_tree(start_path, indent='', ignore_dirs=None):
    if ignore_dirs is None:
        ignore_dirs = ['venv', '__pycache__', '.git', '.vscode', '.idea', 'node_modules']
    
    if os.path.basename(start_path) in ignore_dirs:
        return
    
    print(f"{indent}{os.path.basename(start_path)}/")
    indent += '    '
    
    try:
        for item in os.listdir(start_path):
            item_path = os.path.join(start_path, item)
            if os.path.isdir(item_path):
                print_directory_tree(item_path, indent, ignore_dirs)
            else:
                print(f"{indent}{item}")
    except PermissionError:
        pass

# 替换为你的项目根目录路径
project_root = "C:\\Users\\23255\\Documents\\Project\\LingBlog\\"
print_directory_tree(project_root)