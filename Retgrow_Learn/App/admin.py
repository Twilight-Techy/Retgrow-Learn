from django.contrib import admin
from .models import Course, Level, Module, Task

class TaskInline(admin.TabularInline):
    model = Task
    extra = 1

class ModuleInline(admin.TabularInline):
    model = Module
    extra = 1
    inlines = [TaskInline]

class LevelInline(admin.TabularInline):
    model = Level
    extra = 1
    inlines = [ModuleInline]

class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'picture')
    inlines = [LevelInline]

class LevelAdmin(admin.ModelAdmin):
    list_display = ('name', 'course', 'order')
    list_filter = ('course',)
    inlines = [ModuleInline]

class ModuleAdmin(admin.ModelAdmin):
    list_display = ('name', 'level', 'order')
    list_filter = ('level',)
    inlines = [TaskInline]

class TaskAdmin(admin.ModelAdmin):
    list_display = ('name', 'module', 'order')
    list_filter = ('module',)

admin.site.register(Course, CourseAdmin)
admin.site.register(Level, LevelAdmin)
admin.site.register(Module, ModuleAdmin)
admin.site.register(Task, TaskAdmin)
