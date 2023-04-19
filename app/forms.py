from django import forms
g=[('MALE','male'),('FEMALE','female')]
c=[['PYTHON','python'],('JAVA','java'),['SQL','sql']]
class StudentForm(forms.Form):
    name=forms.CharField(max_length=100)
    age=forms.IntegerField()
    email=forms.EmailField()
    url=forms.URLField()
    date=forms.DateField()
    time=forms.TimeField()
    dateandtime=forms.DateTimeField()
    address=forms.CharField(max_length=100,widget=forms.Textarea(attrs={'col':10,'row':10}))
    password=forms.CharField(max_length=100,widget=forms.PasswordInput)
    #gender=forms.ChoiceField(choices=g)
    gender=forms.ChoiceField(choices=g,widget=forms.RadioSelect)
    #couses=forms.MultipleChoiceField(choices=c)
    courses=forms.MultipleChoiceField(choices=c,widget=forms.CheckboxSelectMultiple)
