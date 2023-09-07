from flask import Flask, request, render_template
import os
import s3

app = Flask(__name__)

# Set the upload folder to the current working directory
upload_folder = os.getcwd()+"/docs"

@app.route('/')
def home():
    return render_template('home.html')

@app.route("/upload", methods=["GET", "POST"])
def upload_file():
    if request.method == "POST":
        uploaded_file = request.files["file"]
        if uploaded_file.filename != "":
            file_path = os.path.join(upload_folder, uploaded_file.filename)
            uploaded_file.save(file_path)
            print("Recieved file ", uploaded_file.filename)
            # print(type(uploaded_file.filename))
            s3.upload_file_in_s3(uploaded_file.filename)
            return f"File '{uploaded_file.filename}' has been uploaded and stored in s3 bucket"
    return render_template("upload.html")

@app.route("/search", methods = ['GET','POST'])
def search_files():
    if request.method == "POST":
        search_file = request.form['search_text']
        if s3.check_file_exists_in_s3(search_file):            
            return "Matching files found in S3 bucket"
        else:
            return "No matching file found in S3 bucket"
    return render_template('search.html')

@app.route("/download", methods = ['GET','POST'])
def download_files():
    if request.method == "POST":
        search_file = request.form['search_text']
        local_path = request.form['local_path']
        if s3.download_file_from_s3(search_file,local_path):            
            return "Downloading....."
        else:
            return "Unable to Download file please check the file_name or correct loacl path"
    return render_template('download.html')
if __name__ == "__main__":

    # create_ec2()
    # connect_to_s3()
    app.run(debug=True)

