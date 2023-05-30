# BMI system for learning django

**use_form** version by nlhsueh@gmail.com

### form.as_table
update_people.html 直接用 f.as_table() 來呈現
```python
{{ form.as_table }}
```

Try `form.as_p`, or `form.as_ul`, too

### view pass form
views.py 產生 依據 id 對應的 people 產生 form 傳遞給 update_people.html

```python
form = PeopleModelForm(instance = p)    
context = {'form':form}     
return render(request, "update_people.html", context)
```

### widget
forms.py 中針對呈現的設定，投過 widget 設定欄位的呈現屬性

```python
widgets = {
            'pname': forms.TextInput(attrs={'class': 'form-control', 
                  'readonly': 'readonly'}), 
            'h': forms.NumberInput(attrs={'class': 'form-control'}), 
            'w': forms.NumberInput(attrs={'class': 'form-control'}),
}
```

### meta in model
* model.py 加上排序的 meta 設定
* 依據身高排序 
```python
class Meta:
     ordering = ['h']        
```

## Run it
http://127.0.0.1:8000/bmi

http://127.0.0.1:8000/admin
* id: fcu
* pwd: fcu