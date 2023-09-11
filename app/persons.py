from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse
from app.schema import User_schema, User_update_schema, usercreate_response_serializer, user_response_serializer
from app.services import create_user, get_single_user, update_user, delete_user

app = APIRouter()



# create a person
@app.post("/api")
async def create_person(request: User_schema):
    account, error = create_user(request)

    if error:
        raise HTTPException(status_code=error.code, detail=error.msg)

    if not account:
        raise HTTPException(status_code=500, detail="failed to create account")
    
    return usercreate_response_serializer(account)

# get a single person
@app.get("/api/{idorname}")
async def get_single_person(idorname: str):
		account, error = get_single_user(idorname)
        
		if error:
			raise HTTPException(status_code=error.code, detail=error.msg)
		if not account:
			raise HTTPException(status_code=404, detail="user not found")
		return user_response_serializer(account)

# update a person
@app.put("/api/{idorname}")
async def update_person(idorname: str, request: User_update_schema ):
	account, error = get_single_user(idorname)

	if error:
		raise HTTPException(status_code=error.code, detail=error.msg)
	
	if not account:
		raise HTTPException(status_code=404, detail="user not found")
	
	account, error = update_user(
		user_object=account,
		name=request.name,
		email=request.email,
		)

	if error:
		raise HTTPException(status_code=error.code, detail=error.msg)
	
	if not account:
		raise HTTPException(status_code=500, detail="failed to update account")
	
	return user_response_serializer(account)

# delete a person
@app.delete("/api/{idorname}")
async def delete_person(idorname: str):
	account, error = get_single_user(idorname)

	if error:
		raise HTTPException(status_code=error.code, detail=error.msg)
	
	if not account:
		raise HTTPException(status_code=404, detail="user not found")
	
	account, error = delete_user(account)

	if error:
		raise HTTPException(status_code=error.code, detail=error.msg)
	
	if not account:
		raise HTTPException(status_code=500, detail="failed to delete account")
	
	return JSONResponse(status_code=200, content={"msg": "account deleted"})