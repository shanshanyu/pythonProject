#!/bin/sh

set -e

[ $# -eq 0 ] && echo "Usage: sh $0 topic_name bootstrap_servers start_time(2023072001) end_time(2023072002)" && exit 0
[ $# -ne 4 ] && echo "参数不匹配，清检查" && exit 1

BASE_DIR=$(cd $(dirname $0) &&echo  $PWD || exit 2)

PYTHON_PATH="$BASE_DIR/python3.7/bin/python3"
main="$BASE_DIR/apps/kafka_sub.py"

${PYTHON_PATH} $main $@