#笔记
###1.模块组成分析
0.templates and statics
1.app config
2.view 函数
3.数据库 增删改查，表model

###2.邮箱验证功能实现
1.安装Flask-Mail
2.在config中进行配置

###3.已经登录过的用户 界面展示问题
1.app.before_request
2.app.context_processor
3.如果已经登录 则在g里保存user变量

###4.装饰器模式 是为了扩展view函数功能的
1.比如对于需要判断是否用户登录的view函数来说，最好使用装饰器以满足开闭，且复用

###5.步骤总结
1.html 前端设计
2.form model view 3步骤实现后端表单保存与展示, 一般一个html对应一个view
