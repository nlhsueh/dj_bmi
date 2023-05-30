# BMI system for learning django

**use_BS** version by nlhsueh@gmail.com


### base.html 加入 link 標記
* 加入 container, container-fluid 來格式化容器

```python
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.3/dist/css/bootstrap.min.css" rel="stylesheet">
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.3/dist/js/bootstrap.bundle.min.js"></script>
```

### 加上一個滿版的 Jumbotron

```python
<div class="mt-1 p-3 bg-success text-white text-center rounded">
   <h1>Run! Don't Walk</h1>
   <img src="/media/nba_banner.jpeg">
   <p class="mt-2">Either you're running for food, or you are running from becoming food.</p>
</div>
```

### peoples.html 改用 list-group 

```python
<ul class="list-group list-group-flush">
    {% for p in plist %}
    <li class="list-group-item"> <img src="{{p.photo.url}}" height="40" width="40"> <a
            href="details/{{p.id}}">{{p.pname}}</a>, {{p.h}}cm,
        {{p.w}}kg, BMI: {{p.bmi}}
    </li>
    {% endfor %}
</ul>
```

### details.html 改用 card 來美化球員資料
* card-img-top
* card-body, card-title
* btn, btn-primary
* tooltip 加上一些提示訊息

```python
<div class="card" style="width:300px">
…
```

### update_people.html 修改
* 改用 form-label, form-control 來標記 form 元件
* 透過 mb-1 調整間距

```python
<div class="mb-1">
   <label class="form-label" for="weight"> …
   <input class="form-control" type="number" …
</div>
```

## Run it
http://127.0.0.1:8000/bmi

http://127.0.0.1:8000/admin
* id: fcu
* pwd: fcu