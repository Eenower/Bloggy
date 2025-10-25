from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
class PostTag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name
    
class PostTagRelation(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='tag_relations')
    tag = models.ForeignKey(PostTag, on_delete=models.CASCADE, related_name='post_relations')

    def __str__(self):
        return f"{self.post.title} - {self.tag.name}"
    

class Page(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='page')
    content = models.TextField()


    def __str__(self):
        return f"page for {self.post.title} - {self.description}"