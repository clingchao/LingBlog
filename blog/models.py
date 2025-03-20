from django.db import models

class Category(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)  # 增加最大长度

    class Meta:
        ordering = ('title',)
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.title


class Post(models.Model):
    
    ACTIVE = 'active'
    DRAFT = 'draft'
    CHOICES_STATUS = (
        (ACTIVE, '发布'),
        (DRAFT, '草稿')
    )
    status = models.CharField(
        max_length=10, 
        choices=CHOICES_STATUS, 
        default=DRAFT  # 默认草稿
    )
    category = models.ForeignKey(Category, related_name='posts', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)  # 确保唯一性
    intro = models.TextField()
    body = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='uploads/', blank=True, null=True)

    class Meta:
        ordering = ('-created_time',)

    def __str__(self):
        return self.title

class Comment(models.Model):
    # 设置外键，绑定对应的文章、related——name 反向查询
    # CASCADE如果 Post 被删除，与之关联的所有 Comment 也会被删除
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    body = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name 