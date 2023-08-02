#!/bin/bash

SSH_DIR=$HOME/.ssh
set -e

echo |ssh-keygen -q -t rsa -N '' >/dev/null 2>&1 &  #把可能出错的命令放在后台跑, & 后台命令执行成功了，就算命令执行成功了

if [ ! -f $SSH_DIR/id_rsa.pub ];then
  echo 'ssh-keygen 失败'
  exit 1
fi

echo -n 'Self Trust...'
cat $SSH_DIR/id_rsa.pub >> $SSH_DIR/authorized_keys  && chmod 600 $SSH_DIR/authorized_keys && echo 'SUCCESS' || echo 'Failed'

#频繁使用 SSH_DIR，再拼接目录，容易拼错，直接定义 key 变量更好一点


#在执行 ssh-keygen 之前未做判断，如果 pub_key 已经存在，不需要再执行

#在执行 cat key >> authorized_keys 中未做判断，如果authorized_keys 中已经存在，不需要再次加密