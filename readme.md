# BMI system for learning django

**update_p** version by nlhsueh@gmail.com

!! 有放一些錯誤讓你來修復，請看程式碼內的註解

### 新增 update_people.html

* form 的 method 設為  `"POST"`
* 透過 `{{p}} 來取得 people 的資料
* 只有 `p.w`, `p.h` 可以修改

```python
<form action="" method="POST">
     …
    <input type="text" id="pname" value="{{ p.pname }}" readonly><br>
```    

### `details.html` 中新增 update 的連接

```python
<a href="/bmi/update/{{p.id}}">Update data</a>
```
### 新增 `form.py`, 宣告 `PeopleModelForm`

* 指定 `model=People`
* 指定欄位 `fields = ['pname', 'h', 'w']` 

```python
class PeopleModelForm(forms.ModelForm):
    class Meta:
        model = People
        fields = ['pname', 'h', 'w'] 
```        

### 新增 URL 路徑

* `bmi/update/<int:id>`
* `view.py` 新增 `update(request, id)`

## Run it
http://127.0.0.1:8000/bmi

http://127.0.0.1:8000/admin
* id: fcu
* pwd: fcu
