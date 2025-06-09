#!/bin/zsh
# @Date    : 2025/06/09 14:29:57
# @Author  : Kan HUANG (kan.huang@connect.ust.hk)
# @Desc    : None

# git stash -u
git checkout main
git pull origin main
git checkout app
git merge main

PROJECT_ROOT="tslib"
mkdir -p $PROJECT_ROOT

dir_modules="data_provider exp layers models utils"

touch $PROJECT_ROOT/__init__.py
for module in ${=dir_modules}; do  # 添加 ${=} 进行单词分割
    cp -r $module $PROJECT_ROOT/
    touch $PROJECT_ROOT/$module/__init__.py
done

# clean
clean_dirs=($=dir_modules "pic" "tutorial" "scripts")  # $= 在 zsh 中强制单词分割

for dir in $clean_dirs; do
    rm -rf $dir
done