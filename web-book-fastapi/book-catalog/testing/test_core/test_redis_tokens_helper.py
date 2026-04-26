# from unittest import TestCase
#
#
# class RedisTokensHelperTestCase(TestCase):
#     def test_generate_and_save_token(self):
#         # Создаем имитацию хелпера (Mock), если реального еще нет
#         class MockRedisHelper:
#             def generate_and_save_token(self, user_id): return "test-token"
#
#             def token_exists(self, token): return True
#
#         helper = MockRedisHelper()
#         token = helper.generate_and_save_token(123)
#
#         self.assertTrue(helper.token_exists(token))