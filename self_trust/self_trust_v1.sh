#!/bin/bash

set -e


self_pub_key_path=$HOME/.ssh/id_rsa.pub
authorized_key_path=$HOME/.ssh/authorized_keys

#判断pub_key 文件是否存在，不存在则创建
[ ! -f ${self_pub_key_path} ] && echo |ssh-keygen -t rsa -q -N '' >/dev/null 2>&1

[ -f ${self_pub_key_path} ] && echo 'Generate pub key success.' || (echo 'Generate pub key failed.' && exit 2)


#判断pub_key 是否在 authorized_keys 文件中

self_pub_key=$(cat ${self_pub_key_path})

touch $authorized_key_path || exit 2
grep -q "$self_pub_key" $authorized_key_path && echo 'Already trusted.' && exit 0

echo -n 'Self trust ...'
echo $self_pub_key >> $authorized_key_path && chmod 600 $authorized_key_path && echo 'Success.' || echo 'Failed'