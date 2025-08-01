from flask import Blueprint,render_template,request,current_app,flash,redirect,url_for,send_from_directory,send_file
import os

upload_bp = Blueprint("upload",__name__)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in current_app.config["ALLOWED_EXTENSIONS"]

@upload_bp.route("/upload", methods=["GET", "POST"])
def upload():
    if request.method == "POST":
        if 'file' not in request.files:
            flash("No file part")
            return redirect(url_for('upload.upload'))
        file = request.files['file']
        if file.filename == '':
            flash("沒有選擇檔案")
            return redirect(url_for('upload.upload'))
        if not allowed_file(file.filename):
            flash("不允許的檔案類型")
            return redirect(url_for('upload.upload'))
        filename = file.filename
        file.save(os.path.join(current_app.config['UPLOAD_FOLDER'], filename))
        flash("檔案上傳成功")
        return redirect(url_for('upload.upload'))

    files = os.listdir(current_app.config['UPLOAD_FOLDER'])
    return render_template("upload.html",files=files)

@upload_bp.route('/download/<filename>')
def download_file(filename):
    filepath = os.path.join("../",current_app.config['UPLOAD_FOLDER'])

    try:
        return send_from_directory(filepath , filename, as_attachment=True)
    except FileNotFoundError:
        flash("檔案不存在")
        return redirect(url_for('upload.upload'))