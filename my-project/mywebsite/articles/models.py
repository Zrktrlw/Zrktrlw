from django.db import models

class articleUser(models.Model):
    GENDER_CHOICES = (
        ("e", "Erkek"),
        ("k", "Kadın"),
        ("b", "Belirtmek İstemiyorum"),
    )
    first_name = models.CharField(max_length=25,verbose_name="İsim")
    last_name = models.CharField(max_length=25,verbose_name="Soy İsim")
    gender = models.CharField(max_length=1,choices=GENDER_CHOICES,default="b")

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Article(models.Model):
    title = models.CharField(max_length=25)
    description = models.TextField()
    author_first_name = models.CharField(max_length=30)
    author_last_name = models.CharField(max_length=25,blank=True)
    created_date = models.DateTimeField(auto_now_add=True,verbose_name="oluşturulma tarihi")
    modified_date = models.DateTimeField(auto_now=True,verbose_name="Düzenleme tarihi")
    article_category = models.ManyToManyField("articleCategory",blank=True)
    author = models.ForeignKey("articleUser",on_delete=models.CASCADE,verbose_name="Yazar",null=True,blank=True)


    class Meta:
        db_table = "Makaleler"
        verbose_name = "Makale"
        verbose_name_plural = "Makaleler"
        ordering = ("created_date",)

    def get_full_name(self):
        return self.author_first_name + " " + self.author_last_name

    def __str__(self):
        return self.title

class articleCategory(models.Model):
    name = models.CharField(max_length=50,verbose_name="Kategori İsmi")
    created_date = models.DateTimeField(null=True,blank=True)

    def __str__(self):
        return self.name