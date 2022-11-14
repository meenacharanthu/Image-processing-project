from flask import Flask, request, render_template, send_from_directory
import ans01
import temp2
import shutil
import os

app = Flask(__name__, static_folder='templates\Homepage - Semantic_files')

if not os.path.exists('stamp_dir'):
    os.makedirs('stamp_dir')
if not os.path.exists('sign_dir'):
    os.makedirs('sign_dir')
shutil.rmtree('sign_dir')
shutil.rmtree('stamp_dir')
if not os.path.exists('stamp_dir'):
    os.makedirs('stamp_dir')
if not os.path.exists('sign_dir'):
    os.makedirs('sign_dir')


@app.route('/cdn/<path:filename>')
def custom_static(filename):
    return send_from_directory(app.config['CUSTOM_STATIC_PATH'], filename)

@app.route('/', methods=['GET', 'POST'])
def f():
    if request.method == "POST":
        # if not os.path.isdir(app.config['UPLOAD_FOLDER']):
        #   os.mkdir(app.config['UPLOAD_FOLDER'])

        f1 = request.files["upload_1"]
        if f1:
            path1 = os.path.join('stamp_dir', f1.filename)
            f1.save(path1)
        # print(path1)

        # print(path2)
        fixed_distance = float(request.form.get("fixed_distance"))
        

        # print(path1)
        if request.form["action"] == "Generate transcript(s)":
            ans01.list_generation(fixed_distance,f1.filename)
            


        # print(os.listdir('sign_dir'))
    return render_template('view.html')


if __name__ == '__main__':
    app.run(debug=True)




