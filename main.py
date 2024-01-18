import time
from fastapi import FastAPI, HTTPException
from database import questions_collection
from chatgpt import query_chatgpt
from bson import ObjectId

app = FastAPI()


@app.get("/query-next-unanswered-question")
async def query_next_unanswered_question():
    # Fetch the next unanswered question
    question_document = questions_collection.find_one({"ChatGPT's response": {"$in": [None, ""]}})

    if not question_document:
        raise HTTPException(status_code=404, detail="No more unanswered questions")

    # Construct the prompt for ChatGPT
    prompt = (f"{question_document['Question']}\nA) {question_document['Option A']}\nB) "
              f"{question_document['Option B']}\nC) {question_document['Option C']}\nD) "
              f"{question_document['Option D']}")
    formatted_prompt = (f"Question: {prompt}\nPlease respond with the correct option in the format 'A' or 'A) Ade' and "
                        f"nothing more.")

    # Start timing before the request
    start_time = time.time()

    # Query ChatGPT
    chatgpt_raw_response = query_chatgpt(formatted_prompt)

    # Stop timing after the response
    end_time = time.time()

    # Calculate the duration
    duration = end_time - start_time

    # Extract the actual response content
    chatgpt_response_content = chatgpt_raw_response.get('choices', [{}])[0].get('message', {}).get('content', '')

    # Update the document with ChatGPT's response content and query time
    questions_collection.update_one({"_id": ObjectId(question_document["_id"])}, {
        "$set": {
            "ChatGPT's response": chatgpt_response_content,
            "Query_duration": duration
        }
    })

    return {
        "question": question_document["Question"],
        "Option A": question_document["Option A"],
        "Option B": question_document["Option B"],
        "Option C": question_document["Option C"],
        "Option D": question_document["Option D"],
        "answer": question_document["Answer"],
        "chatgpt_response": chatgpt_response_content,
        "query_duration": duration
    }


@app.get("/process-all-unanswered-questions")
async def process_all_unanswered_questions():
    unanswered_questions = questions_collection.find({"ChatGPT's response": {"$in": [None, ""]}})

    success_count = 0
    failure_count = 0

    for question_document in unanswered_questions:
        try:
            # Construct the prompt for ChatGPT
            prompt = (f"{question_document['Question']}\nA) {question_document['Option A']}\nB) "
                      f"{question_document['Option B']}\nC) {question_document['Option C']}\nD) "
                      f"{question_document['Option D']}")
            formatted_prompt = (
                f"Question: {prompt}\nPlease respond with the correct option in the format 'A' or 'A) Ade' and "
                f"nothing more.")

            # Query ChatGPT and measure time
            start_time = time.time()
            chatgpt_raw_response = query_chatgpt(formatted_prompt)
            end_time = time.time()
            duration = end_time - start_time

            # Extract the response content
            chatgpt_response_content = chatgpt_raw_response.get('choices', [{}])[0].get('message', {}).get('content',
                                                                                                           '')

            # Update the document with the response and query time
            questions_collection.update_one({"_id": ObjectId(question_document["_id"])}, {
                "$set": {
                    "ChatGPT's response": chatgpt_response_content,
                    "Query_duration": duration
                }
            })

            success_count += 1

        except Exception as e:
            # Increment failure count in case of an error
            failure_count += 1

    return {
        "total_successfully_answered": success_count,
        "total_failed_to_answered": failure_count
    }