from unittest import mock
from text2sql.core import Text2SQL
import pytest

@mock.patch("openai._base_client.SyncAPIClient.request", mock.MagicMock())
@mock.patch("langchain_core.runnables.base.Runnable.invoke", mock.MagicMock())
@mock.patch("sqlalchemy.create_engine", mock.MagicMock())
@mock.patch.dict("os.environ", {"OPENAI_API_KEY": "FAKE_KEY"})
def test_model():

    sql = Text2SQL()
    with pytest.raises(IndexError):
        sql.query(question = "test")


