from flask import Flask
from app import views
app=Flask(__name__)

app.add_url_rule('/skills','skills',views.skills)
app.add_url_rule('/','index',views.index)
app.add_url_rule('/certificates','certificates',views.c)
app.add_url_rule('/experience','experience',views.exper)
app.add_url_rule('/personalprojects','personalprojects',views.pp)
app.add_url_rule('/about','about',views.about)



if __name__ == '__main__':
    app.run(debug=True)