#!/usr/bin/env bash
# define keys path
self_pub_key_path="${HOME}/.ssh/id_rsa.pub"
authorized_keys_path="${HOME}/.ssh/authorized_keys"

# check & generate pub_key
echo -n "Generate ${self_pub_key_path}... "
[ ! -f ${self_pub_key_path} ] && echo | ssh-keygen -q -t rsa -N '' > /dev/null
[ -f ${self_pub_key_path} ] && echo "SUCCEED" || (echo "FAILED" && exit 2)

self_pub_key=$(cat ${self_pub_key_path})

# update authorized_keys
echo -n "Begin self trust... "
touch ${authorized_keys_path} || exit 2

# check if pub_key in authorized_keys
grep -q "${self_pub_key}" ${authorized_keys_path} && echo "ALREADY TRUSTED" && exit 0
# write pub_key to authorized_keys
cat ${self_pub_key_path} >> ${authorized_keys_path} && chmod 600 ${authorized_keys_path} && echo "SUCCEED"