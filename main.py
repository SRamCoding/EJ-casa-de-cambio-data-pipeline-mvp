from fastapi import FastAPI, HTTPException
from models import Transaction
from database import transactions_collection

app = FastAPI(title="Casa de Cambios API")

@app.post("/transactions")
def create_transaction(transaction: Transaction):
    try:
        # Convertir a dict y guardar en MongoDB
        transaction_dict = transaction.model_dump()
        result = transactions_collection.insert_one(transaction_dict)
        return {"status": "success", "transaction_id": str(result.inserted_id)}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/transactions/{user_id}")
def get_transactions(user_id: str):
    try:
        results = transactions_collection.find({"user_id": user_id})
        transactions = []
        for tx in results:
            tx["_id"] = str(tx["_id"])  # Convertir ObjectId a string
            transactions.append(tx)
        return {"transactions": transactions}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
