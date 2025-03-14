from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField()

    class Meta:
        ordering = ('title',)
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.title
    

class Post(models.Model):
    # 数据库存储  
    ACTIVE = 'active'
    DRAFT = 'draft'
    # 在admin界面显示
    CHOICES_STATUS=(
        (ACTIVE,'发布'),
        (DRAFT,'草稿')
    )
    status = models.CharField(max_length=10,choices=CHOICES_STATUS,default=ACTIVE)
    # 外键
    category = models.ForeignKey(Category,related_name='posts',on_delete=models.CASCADE)
    title = models.CharField(max_length=255)  # 标题
    slug = models.SlugField()  # URL友好格式的短标签
    intro = models.TextField()  # 简介
    body = models.TextField()  # 正文
    created_time = models.DateTimeField(auto_now_add=True)  # 创建时间（自动添加）
    image = models.ImageField(upload_to='uploads/',blank=True,null=True)

    class Meta:
        ordering = ('-created_time',)  # 按创建时间降序排列

    def __str__(self):
        return self.title

class Comment(models.Model):
    # 设置外键，绑定对应的文章、related——name 反向查询
    # CASCADE如果 Post 被删除，与之关联的所有 Comment 也会被删除
    post = models.ForeignKey(Post,related_name='comments',on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    body = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name