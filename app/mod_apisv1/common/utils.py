def return_error(code, message):
    data_out = {
        'code': code,
        'status': message
    }
    return data_out, code