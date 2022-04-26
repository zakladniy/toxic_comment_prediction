from fastapi import FastAPI
from fastapi.responses import RedirectResponse

from .api_config import api_title, api_desc, logger
from .api_models import Comments
from .model_tools.load_model import load_model_from_file
from .model_tools.predict_tools import get_prediction

app = FastAPI(
    title=api_title,
    description=api_desc,
)

bert_model, bert_tokenizer = load_model_from_file()


@app.get("/")
def redirect_to_docs() -> RedirectResponse:
    """Auto redirect to docs page.

    @return: RedirectResponse
    """
    return RedirectResponse("/docs")


@app.post("/api/toxic_predict")
def product_group_predict(data: Comments) -> dict[str, list[dict]]:
    """API endpoint for predict toxicity of russian comments.

    @param data: russian texts/comments for predict
    @return: label and toxic probability for each comment
    """
    predictions = get_prediction(
        texts=data.comments,
        tokenizer=bert_tokenizer,
        model=bert_model,
    )
    for pred in predictions:
        logger.info(
            f"input_text: {pred['input_text']}, "
            f"class: {pred['class']}, "
            f"toxic_proba: {pred['toxic_proba']}"
        )
    return {
        "data": predictions,
    }
