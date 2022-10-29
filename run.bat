@echo off
python CC.py
chcp 65001
echo 程序已执行完毕
echo 5秒后关闭
chcp 936
ping 127.1 -n 6 >nul