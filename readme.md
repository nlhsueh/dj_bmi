# BMI system for learning django

photo version

### ImageField
* models 中的 People 新增 ImageField 的 photo 欄位，用以儲存 people 的照片

```python
photo = models.ImageField(upload_to="people/", null=True, blank=True)
```

### admin 介面上呈現 photo

```python
list_display = ("pname", "h", "w", "photo")
```

settings.py 要加上 media 的路徑
* MEDIA_URL
* MEDIA_ROOT
* STATIC_URL

```python
import os
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'
```

### 修改 urls.py

擴充 urlpatterns

```python
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('bmi.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

### 修改 details.html
* `{{p.photo.url}}` 取得照片路徑

```python
<img src="{{p.photo.url}}" width="200">
```

## Run it
http://127.0.0.1:8000/bmi

http://127.0.0.1:8000/admin
id: fcu
pwd: fcu