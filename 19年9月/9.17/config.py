#进阶七：子查询
#
# 含义：
# 出现在其他语句中的select语句，称为子查询或内查询
# 外部的查询语句，称为主查询或外查询
#
# 分类：
# 按子查询出现的位置：
#     select后面:
#         仅仅支持量子查询
#     from后面:
#         支持表子查询
#     where或having后面：
#         标量子查询（单行）
#         列子查询  （多行）
#         行子查询
#
#     exits后面（相关子查询）
#         表子查询

#案例2: 返回job_id与141号员工相同，salary比143号员工多的员工 姓名，job_id 和工资

# 查询141






# 案例二：查询没有女朋友的男神信息
# in
# SELECT bo.*
# FROM boys bo
# WHILE bo.id NOT IN(
#     SELECT boyfriend_id
#     FROM beauty
# )
#
# # exists
# SELECT bo.*
# FROM boys bo
# WHILE NOT EXISTS(
#     SELECT boyfriends_id
#     FROM beauty b

# )