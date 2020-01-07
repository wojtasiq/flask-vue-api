from flask_restplus import fields


user_data_fields = {
    'name': fields.String,
    'surname': fields.String,
    'username': fields.String
}

login_history_fields = {
    'date': fields.String
}