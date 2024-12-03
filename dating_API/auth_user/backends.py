# class JWTAuthentication(BaseAuthentication):
#     token = TokenValidate()
#
#     def authenticate(self, request):
#         token = self.token.get_token(request)
#         if not token:
#             return (None, None)
#         self.token.validate_token(token)
#         payload = self.token.decoding_token(token)
#         self.token.token_lifetime(payload=payload)
#         user = get_object_or_404(get_user_model(), id=payload.get('sub'))
#         return (user, token)