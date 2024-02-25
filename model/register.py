#model/register.py
import hashlib
from util.database import get_mysql_connection
from util.config import send_success_response, send_error_response

def hash_password(password):
    return hashlib.md5(password.encode()).hexdigest()

def register_query(data):
    try:
        email = data.get('email')
        plain_password = data.get('password')

        connection = get_mysql_connection()
        cursor = connection.cursor()

        cursor.execute("SELECT COUNT(*) FROM tbl_user WHERE email = %s", (email,))
        count = cursor.fetchone()[0]

        if count > 0:
            cursor.close()
            connection.close()
            return send_error_response(400, {'error': 'Email already exists'}, 400)

        hashed_password = hash_password(plain_password)
        data['password'] = hashed_password

      
        cursor.execute("""
            INSERT INTO registration
            (email, password, prefix, firstName, midName, lastName, organization, industryType,
            postalAddress, street, state, country, pincode, highestQualification, yearOfPassing)
            VALUES (%(email)s, %(password)s, %(prefix)s, %(firstName)s, %(midName)s, %(lastName)s,
                    %(organization)s, %(industryType)s, %(postalAddress)s, %(street)s, %(state)s,
                    %(country)s, %(pincode)s, %(highestQualification)s, %(yearOfPassing)s)
        """, data)

        connection.commit()
    except Exception as e:
        return send_error_response(500, {'error': str(e)}, 500)
    finally:
        cursor.close()
        connection.close()

    return send_success_response({'message': 'Registration successful'}, 201)
