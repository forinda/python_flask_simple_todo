from todo import app
from todo.models import Todo,db
from todo.forms import TodoCreationForm
from todo.forms import TodoUpdateForm
from flask import (request,
                    redirect,
                    url_for,
                    render_template,
                    flash,
                    session
                    )

@app.route('/')
@app.route('/index')
@app.route('/home')
def index():
    todos = Todo.query.all()
    return render_template('index.html', todos=todos)


@app.route('/add',methods=['GET','POST'])
def add():
    title='add'
    form = TodoCreationForm()
    if form.validate_on_submit():
        todo = Todo(body=form.body.data, done=form.done.data)
        db.session.add(todo)
        db.session.commit()
        flash("Todo added successfully")
        return redirect(url_for('index'))
    
    return render_template('add.html', form=form, title=title)

@app.route('/update/<int:id>',methods=['GET','POST'])
def update(id):
    title='updtate'
    form = TodoUpdateForm()
    todo = Todo.query.filter_by(id=id).first()
    if form.validate_on_submit():
        todo.body = form.body.data
        db.session.commit()
        flash("Todo updated successfully")
        return redirect(url_for('index'))
    if request.method == 'GET':
        form.body.data = todo.body
        # form.done.data = todo.done
    return render_template('update.html', form=form, title=title)

@app.route('/delete/<int:id>',methods=['GET','POST'])
def delete(id):
    td=Todo.query.get(id)
    print(td.id)
    db.session.delete(td)
    db.session.commit()
    return redirect('/')

