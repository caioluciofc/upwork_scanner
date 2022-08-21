import http3
import asyncio
from helpers.exceptions import WrongUsernamePassword

alternative_headers = ["Mozilla/5.0 (X11; Linux x86_64; rv:12.0) Gecko/20100101 Firefox/12.0",
                       "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:15.0) Gecko/20100101 Firefox/15.0.1"]

class UpworkScanner():
    """
    This Scanner has the objective to fetch the user data at Upwork
    It works first fetching the Cross Site Request Forgery (XSRF) token from a simple get request
    on the website and continues using this token for validation on the next iterations.
    If the website refuses to accept the request, it`ll try again with a different header.
    After collecting the token, it`ll try to login using the credentials provided, and after
    the session is logged in, it`ll fetch the data and return a dictionary with the collected data.
    :doc-author: Caio Carvalho
    """
    def __init__(self):
        self.login_url = 'https://www.upwork.com/ab/account-security/login'
        self.home_url = 'https://www.upwork.com/'
        self.profile_url = 'https://www.upwork.com/freelancers/settings/api/v1/contactInfo'
        self.headers = {
            "User-Agent": 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
        }

    async def collect_xsrf_token_data(self):
        async with http3.AsyncClient() as client:
            get_home_url = await client.get(url=self.login_url, headers=self.headers)
            if get_home_url.status_code == 200:
                cookies = get_home_url.cookies.items()
                xsrf_token = [cookie[1] for cookie in cookies if cookie[0] == "XSRF-TOKEN"]
                self.xsrf_token = xsrf_token[0]
                return xsrf_token[0], client
            else:
                return False, False

    async def _login(self, xsrf_token, client, username, password):
        self.headers.update({
            'content-type': 'application/json',
            'x-requested-with': 'XMLHttpRequest',
            'x-odesk-csrf-token': xsrf_token,
            'referer': self.login_url,
        })
        client.cookies.set('XSRF-TOKEN', xsrf_token)
        login_data = {
            "login": {"password": password,
                      "mode": "password",
                      "username": username}
        }
        login_request = await client.post(url=self.login_url,
                                          headers=self.headers,
                                          json=login_data)
        login_request_data = login_request.json()
        if login_request.status_code == 200 and login_request_data.get("success") == 1:
            user_object = await self._collect_data(client)
            return user_object
        elif (login_request_data.get("success") == 0 and 
             login_request_data.get("alerts", {}).get("eventCode") == "wrongPassword"):
            raise WrongUsernamePassword()

    def _parse_data(self, user_data):
        email = user_data.get("email").get("address")
        email_verified = user_data.get("email").get("isVerified")
        first_name = user_data.get("firstName")
        last_name = user_data.get("lastName")
        user_rid = user_data.get("rid")
        user_phone = user_data.get("phone")
        id_verification = True if not user_data.get("isIdVerificationPending") else False
        address_line_1 = user_data.get("address").get("street")
        address_line_2 = user_data.get("address").get("additionalInfo")
        state = user_data.get("address").get("state")
        city = user_data.get("address").get("city")
        country = user_data.get("address").get("country")
        postal_code = user_data.get("address").get("zip")
        profile_picture_link = user_data.get("portrait").get("bigPortrait")
        username = user_data.get("nid")
        user_object = {
            "first_name": first_name,
            "last_name": last_name,
            "full_name": first_name + " " + last_name,
            "user_rid": user_rid,
            "phone_number": user_phone,
            "id_verified": id_verification,
            "email": email,
            "email_verified": email_verified,
            "profile_pic_link": profile_picture_link,
            "username": username,
            "address": {
                "line1": address_line_1,
                "line2": address_line_2,
                "city": city,
                "state": state,
                "postal_code": postal_code,
                "country": country
            }
        }
        return user_object

    async def _collect_data(self, client):
        contact_info_get = await client.get(url="https://www.upwork.com/freelancers/settings/api/v1/contactInfo", headers=self.headers)
        if contact_info_get.status_code == 200:
            user_data = contact_info_get.json()["freelancer"]
            user_object = self._parse_data(user_data)
            return user_object

    async def collect_user_data(self, username, password):
        xsrf_token, client = await self.collect_xsrf_token_data()
        if not xsrf_token and not client:
            # TODO : Also use a proxy here, since eventually the IP will be flagged
            # A good alternative would be using scrapingbee, but since frameworks as
            # such are discouraged, I haven`t used it`
            for header in alternative_headers:
                self.headers = header
                xsrf_token, client = await self.collect_xsrf_token_data()
                if xsrf_token and client:
                    break
        user_object = await self._login(xsrf_token, client, username, password)
        return user_object


