from models.upwork_user import UpworkUser

def test_model_instantiation():
    mock_data = {'user_rid': '1003840962', 
                 'last_name': 'Backupy', 
                 'full_name': 'Bobby Backupy', 
                 'phone_number': '9176987366', 
                 'id_verified': True, 
                 'email': 'bob.worker+backupaccount@argyle.io', 
                 'email_verified': True, 
                 'profile_pic_link': 'https://www.upwork.com/profile-portraits/c1mLLxjwmuM_8hrcf2IDa4AajZFNGdDSKleHcddaSlYdha-Z2SdY2nLtbFdizwfo-Z', 
                 'address': {
                    'line1': 'Party street 100', 
                    'line2': '1', 
                    'city': 'Miami', 
                    'state': 'FL', 
                    'postal_code': '123456', 
                    'country': 'United States'}, 
                    'username': 'bobbybackupy'}
    mocked_user = UpworkUser(**mock_data)
    assert mocked_user.user_rid
    assert mocked_user.last_name
    assert mocked_user.full_name
    assert mocked_user.phone_number
    assert mocked_user.id_verified
    assert mocked_user.email
    assert mocked_user.email_verified
    assert mocked_user.profile_pic_link
    assert mocked_user.address
