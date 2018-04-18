from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed, FileRequired
from wtforms import StringField,TextAreaField
from wtforms.validators import DataRequired
ALLOWED_EXTENSIONS = [ 'png', 'jpg', 'jpeg', 'gif']

class UploadForm(FlaskForm):
    
    upload = FileField('Photo', validators=[FileRequired(),FileAllowed(ALLOWED_EXTENSIONS, 'Images only!')])
    description=TextAreaField(u'Image Description') 
    



    
