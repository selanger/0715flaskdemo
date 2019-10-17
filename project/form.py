import wtforms
from flask_wtf import FlaskForm
from wtforms import validators
from wtforms import ValidationError

def keywords_valid(form,field):
    """
    判断填写的数据是否有敏感字
    这个字段 不需要手动传参
    :param form:   表单
    :param field:  字段
    :return:
    """
    data = field.data
    keywords = ["admin","管理员","香港"]
    if data in keywords:
        raise ValidationError("不可以是敏感词汇")


class TaskForm(FlaskForm):
    ## 属性
    name = wtforms.StringField(
                               render_kw={
                                   "class":"form-control",
                                   "placeholder":"任务的名字"
                               },
                                validators=[
                                    validators.DataRequired("任务的名字不能为空"),
                                    # validators.Email("必须符合邮箱格式"),
                                    # validators.length(max=8,min=6),
                                    keywords_valid
                                ]
                               )
    description = wtforms.TextField(render_kw={
                                   "class":"form-control",
                                   "placeholder":"任务的描述"
                                    },
                                    # validators=[
                                    #     validators.EqualTo("name"),    ### 描述和name值一样
                                    # ]
                    )
    time = wtforms.DateField(render_kw={
                                   "class":"form-control",
                                   "placeholder":"任务的时间"
                               })
    public = wtforms.StringField(render_kw={
                                   "class":"form-control",
                                   "placeholder":"任务的发布人"
                               })





