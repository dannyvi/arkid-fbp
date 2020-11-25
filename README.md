# arkfbp-py-server-template

## 环境搭建
1、需要python3环境及arkfbp-py的支持。
   1) brew install python3
   2) pip install arkfbp-py 注意：目前arkfbp-py需要从git拉下来到本地进行安装

2、数据库迁移

  1) python manage.py migrate

3、启动项目

  1) python manage.py runserver

## 相关API例子

1、用户管理
   1) 创建用户: 
   http://localhost:8000/arkfbp-admin/user/ POST

   1) 查找用户: 
   http://localhost:8000/arkfbp-admin/user/?page=&page_size= GET

   1) 更新用户: 
   http://localhost:8000/arkfbp-admin/user/<user_id>/ PATCH

   1) 删除用户: 
   http://localhost:8000/arkfbp-admin/user/<user_id>/ DELETE
   

2、前端获取meta config
   1) 获取指定meta config
   http://localhost:8000/arkfbp-admin/meta_config/<meta_name>/ GET
