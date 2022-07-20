from src import main
from fastapi.testclient import TestClient

app = TestClient(main())