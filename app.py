from flask import Flask
from db import init_db
from lib import crawl_cards

app = Flask(__name__)

if __name__ == "__main__":
    init_db.init_cards_db()
    crawl_cards.crawl_cards()
    app.run(debug=True, use_reloader=False)
# class WixossCards(db.Model):
#   id = db.Column(db.Integer, primary_key=True)
#   name = db.Column(db.String(256), nullable=False)
#   def __repr__(self):
#     return '<WixossCards %r>' % self.id

# db.create_all()

# @app.route("/", methods=['POST', 'GET'])
# def index():
#   if request.method == "POST":
#     task_content = request.form['content']
#     new_task = WixossCards(content=task_content)

#     try:
#       db.session.add(new_task)
#       db.session.commit()
#       if request.accept_mimetypes.accept_json:
#         return jsonify(new_task)
#       else:
#         return redirect('/')
#     except:
#       return "There was an issue inserting into the DB"
#   else:
#     tasks = WixossCards.query.order_by(WixossCards.id).all()
#     return render_template('index.html', tasks=tasks)

# @app.route("/delete/<int:id>")
# def delete(id):
#   task_to_delete = WixossCards.query.get_or_404(id)
#   try:
#     db.session.delete(task_to_delete)
#     db.session.commit()
#     if request.accept_mimetypes.accept_json:
#       return jsonify(task_to_delete)
#     else:
#       return redirect('/')
#   except Exception as e:
#     if request.accept_mimetypes.accept_json:
#       return jsonify({ "error": e }), 500
#     else:
#       return "There was an issue deleting" + e


# @app.route("/update/<int:id>", methods=["GET", "POST"])
# def update(id):
#   task = WixossCards.query.get_or_404(id)
#   if request.method == "POST":
#     task.content = request.form["content"]
#     try:
#       db.session.commit()
#       if request.accept_mimetypes.accept_json:
#         return jsonify(task)
#       else:
#         return redirect('/')
#     except Exception as e:
#       if request.accept_mimetypes.accept_json:
#         return jsonify({ "error": e }), 500
#       else:
#         return "There was an issue updating" + e
#   else:
#     return render_template('update.html', task=task)

# if __name__ == "__main__":
#   app.run(debug=True)