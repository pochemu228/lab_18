# import pytest
# from pydantic import ValidationError
# from schemas.book import BookCreate
#
# class TestBookValidation:
#     # Тест на короткий slug
#     def test_slug_too_short(self):
#         with pytest.raises(ValidationError):
#             BookCreate(slug="ab", title="T", description="D", pages=10)
#
#     # Самостоятельно: тест на длинный slug
#     def test_slug_too_long(self):
#         with pytest.raises(ValidationError):
#             BookCreate(slug="s" * 31, title="T", description="D", pages=10)