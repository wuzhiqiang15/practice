from django.contrib import admin
from meetyou.models import Student, ClassRoom, Teacher

# Register your models here.

# 设置admin后台的标题头、位置title和主页title
admin.site.site_header = "测试管理后台"
admin.site.site_title = "美柚测试管理后台"
admin.site.index_title = "首页"

# 设置admin管理类（来管理下面“已经被绑定的模型”）
# 管理类 必须 继承admin.ModelAdmin
class ClassRoomAdminInfo(admin.ModelAdmin):
    pass

# 使用装饰器的方式来管理Models
@admin.register(Teacher)
class TeacherAdminInfo(admin.ModelAdmin):
    # 设置每页显示总条数
    list_per_page = 6
    # 设置操作栏在 底部（Ture）
    actions_on_bottom = True
    # 设置操作栏在 顶部（由于默认是在顶部，所以要将其设置为 False）
    actions_on_top = False
    # 设置页面中显示的列表项
    list_display = ["name", "course", "room", "curTime"]
    # 在页面中增加搜索框，这里是根据"name"来进行搜索
    search_fields = ["name"]

    # 将页面的显示区域分为两个部分
    fieldsets = (
        ("基本信息", {"fields": ["name", ]}),
        ("其他信息", {"fields": ["course", "room"]}),
    )


class StudentAdminInfo(admin.ModelAdmin):
    list_per_page = 2
    actions_on_bottom = True
    actions_on_top = False
    #list_display = []


'''
 把后台跟models中的模型进行绑定
 这里使用register绑定过的模型，才会在后台显示
 这里的第一个参数（如ClassRoom）是models.py中的模型类，第二个参数是上方定义的admin管理类（如ClassRoomAdminInfo）
'''
admin.site.register(ClassRoom, ClassRoomAdminInfo)
#admin.site.register(Teacher, TeacherAdminInfo)
admin.site.register(Student, StudentAdminInfo)
