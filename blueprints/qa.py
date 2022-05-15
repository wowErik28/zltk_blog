from datetime import datetime

from flask import Blueprint, render_template, request, g, \
    redirect, url_for
from sqlalchemy import or_

from exts import db
from decorators import login_required
from models import QuestionModel, AnswerModel
from .forms import AnswerForm

bp = Blueprint('qa', __name__, url_prefix='/')


@bp.route('/')
def index():
    questions = QuestionModel.query.filter_by().all()
    if questions:
        context = {'questions': questions}
        return render_template('index.html', **context)
    else:
        return render_template('index.html')


@bp.route('/question/<int:question_id>')
def question_detail(question_id):
    question = QuestionModel.query.get(question_id)

    return render_template('detail.html', question=question, answers=question.answers,
                           answers_num=len(question.answers))


@bp.route('/question/<int:question_id>/answer', methods=['POST'])
@login_required
def upload_answer(question_id):
    form = AnswerForm(request.form)
    # 需要登录
    if form.validate():
        content = form.content.data
        create_time = datetime.now()
        author_id = g.user.id
        answer_model = AnswerModel(content=content, create_time=create_time, question_id=question_id,
                                   author_id=author_id)
        db.session.add(answer_model)
        db.session.commit()
    return redirect(url_for('qa.question_detail', question_id=question_id))

@bp.route('/question/<int:question_id>/delete_answer<int:answer_id>')
@login_required
def delete_answer(question_id, answer_id):
    AnswerModel.query.filter_by(id=answer_id).delete()
    db.session.commit()
    return redirect(url_for('qa.question_detail', question_id=question_id))

@bp.route('/search')
def search():
    q = request.args.get('q') #关键字 string
    questions = QuestionModel.query.filter(or_(QuestionModel.title.contains(q),
                                   QuestionModel.content.contains(q)))
    return render_template('index.html', questions=questions)

