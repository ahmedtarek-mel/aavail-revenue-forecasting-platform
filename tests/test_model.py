from src.model import run_model


def test_model_training():
    model = run_model("data/cs-train")
    assert model is not None
