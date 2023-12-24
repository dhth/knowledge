# Pytest order of mock and parameterize

Order of arguments to a test function: Mocks come first (in reverse order), then parameterized stuff, and then the normal fixtures.

```python
    @pytest.mark.parametrize(
        "exception_type, some_val",
        [
            (FailureSavingtoDatabase, 1),
            (FailureSavingtoDataStore, 2),
        ],
    )
    @patch("app.routers.upload.upload_image")
    @patch("app.routers.upload.download_image")
    def test_returns_500_if_failure_in_saving_image(
        self,
        mocked_download_image,
        mocked_upload_image,
        exception_type,
        some_val,
        test_app: TestClient,
    ):
```
